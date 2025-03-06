import csv
import math
import sys
import threading
from DrissionPage import ChromiumPage, ChromiumOptions, SessionPage
import urllib3
from loguru import logger

from src.common.content_utils import *
from src.common.form_utils import *

# # 禁用 InsecureRequestWarning
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger.remove()

# 为 INFO 级别设置格式
logger.add(
    sys.stderr,
    format="<bold><white>{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}</white></bold>",
    level="INFO",
    filter=lambda record: record["level"].name == "INFO"
)

# 为 WARNING 级别设置格式
logger.add(
    sys.stderr,
    format="<blue>{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}</blue>",
    level="WARNING",
    filter=lambda record: record["level"].name == "WARNING"
)

# 为 ERROR 级别设置格式
logger.add(
    sys.stderr,
    format="<red>{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}</red>",
    level="ERROR",
    filter=lambda record: record["level"].name == "ERROR"
)

# 添加一个默认处理器来捕获所有其他级别的日志
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}</green>",
    level="SUCCESS",
    # level="DEBUG",
    filter=lambda record: record["level"].name not in ["INFO", "WARNING", "ERROR"]
)

# 禁用 InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def read_region_code_csv():
    """读取城市编码表"""
    # 获取当前文件的目录（假设此脚本位于src/utils文件夹中）
    current_dir = os.path.dirname(__file__)

    # 打开指定路径的CSV文件，采用'gbk'编码方式读取
    with open(os.path.join(current_dir, '../../docs/region_code.csv'), mode='r', encoding='gbk') as file:
        reader = csv.DictReader(file)
        return list(reader)


def match_city_code(city_info, region_data_list):
    """匹配城市名称与编码"""
    # 获取城市名称和编码的最短长度，以防止匹配出错
    min_length = min(len(city_info['city_name']), len(region_data_list[0]['城市']))

    # 获取城市名称的前min_length个字符
    city_name_short = city_info['city_name'][:min_length]

    # 遍历region_data_list，查找匹配的城市名称
    for region_data in region_data_list:
        # 如果城市名称的前min_length个字符匹配
        if city_name_short == region_data['城市'][:min_length]:
            # 如果匹配成功，则赋值region_data的编码
            return region_data['编码']

    # 如果没有找到匹配的城市，赋值为city_info中的city_code
    return city_info['city_code']


class PageMother:
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

    def __init__(self, city_info: dict, content_xpath: dict = None, is_headless=True,
                 thread_num: int = 5, proxies: dict = None):
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
        self.city_code = self.initialize_city_code(self, city_info)
        self.city_name = city_info['city_name']
        self.province_name = city_info['province_name']
        self.base_url = city_info['base_url']
        # self.targeted_year = city_info['targeted_year'] - 1
        self.province = city_info['province']
        self.total_news_num = city_info['total_news_num']
        self.each_page_news_num = city_info['each_page_news_num']
        # 计算总页数
        # self.total_page_num = self.count_page_num()
        self.total_page_num = self.add_extra_page_num()
        # 日志
        self.logger = logger

        # 选用参数
        self.content_xpath = content_xpath or {}
        self.is_headless = is_headless
        self.thread_num = thread_num
        self.proxies = proxies if proxies is not None else {"http": None, "https": None}
        self.fiddler_proxy = {"http": "http://127.0.0.1:8888", "https": "https://127.0.0.1:8888"}

        # 存储新闻数据
        self.total_news_data = []
        # 存储去重后的新闻数据
        self.unique_news = set()
        # 多线程程序锁
        self.lock = threading.Lock()

        # 初始化浏览器
        self.start_page()

    def start_page(self):
        """根据是否为无头模式初始化浏览器页面。"""
        options = ChromiumOptions()
        # 设置每次打开的浏览器
        options.auto_port()
        # options.set_argument('--ignore-certificate-errors')
        options.set_argument("--blink-settings=imagesEnabled=false")
        # 设置浏览器代理
        options.set_proxy('')
        # 无头模式
        if self.is_headless:
            options.headless()
        # 是否需要模拟请求
        self.page = ChromiumPage(options)

        self.session = SessionPage()

        self.logger.info(f"{self.city_name} - 新闻数量为{self.total_news_num}条 - "
                         f"页数有{self.total_page_num}页 - 爬虫最大进程数为{self.thread_num}")

    def save_files(self):
        """保存数据到文件。"""
        self.logger.success(f"{self.city_name} - 共爬取数据{len(self.total_news_data)}/{self.total_news_num}条")

        self.page.quit()
        self.session.close()

        # 处理数据
        self.process_dataframes()

        if self.total_news_data:
            save_to_excel(self.total_news_data, self.city_name, self.province_name)


    def count_page_num(self):
        """获取总页数。"""
        if self.total_news_num <= 0:
            total_page_num = 0
        else:
            total_page_num = math.ceil(self.total_news_num / self.each_page_news_num)
        return total_page_num

    def add_extra_page_num(self):
        """增加额外的页数。"""
        page_num = self.count_page_num()
        return page_num + page_num // 10

    def process_dataframes(self):
        # 移除数据不完整或者'content'键不存在或为空的新闻数据
        self.total_news_data = [data for data in self.total_news_data if len(data['content']) >= 2
                                or len(data['content'][0]) > 60]

        best_data = {}
        for data in self.total_news_data:
            # 合并 content 列表中的所有文本
            full_content = ' '.join(data['content'])  # 将列表转换为单个字符串
            first_30_chars = full_content[:300]  # 提取前300个字符

            # 使用前30个字符作为字典键来筛选和存储最优数据
            if first_30_chars in best_data:
                # 如果已有相同的前30字符，则比较全文长度，保留更长的那个
                if len(full_content) > len(' '.join(best_data[first_30_chars]['content'])):
                    best_data[first_30_chars] = data
            else:
                best_data[first_30_chars] = data

        # 更新self.total_news_data为最优数据集
        self.total_news_data = list(best_data.values())
        self.logger.success(f"{self.city_name} - 清洗后数据为{len(self.total_news_data)}/{self.total_news_num}条")

    @staticmethod
    def initialize_city_code(self, city_info):
        """
        初始化城市编码
        :param self:
        :param city_info:
        :return:
        """
        # 读取城市编码表
        region_data_list = read_region_code_csv()

        # 调用函数进行匹配
        city_code = match_city_code(city_info, region_data_list)

        return city_code

