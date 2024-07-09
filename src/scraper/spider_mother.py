import copy
import json
import math
import sys
import threading
import time
from typing import List, Callable
import requests
from DrissionPage import ChromiumPage, ChromiumOptions, SessionPage
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
from lxml import html
from requests import RequestException
import requests
import urllib3

from src.common.content_utils import *
from src.common.form_utils import *

# 禁用 InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss} - <level>{level}</level> - {message}</green>",
    level="INFO",
)


class PageMother:
    def __init__(self, city_info: dict,
                 content_xpath: dict = None, is_headless=False, thread_num: int = 5, proxies: dict = None):
        """
        初始化爬虫母类。

        参数:
        name (str): 爬虫名称。
        url (str): 基础URL，用于构造访问的完整URL。
        total_page_num (int): 需要爬取的总页数。
        date_xpath (dict): 存储有关日期的XPath的字典。
        is_headless (bool): 是否启用无头浏览器模式。
        """
        # 必须参数
        self.name = city_info['name']
        self.base_url = city_info['base_url']
        self.targeted_year = city_info['targeted_year'] - 1
        self.province = city_info['province']
        self.total_news_num = city_info['total_news_num']
        self.each_news_num = city_info['each_page_num']
        self.total_page_num = math.ceil(city_info['total_news_num'] / city_info['each_page_num']) + 1

        # 选用参数
        self.content_xpath = content_xpath or {}
        self.is_headless = is_headless
        self.thread_num = thread_num
        self.proxy = proxies if proxies is not None else {"http": None, "https": None}

        # 存储新闻数据
        self.news_data = []
        # 存储去重后的新闻数据
        self.unique_news = []
        # 多线程程序锁
        self.lock = threading.Lock()

        # 初始化浏览器
        self.start_page()

    def start_page(self):
        """根据是否为无头模式初始化浏览器页面。"""

        options = ChromiumOptions()
        options.auto_port()
        # 无头模式
        if self.is_headless:
            options.headless()
        # 是否需要模拟请求
        self.page = ChromiumPage(options)

        logger.info(f"{self.name} - 爬取年份为{self.targeted_year} - 新闻数量为{self.total_news_num}条 - "
                    f"页数有{self.total_page_num - 1}页 - 爬虫最大进程数为{self.thread_num}")

    def fetch_web_multiple(self, frames_xpath=None, title_xpath=None, date_xpath=None, listen_target=None,
                           cleaned_method: Callable = None, by_method: str = None, is_begin_from_zero=None):
        """多线程抓取web页面数据并处理重复数据。"""
        if is_begin_from_zero:
            page_range = range(0, self.total_page_num - 1)
        else:
            page_range = range(1, self.total_page_num)

        with ThreadPoolExecutor(max_workers=self.thread_num) as executor:
            # # 直接通过get请求网页，返回json获取
            if by_method == "by_json":
                future_to_url = {
                    executor.submit(
                        self.get_data_from_json, self.base_url.format(page_num=page_num),
                        page_num): page_num for page_num in page_range
                }
            # 监听post请求，返回json数据
            elif by_method == "by_listen":
                future_to_url = {
                    executor.submit(
                        self.get_data_from_listen, self.base_url.format(page_num=page_num),
                        page_num, listen_target, is_new_tab=True): page_num for page_num in page_range
                }
            elif by_method == "by_session":
                future_to_url = {
                    executor.submit(
                        self.get_data_from_listen, self.base_url.format(page_num=page_num),
                        page_num, listen_target, is_new_tab=True): page_num for page_num in page_range
                }
            # 通过页面XPAth获取
            else:
                future_to_url = {
                    executor.submit(
                        self.get_data_from_page, self.base_url.format(page_num=page_num),
                        page_num, frames_xpath, title_xpath, date_xpath): page_num for page_num in page_range
                }

            for future in as_completed(future_to_url):
                try:
                    news_data = future.result()
                    if cleaned_method:
                        filtered_data = cleaned_method(news_data['json_dict'], self.targeted_year,
                                                       news_data['page'], logger)
                    else:
                        filtered_data = news_data['json_dict']

                    if filtered_data:
                        # 去重
                        unique_data = remove_duplicates(filtered_data)
                        self.process_and_store_news(unique_data)
                except Exception as e:
                    logger.error(f"处理future结果时发生错误: {e}")

        # 存储在Excel中
        self.save_files()

    def fetch_web_by_click(self, next_button_xpath: str, process_json_method: Callable,
                           target_path=None, by_method: str = None):
        """无法多线程操作，只能通过点击进入下一页"""
        self.page.get(self.base_url)
        if by_method == 'by_listen':
            self.page.listen.start(target_path)
        # time.sleep(20)
        # 手动输入参数
        # time.sleep(20)
        """通过页面点击进入下一页"""
        for page_num in range(1, self.total_page_num):
            if by_method == 'by_listen':
                news_data = self.get_data_from_listen(self.page.url, page_num, target_path)
            elif by_method == 'by_json':
                news_data = self.get_data_from_json(self.page.url, page_num)
            else:
                # 不能多开操作，通过
                news_data = self.get_data_from_page('', page_num, is_by_click=True)

            if news_data:
                # 自定义的获取json的函数方法
                cleaned_json_data = process_json_method(news_data)
                self.news_data.extend(cleaned_json_data)

            # 点击"下一页"按钮
            try:
                page_button = self.page.ele(next_button_xpath)
                page_button.click()
            except Exception as e:
                page_button = self.page.ele(next_button_xpath)
                page_button.click(by_js=True)
                logger.warning(f"下一页按钮错误 - {e}")
            finally:
                time.sleep(2)
                logger.info("进入下一页")

        self.news_data = remove_duplicates(self.news_data)
        self.get_content()

    def fetch_web_by_json(self, cleaned_method: Callable = None):
        """当页面为json格式时，且包含内容时，使用多线程直接获取api接口"""

        with ThreadPoolExecutor(max_workers=self.thread_num) as executor:  # 可以调整 max_workers 根据需要
            # 创建未来任务列表
            futures = [executor.submit(self.get_data_from_json, self.base_url.format(page_num=page_num), page_num)
                       for page_num in range(1, self.total_page_num)]

            for future in as_completed(futures):
                try:
                    news_data = future.result()
                    # 是否需要清洁
                    if cleaned_method:
                        filtered_data = cleaned_method(news_data['json_dict'], self.targeted_year,
                                                       news_data['page'], logger)
                    else:
                        filtered_data = news_data
                    # 进程锁
                    if news_data:
                        # 去重
                        news_data = remove_duplicates(filtered_data)
                        self.process_and_store_news(news_data, is_direct_fetch=True)
                except Exception as e:
                    logger.error(f"通过URL获取内容时，出现问题: {e}")

        # 存储在Excel中
        self.save_files()

    def fetch_web_by_requests(self, request_type: str, data_dict: dict = None,
                              page_num_name: str = '', cleaned_method: Callable = None,
                              update_time_to: bool = False, off_set: int = 1,
                              base_url: str = None, change_url=None, headers=None, data_type: str = 'data',
                              is_begin_from_zero=False, is_versify=True, is_by_requests=False):
        """
        通用方法以多线程方式抓取网页内容，支持POST和GET请求。

        参数:
        request_type (str): 请求类型，'get' 或 'post'。
        data_dict (dict): 如果是 POST 请求，使用的数据字典。
        page_num_name (str): POST 请求中页码参数的名称。
        cleaned_method (Callable): 清洁数据的方法。
        update_time_to (bool): 是否更新时间戳。
        """
        if is_begin_from_zero:
            page_range = range(0, self.total_page_num - 1)
        else:
            page_range = range(1, self.total_page_num)

        with ThreadPoolExecutor(max_workers=self.thread_num) as executor:  # 使用线程池处理并发请求
            futures = []
            for page_num in page_range:  # 遍历页面编号范围
                data_dict_copy = copy.deepcopy(data_dict) if data_dict else {}
                if page_num_name:
                    set_nested_value(data_dict_copy, page_num_name, str(page_num * off_set))
                if update_time_to:  # 如果需要更新时间
                    data_dict_copy['time_to'] = int(time.time())  # 更新时间戳为当前时间

                # 动态构建函数调用
                if request_type == 'post':
                    future = executor.submit(self.get_data_from_post, data_dict_copy, page_num,
                                             headers=headers, is_versify=is_versify)  # 提交post请求数据获取任务
                elif request_type == 'post_xpath':
                    future = executor.submit(self.get_data_from_post_xpath, data_dict_copy,
                                             page_num, headers=headers)  # 提交post_xpath请求数据获取任务
                elif request_type == 'post_session':
                    if change_url:
                        # 提交带会话的post请求数据获取任务
                        future = executor.submit(self.get_data_from_post, data_dict_copy,
                                                 page_num, is_by_session=True,
                                                 post_url=f'{change_url}{page_num}/10',
                                                 data_type=data_type, headers=headers, is_versify=is_versify)
                    else:
                        future = executor.submit(self.get_data_from_post, data_dict_copy, page_num,
                                                 is_by_session=True, headers=headers,
                                                 data_type=data_type, is_versify=is_versify)  # 提交带会话的post请求数据获取任务
                # 提交get请求数据获取任务
                elif request_type == 'get':
                    future = executor.submit(self.get_data_from_get, page_num * off_set, headers=headers,
                                             is_versify=is_versify)
                elif request_type == 'get_xpath':
                    future = executor.submit(self.get_data_from_get_xpath, page_num * off_set, headers=headers,
                                             is_versify=is_versify, is_by_requests=is_by_requests, base_url=base_url)
                futures.append(future)  # 将任务future添加到列表中

            # 通过as_completed在任务完成时收集结果
            for future in as_completed(futures):

                news_data = future.result()
                try:
                    # 是否需要清洁
                    if cleaned_method:
                        filtered_data = cleaned_method(news_data['json_dict'], self.targeted_year,
                                                       news_data['page'], logger, base_url=base_url)
                    else:
                        filtered_data = news_data
                except Exception as e:
                    logger.error(f"进行清理函数时，出现问题: {e}")
                # 进程锁
                if filtered_data:
                    try:
                        # 去重
                        news_data = remove_duplicates(filtered_data)
                        self.process_and_store_news(news_data)
                    except Exception as e:
                        logger.error(f"获取详细新闻内容时，出现问题: {e}")

        self.save_files()

    def process_and_store_news(self, news_data, is_direct_fetch=False):
        with self.lock:  # 确保对列表的修改是线程安全的
            if is_direct_fetch:
                self.unique_news.extend(news_data)
            else:
                self.unique_news = process_news_content(news_data, self.page, self.unique_news)

    """访问URL列表，获取详细内容信息"""

    def get_content(self):
        # 获取新闻信息
        self.unique_news = process_news_content(self.news_data, self.page, self.unique_news)

        self.save_files()

    def get_data_from_page(self, url, page_num, frames_xpath=None, title_xpath=None, date_xpath=None,
                           is_by_click=False):
        """
        从给定的URL加载新闻列表。
        参数:
        url -- 要访问的网址。
        page_num -- 当前页码。
        frames_xpath -- 用于查找新闻框架的XPath。
        title_xpath -- 用于查找新闻标题的XPath。
        date_xpath -- 用于查找新闻日期的XPath列表。
        is_by_click -- 是否通过点击进行翻页。
        """
        # 设置默认参数值
        if frames_xpath is None:
            frames_xpath = self.content_xpath['frames']
        if title_xpath is None:
            title_xpath = self.content_xpath['title']
        if date_xpath is None:
            date_xpath = self.content_xpath['date']

        # time.sleep(5)
        # 是否靠点击查找下一页
        if not is_by_click:
            tab = self.page.new_tab()
            tab.get(url)
            if page_num % 10 == 0:
                logger.info(f"当前的页数：{page_num}/{self.total_page_num} - URL：{url}")
        else:
            tab = self.page
            if page_num % 10 == 0:
                logger.info(f"当前的页数：{page_num}/{self.total_page_num}")

        news_frames = tab.eles(frames_xpath)
        # 获取所有标题
        titles = [frame.ele(title_xpath) for frame in news_frames]
        # 获取所有日期
        dates = []
        for frame in news_frames:
            date = None
            for xpath in date_xpath:
                if frame.ele(xpath):
                    date = frame.ele(xpath)
                    break
            dates.append(date)

        news_data = fetch_news_data(titles, dates, url, self.targeted_year, page_num)
        if not is_by_click:
            tab.close()
        return {'json_dict': news_data}

    def get_data_from_json(self, url, page_num):
        """
        通过get访问API，返回的json数据获取URL内容

        :param url: 遍历的URL
        :param page_num: 当前的页数
        :return: data: Dict {{}}
        """
        tab = self.page.new_tab()
        tab.get(url)
        if page_num % 10 == 0:
            logger.info(f"当前的页数：{page_num}/{self.total_page_num} - URL：{url}")

        # 解析 HTML
        soup = BeautifulSoup(tab.html, 'html.parser')

        if soup:
            # 获取无标签的文本
            json_str = soup.get_text()

            # 转换 JSON 字符串为 Python 字典
            data = json.loads(json_str)
            tab.close()
            return data
        else:
            return None

    def get_data_from_listen(self, url, page_num, listen_target, is_new_tab=False):
        """
        通过监听post请求。返回URL信息

        :param is_new_tab:
        :param listen_target:
        :param url: 遍历的URL
        :param page_num: 当前的页数
        :return: data: Dict {{}}
        """

        if is_new_tab:
            tab = self.page.new_tab()
            tab.listen.start(listen_target)
            tab.get(url)
        else:
            tab = self.page

        res = tab.listen.wait(timeout=10)
        # 防止无法抓取到包
        try:
            data_dict = res.response.body
        except Exception as e:
            tab.refresh()
            res = tab.listen.wait(timeout=20)
            data_dict = res.response.body
            if not data_dict:
                logger.error(f"第{page_num}页无法抓取到目标数据包 - {e} - URL：{url}")
                return None
        if page_num % 10 == 0:
            logger.info(f"当前的页数：{page_num} - URL：{url}")

        if is_new_tab:
            tab.close()

        if data_dict:
            return {'json_dict': data_dict, 'page': page_num}
        else:
            return None

    def get_data_from_post(self, data_dict, page_num, post_url=None, is_by_session=False, headers=None,
                           data_type='data', is_versify=True):
        """通过POST访问API获取数据"""
        json_dict = {}
        news_url = post_url if post_url else self.base_url

        try:
            # 尝试使用 session page 或 requests.post 两种方式获取数据
            if is_by_session:
                tab = SessionPage()
                if data_type != 'json':
                    tab.post(news_url, data=data_dict, proxies=self.proxy, headers=headers, verify=is_versify)
                else:
                    tab.post(news_url, json=data_dict, proxies=self.proxy, headers=headers, verify=is_versify)
                json_dict = tab.json if tab.json else tab.html  # 尝试获取JSON数据，优化错误处理
            else:
                response = requests.post(news_url, data=data_dict, proxies=self.proxy, headers=headers,
                                         verify=is_versify)
                json_dict = response.json()  # 直接尝试解析JSON，优化错误处理

            if page_num % 10 == 0:
                logger.info(f"当前的页数：{page_num}/{self.total_page_num}")

        except RequestException as e:
            # 处理请求错误
            logger.error(f"第{page_num}页，请求发生错误 - {e}")
            json_dict = {}

        except json.JSONDecodeError as e:
            # 处理JSON解码错误
            logger.error(f"第{page_num}页，JSON解析错误 - {e}")
            json_dict = {}

        finally:
            # 无论如何都返回数据和页码
            return {'json_dict': json_dict, 'page': page_num}

    def get_data_from_get(self, page_num, headers=None, is_versify=True):
        """ 通过get访问api获取URL"""
        json_dict = {}

        url = self.base_url.format(page_num=page_num)

        try:
            response = requests.get(url, proxies=self.proxy, headers=headers, verify=is_versify)

            # 解码内容并存储到变量中
            decoded_content = response.content.decode('utf-8')

            json_dict = json.loads(decoded_content)
            if page_num % 10 == 0:
                logger.info(f"当前的页数：{page_num}/{self.total_page_num}")
        except Exception as e:
            logger.error(f"第{page_num}页，发生错误 - {e}")
            json_dict = {}
        finally:
            return {'json_dict': json_dict, 'page': page_num}

    def get_data_from_post_xpath(self, data_dict, page_num, headers=None, is_by_session=True):
        """
        从给定的URL加载新闻列表。
        参数:
        url -- 要访问的网址。
        page_num -- 当前页码。
        frames_xpath -- 用于查找新闻框架的XPath。
        title_xpath -- 用于查找新闻标题的XPath。
        date_xpath -- 用于查找新闻日期的XPath列表。
        is_by_click -- 是否通过点击进行翻页。
        """
        news_list = []

        if is_by_session:
            tab = SessionPage()
            try:
                # 尝试使用 session page 获取数据
                tab.post(self.base_url, data=data_dict, proxies=self.proxy, headers=headers)

                # 获取元素
                frames = tab.eles(self.content_xpath['frames'])
                for frame in frames:
                    try:
                        title = frame.ele(self.content_xpath['title']).attr('title') or frame.ele(
                            self.content_xpath['title']).text
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
                            continue

                        if 'url' not in self.content_xpath or not self.content_xpath['url']:
                            title_url = frame.ele(self.content_xpath['title']).attr('data-url') or frame.ele(
                                self.content_xpath['title']).attr('href')
                        else:
                            title_url = frame.ele(self.content_xpath['url']).attr('href')
                    except Exception as e:
                        continue

                    if title and date:
                        news_dict = {'topic': title, 'date': date, 'url': title_url}

                        # 清理URL字符串
                        cleaned_dict = clean_news_data(news_dict)

                        # 检查是否符合年份的要求
                        if is_in_year(cleaned_dict['date'], self.targeted_year):
                            # 将提取的信息存储在字典中，并添加到列表
                            news_list.append(cleaned_dict)

                logger.info(
                    f"第{page_num}页 - 符合年份为{self.targeted_year}的新闻有 {len(news_list)}/{len(frames)} 条")

            except RequestException as e:
                # 处理请求错误
                logger.error(f"第{page_num}页，请求发生错误 - {e}")
                news_list = []

            except json.JSONDecodeError as e:
                # 处理JSON解码错误
                logger.error(f"第{page_num}页，JSON解析错误 - {e}")
                news_list = []

            finally:
                if page_num % 10 == 0:
                    logger.info(f"当前的页数：{page_num}页/{self.total_page_num}页")
                # 无论如何都返回数据和页码
                return news_list

    def get_data_from_get_xpath(self, page_num, headers=None, is_versify=True, is_by_requests=False, base_url=None):
        """通过Session访问HTMl页面获取数据"""
        news_list = []

        try:
            # 尝试使用 session page 获取数据
            news_url = self.base_url.format(page_num=page_num)

            if not is_by_requests:
                tab = SessionPage()
                tab.get(news_url, proxies=self.proxy, headers=headers, verify=is_versify)

                # 获取元素
                frames = tab.eles(self.content_xpath['frames'])
                for frame in frames:
                    try:
                        title = frame.ele(self.content_xpath['title']).attr('title') or frame.ele(
                            self.content_xpath['title']).text
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
                            continue

                        if 'url' not in self.content_xpath or not self.content_xpath['url']:
                            title_url = frame.ele(self.content_xpath['title']).attr('data-url') or frame.ele(
                                self.content_xpath['title']).attr('href')
                        else:
                            title_url = frame.ele(self.content_xpath['url']).attr('href')
                    except Exception:
                        continue

                    if title and date:
                        news_dict = {'topic': title, 'date': date, 'url': title_url}

                        # 清理URL字符串
                        cleaned_dict = clean_news_data(news_dict)

                        # 检查是否符合年份的要求
                        if is_in_year(cleaned_dict['date'], self.targeted_year):
                            # 将提取的信息存储在字典中，并添加到列表
                            news_list.append(cleaned_dict)
            else:
                response = requests.get(news_url, proxies=self.proxy, headers=headers, verify=is_versify)
                page_content = response.content.decode('utf-8')
                doc = html.fromstring(page_content)

                # 获取元素
                frames = doc.xpath(self.content_xpath['frames'])
                for frame in frames:
                    try:
                        title = frame.xpath(self.content_xpath['title'])[0].attrib.get('title', '') or \
                                frame.xpath(self.content_xpath['title'])[0].text_content()
                        date = None
                        for xpath in self.content_xpath['date']:
                            date_elements = frame.xpath(xpath)
                            if date_elements:
                                date = date_elements[0].text_content().strip()
                                date = format_date(date)
                                break
                        if not date:
                            continue

                        url_xpath = self.content_xpath.get('url', '')
                        title_url = frame.xpath(url_xpath or self.content_xpath['title'])[0].get('data-url', '') or \
                                    frame.xpath(url_xpath or self.content_xpath['title'])[0].get('href', '')
                    except Exception:
                        continue

                    if title and date:
                        news_dict = {'topic': title,
                                     'url': title_url if title_url.startswith(
                                         ('http://', 'https://')) else base_url + title_url,
                                     'date': date,
                                     }
                        cleaned_dict = clean_news_data(news_dict)
                        if is_in_year(cleaned_dict['date'], self.targeted_year):
                            news_list.append(cleaned_dict)
        except RequestException as e:
            # 处理请求错误
            logger.error(f"第{page_num}页，请求发生错误 - {e}")
            news_list = []

        except json.JSONDecodeError as e:
            # 处理JSON解码错误
            logger.error(f"第{page_num}页，JSON解析错误 - {e}")
            news_list = []

        finally:
            logger.info(f"第{page_num}页 - 符合年份为{self.targeted_year}的新闻有 {len(news_list)}/{len(frames)} 条")

            if page_num % 10 == 0:
                logger.info(f"当前的页数：{page_num}页/{self.total_page_num}页")
            # 无论如何都返回数据和页码
            return news_list

    def save_files(self):

        logger.success(f"{self.name} - 共爬取数据{len(self.unique_news)}条")
        # 存储在Excel中
        save_to_excel(self.unique_news, self.name, self.province)

        self.page.quit()
