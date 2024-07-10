import copy
import json
import random
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from DrissionPage import SessionPage

from common.content_utils import process_news_content
from common.form_utils import set_nested_value, format_date, clean_news_data, remove_duplicates, is_json
from scraper.basic_page import PageMother


class Scraper(PageMother):
    """
    爬虫母类，用于爬取新闻数据。
    爬取流程：
    1. 爬取新闻列表页面，获取所有新闻的URL，日期，标题等信息。
    2. 清理数据，去除无用数据，并将数据存储到列表中。格式为
        [{'province': '省份名称', 'city': '城市名称', 'url': '新闻URL', 'date': '新闻日期', 'topic': '新闻标题'},
        {...}, {...}]。
    3. 爬取新闻内容页面，获取新闻正文。
    4. 存储数据到文件。
    """

    def __init__(self, city_info: dict, method: str, data_type: str,
                 content_xpath: dict = None, is_headless=True,
                 thread_num: int = 3, proxies: dict = None,
                 extracted_method: callable = None, **kwargs):
        """
        初始化爬虫

        必须参数：
        :param city_info: 城市信息，格式为{'province': '省份名称', 'city': '城市名称'}
        :param method: 请求方法，GET 或 POST
        可选参数：
        :param content_xpath: xpath规则，用于提取新闻URL
        :param is_headless: 是否使用无头浏览器
        :param thread_num: 最大线程数
        :param proxies: 代理
        """
        super().__init__(city_info, content_xpath, is_headless, thread_num, proxies)

        self.method = method
        self.data_type = data_type

        # params 用于传递给requests.get或requests.post的参数
        self.params = kwargs

        # 可选参数
        # 用于指定爬取的页数
        self.page_num_start = kwargs.pop('page_num_start', 1)
        # 用于指定爬取的页数间隔
        self.num_added_each_time = kwargs.pop('num_added_each_time', 1)
        self.post_data = kwargs.pop('post_data', '')
        self.page_num_name = kwargs.pop('page_num_name', None)

        # 用于指定监听新闻的URL路径
        self.listen_name = kwargs.pop('listen_name', None)

        # 用于指定提取新闻信息的方法
        self.extracted_method = extracted_method

        self.is_post_by_json = kwargs.pop('is_post_by_json', False)

        # 用于判断是否停止爬取
        self.is_stop = False
        # 用于记录爬取到的内容全部为None的新闻数量
        self.null_news_num = 0

        self.logger.info(f"{self.city_name} - 开始爬取数据 - 爬取方法为{self.method.upper()} - 数据类型为{self.data_type.upper()}")

    def run(self):
        """
        运行爬虫
        """
        if self.method.upper() == 'LISTEN':
            self.method_LISTEN()
        else:
            self.fetch_data()
        self.save_files()

    def fetch_data(self):
        with ThreadPoolExecutor(max_workers=self.thread_num) as executor:
            futures = []
            for i in range(self.total_page_num):
                if self.is_stop:
                    break  # 提前终止提交新任务

                current_page_num = self.page_num_start + i * self.num_added_each_time
                future = executor.submit(self.fetch_page_data, current_page_num)
                futures.append(future)

            for future in as_completed(futures):
                news_list = future.result()

                # 判断是否停止爬取
                self.detect_stop_status()
                if self.is_stop:
                    break  # 提前终止处理结果

                if news_list:
                    self.unique_news.extend(news_list)
                    news_list = remove_duplicates(news_list)
                    # 确保对列表的修改是线程安全的
                    self.process_and_store_news(news_list)

    def fetch_page_data(self, page_index):
        """
        爬取单个页面的数据

        :param page_index: 当前页码
        :return: 解析后的新闻列表
        """

        if self.method.upper() == 'GET':
            session = self.method_GET(page_index)
        elif self.method.upper() == 'POST':
            session = self.method_POST(page_index)
        elif self.method.upper() == 'POST_CHANGE':
            session = self.method_POST_CHANGE(page_index)
        else:
            raise ValueError("Unsupported method")

        try:
            if self.data_type.upper() == 'JSON':
                news_list = self.parse_json(session)
            elif self.data_type.upper() == 'HTML':
                news_list = self.parse_html(session)
            else:
                news_list = None
        except Exception as e:
            self.logger.error(f"{self.city_name} - 第{page_index}页数据解析失败：{e}")
            return []

        self.logger.info(f"{self.city_name} - 正在爬取第 {int(page_index/self.num_added_each_time)}/{self.total_page_num} 页数据 - "
                         f"获取URL数据 {len(news_list)}/{self.each_page_news_num} 条"
                         f" - 已获取 {len(self.unique_news)}/{self.total_news_num} 条新闻URL")

        return news_list

    def process_and_store_news(self, news_data, is_direct_fetch=False):
        """
        处理并存储新闻数据
        :param news_data:
        :param is_direct_fetch:
        :return:
        """

        with self.lock:
            if is_direct_fetch:
                self.total_news_data.extend(news_data)
            else:
                data_list = process_news_content(news_data, self.page, [])

                # 确保返回的数据长度大于1，否则视为无效数据
                if len(data_list) < 2:
                    self.null_news_num += 1

                self.total_news_data.extend(data_list)
            self.logger.info(f"{self.city_name} - 已成功获取 {len(self.total_news_data)}/{self.total_news_num} 条新闻正文数据")

    def method_GET(self, current_page_num):
        """
        爬取GET请求的页面

        :param current_page_num: 当前页码

        :return: 爬取到的页面 SessionPage对象
        """
        session = SessionPage()

        url = self.set_url(current_page_num)

        self.logger.info(f"{self.city_name} - URL: {url}")

        session.get(url=url, proxies=self.proxies, **self.params, timeout=30)
        # session = requests.get(url=url, proxies=self.proxies, **self.params, timeout=30)
        time.sleep(random.randrange(1, 2))

        return session

    def method_POST(self, current_page_num):
        """
        爬取POST请求的页面

        :param current_page_num: 当前页码

        :return: 爬取到的页面 SessionPage对象
        """
        session = SessionPage()

        # 复制参数字典，防止原参数字典被修改
        data_copy = self.set_url(current_page_num)

        # 判断是否为json数据
        if self.is_post_by_json:
            session.post(url=self.base_url, proxies=self.proxies, json=data_copy, **self.params)

            # session.post(url=data_copy, proxies=self.proxies, json=self.post_data, **self.params)
            if session.response.status_code == 200:
                time.sleep(random.randrange(1, 2))
                return session

        try:
            session.post(url=self.base_url, proxies=self.proxies, data=data_copy, **self.params)
            # session = requests.post(url=self.base_url, proxies=self.proxies, data=data_copy, **self.params)
        except Exception as e:
            session.post(url=self.base_url, proxies=self.proxies, json=data_copy, **self.params)
        finally:
            if isinstance(session, SessionPage):
                if session.response.status_code != 200:
                    session.post(url=self.base_url, proxies=self.proxies, json=data_copy, **self.params)
                    if session.response.status_code == 200:
                        self.is_post_by_json = True

            pass

        time.sleep(random.randrange(1, 2))
        return session

    def method_POST_CHANGE(self, current_page_num):
        """
           爬取POST请求的页面

           :param current_page_num: 当前页码

           :return: 爬取到的页面 SessionPage对象
       """
        session = SessionPage()

        # 复制参数字典，防止原参数字典被修改
        data_copy = self.set_url(current_page_num)

        # 判断是否为json数据
        if self.is_post_by_json:
            session.post(url=data_copy, proxies=self.proxies, json=self.post_data, **self.params)
            if session.response.status_code == 200:
                time.sleep(random.randrange(1, 2))
                return session

        try:
            session.post(url=data_copy, proxies=self.proxies, data=self.post_data, **self.params)
            # session = requests.post(url=self.base_url, proxies=self.proxies, data=data_copy, **self.params)
        except Exception as e:
            session.post(url=self.base_url, proxies=self.proxies, json=data_copy, **self.params)
        finally:
            if isinstance(session, SessionPage):
                if session.response.status_code != 200:
                    session.post(url=self.base_url, proxies=self.proxies, json=data_copy, **self.params)
                    if session.response.status_code == 200:
                        self.is_post_by_json = True

            pass

        time.sleep(random.randrange(1, 2))
        return session

    def method_LISTEN(self):
        """
        监听新闻页面

        监听新闻页面，获取新闻列表，并存储到列表中。
        :return:
        """

        page = self.page

        news_list = []

        if self.data_type.upper() == 'JSON':
            page.listen.start(self.listen_name)

        url = self.set_url(1)

        page.get(url)

        for i in range(self.total_page_num):

            if self.data_type.upper() == 'JSON':
                page.wait(2, 3)

                while True:

                    res = page.listen.wait()

                    json_data = res.response.body

                    extracted_data = self.parse_json(json_data)

                    if len(extracted_data) > 0:
                        news_list.extend(extracted_data)
                        break

            elif self.data_type.upper() == 'HTML':
                news_list = self.parse_html(page)

            self.logger.info(f"{self.city_name} - 正在爬取第 {i}/{self.total_page_num} 页数据 - "
                             f"获取URL数据 {len(news_list)}/{self.each_page_news_num} 条"
                             f" - 已获取 {len(self.unique_news)}/{self.total_news_num} 条新闻URL")

            # 处理新闻数据
            if news_list:
                self.unique_news.extend(news_list)
                news_list = remove_duplicates(news_list)
                # 确保对列表的修改是线程安全的
                self.process_and_store_news(news_list)

            # 点击下一页按钮
            try:
                next_button = page.ele(self.content_xpath['next_button'])
                next_button.click()
                page.wait(1, 3)
            except Exception as e:
                self.logger.success(f"{self.city_name} - 解析完成，无下一页按钮")
                break

    def parse_json(self, session):
        """
        解析json数据


        :param session: 爬取到的页面 SessionPage对象
        :return: 解析后的新闻列表
            格式为[{'province': '省份名称', 'city': '城市名称', 'url': '新闻URL', 'date': '新闻日期', 'topic': '新闻标题'},
                             {...}, {...}, {...}]
        """

        if isinstance(session, SessionPage):
            json_data = session.json if session.json else session.html
        elif isinstance(session, requests.Response):
            json_data = session.content.decode('utf-8')
        else:
            json_data = session

        news_list = []

        # 调用自定义的提取方法
        if self.extracted_method:
            json_list = self.extracted_method(json_data, self.page_num_start, self.logger)
        else:
            json_list = json_data

        # 遍历json列表，清理数据
        if isinstance(json_list, list):
            for news in json_list:
                news['province'] = self.province_name
                news['city'] = self.city_name
                # 清理数据
                cleaned_dict = clean_news_data(news)
                news_list.append(cleaned_dict)

        if isinstance(session, SessionPage):
            session.close()
        return news_list

    def parse_html(self, session):
        """
        解析html数据

        :param session: 爬取到的页面 SessionPage对象
        :return: 解析后的新闻列表
            格式为[{'province': '省份名称', 'city': '城市名称', 'url': '新闻URL', 'date': '新闻日期', 'topic': '新闻标题'},
                             {...}, {...}, {...}]
        """

        news_list = []

        # 获取元素
        frames = session.eles(self.content_xpath['frames'])
        for frame in frames:
            try:
                if isinstance(frame.ele(self.content_xpath['title']), str):
                    title = frame.ele(self.content_xpath['title'])
                else:
                    title = frame.ele(self.content_xpath['title']).text or frame.ele(self.content_xpath['title']).attr('title')

                # 获取日期
                date = None
                for xpath in self.content_xpath['date']:
                    date = frame.ele(xpath)
                    if date:
                        if isinstance(date, str):
                            date = format_date(date.strip())
                        else:
                            date = format_date(date.text.strip())
                        break
                if not date:
                    date = '2024-01-01'

                # 获取URL
                if 'url' not in self.content_xpath or not self.content_xpath['url']:
                    title_url = frame.ele(self.content_xpath['title']).attr('data-url') or frame.ele(
                        self.content_xpath['title']).attr('href')
                else:
                    title_url = frame.ele(self.content_xpath['url']).attr('href')

            except Exception as e:
                continue

            # script_content = frame.text
            #
            # # 使用正则表达式来提取标题，URL和日期
            # title = re.search(r'class="searchresulttitle".*?>(.*?)<', script_content)
            # title_url = re.search(r'href="(.*?)"', script_content)
            # date = re.search(r'(\d{4}-\d{2}-\d{2})', script_content)
            #
            # title = title.group(1) if title else None
            # title_url = title_url.group(1) if title_url else None
            # date = date.group(1) if date else None

            if title_url:
                news_dict = {'province': self.province_name, 'city': self.city_name,
                             'topic': title, 'date': date, 'url': title_url}

                # 清理URL字符串
                cleaned_dict = clean_news_data(news_dict)

                # 将提取的信息存储在字典中，并添加到列表
                news_list.append(cleaned_dict)

        if self.method.upper() == 'POST':
            session.close()
        return news_list

    def set_url(self, current_page_num):
        """
        设置URL
        :param current_page_num: 当前页码
        :return: URL或参数字典
        """

        if self.method.upper() == 'GET' or self.method.upper() == 'LISTEN' or self.method.upper() == 'POST_CHANGE':
            url = self.base_url.format(page_num=current_page_num)

            return url

        elif self.method.upper() == 'POST':
            # 复制参数字典，防止原参数字典被修改
            data_copy = copy.deepcopy(self.post_data) if self.post_data else {}
            # 设置页码参数
            if self.page_num_name:
                data_copy = set_nested_value(data_copy, self.page_num_name, str(current_page_num))

            return data_copy

    def detect_stop_status(self):
        if self.null_news_num >= 20:
            self.is_stop = True
            self.logger.warning(f"{self.city_name} - 已获取 {len(self.total_news_data)}/{self.total_news_num} 条新闻正文数据全部为None，停止爬取")

