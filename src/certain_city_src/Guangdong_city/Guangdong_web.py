import sys
import time

import requests

from scraper.spider_mother import PageMother

from src.common.form_utils import *

# 设置日志
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss} - <level>{level}</level> - {message}</green>",
    level="INFO",
)


class GuangdongSpider:
    """广东省22个地级市的政府官网爬取“学习考察”新闻"""

    def __init__(self):
        self.province_code = {
            'Guangzhou': 200,  # 广州
            'Shenzhen': 755,  # 深圳
            'Zhuhai': 756,  # 珠海
            'Shantou': 754,  # 汕头
            'Foshan': 757,  # 佛山
            'Shaoguan': 751,  # 韶关
            'Zhanjiang': 759,  # 湛江
            'Zhaoqing': 758,  # 肇庆
            'Jiangmen': 750,  # 江门
            'Maoming': 668,  # 茂名
            'Huizhou': 752,  # 惠州
            'Meizhou': 753,  # 梅州
            'Shanwei': 660,  # 汕尾
            'Heyuan': 762,  # 河源
            'Yangjiang': 662,  # 阳江
            'Qingyuan': 763,  # 清远
            'Dongguan': 769,  # 东莞
            'Zhongshan': 760,  # 中山
            'Chaozhou': 768,  # 潮州
            'Jieyang': 663,  # 揭阳
            'Yunfu': 766  # 云浮
        }
        self.base_url = "https://search.gd.gov.cn/api/search/all"

        self.listen_target = '/api/search/all'

    def run(self):

        """
        爬虫运行方法

        return -
        """
        for index, (key, value) in enumerate(self.province_code.items()):
            if index <= 9:
                continue

            if key == "Guangzhou":
                self.year = 2015
            elif key == "Foshan":
                self.year = 2017
            else:
                self.year = 2019

            # 省份名称
            province_name = key
            self.province = key
            # 省份ID
            province_id = value

            # 省份数据
            province_data = {"page": "{page_num}", "sort": "time", "keywords": "学习考察 考察学习",
                             "time_to": int(time.time()),
                             "time_from": 189273600, "site_id": "2", "range": "city", "position": "title",
                             "service_area": f"{province_id}",
                             "recommand": 1, "gdbsDivision": "440000"}

            total_news_num = self.get_total_news_num(province_data)
            # 省份爬虫类
            province_class = PageMother(name=province_name, url=self.base_url, targeted_year=self.year,
                                        province='Guangdong', each_page_num=20, total_news_num=total_news_num,
                                        is_headless=True)
            # 需要爬取的方法
            province_class.get_web_by_post(data_dict=province_data, page_num_name="page",
                                           cleaned_method=self.extract_news_info, update_time_to=True)

    def extract_news_info(self, json_data, targeted_year, logger):
        """
        从 JSON 数据中提取新闻标题、URL 和发布日期。

        参数:
        - json_data: 包含新闻信息的 JSON 字符串

        返回:
        - news_list: 包含每条新闻的标题、URL 和发布日期的字典列表
        """

        # 将 JSON 字符串解析为 Python 字典
        data = json_data

        # 初始化一个列表来存储新闻信息
        news_list = []

        # 检查 JSON 数据结构中是否存在所需的路径和数据
        if 'data' in data and 'news' in data['data'] and 'list' in data['data']['news']:
            # 遍历新闻列表
            for news_item in data['data']['news']['list']:
                # 提取所需的信息
                title = news_item.get('title', '')  # 若无标题，默认值
                url = news_item.get('url', '')  # 若无 URL，默认值
                publish_date = news_item.get('pub_time', '')  # 若无发布日期，默认值

                news_dict = {
                    'topic': title,
                    'url': url,
                    'date': publish_date
                }
                # 清理URL字符串
                cleaned_dict = clean_news_data(news_dict)

                if is_in_year(cleaned_dict['date'], targeted_year):
                    # 将提取的信息存储在字典中，并添加到列表
                    news_list.append(cleaned_dict)
                    logger.info(
                        f"{self.province} - {cleaned_dict['topic']} 日期为：{cleaned_dict['date']} 年份属于 {targeted_year}")
                else:
                    logger.debug(
                        f"{self.province} - {cleaned_dict['topic']} 日期为：{cleaned_dict['date']} 不属于 {targeted_year}")

        # 返回结果列表
        return news_list

    def get_total_news_num(self, data_dict):
        url = 'https://search.gd.gov.cn/api/search/all'
        data_dict['page'] = 1
        req = requests.post(url=url, data=data_dict)

        # # 解码内容并存储到变量中
        decoded_content = req.content.decode('utf-8')

        # # 打印解码后的内容
        json_dict = json.loads(decoded_content)
        total_page_num = json_dict['data']['news']['total']

        return int(total_page_num)


if __name__ == '__main__':
    Test = GuangdongSpider()
    Test.run()
