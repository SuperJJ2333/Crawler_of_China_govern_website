import json
from datetime import datetime

from bs4 import BeautifulSoup

from common.form_utils import clean_news_data, is_in_year
from scraper.spider_mother import PageMother


def extract_news_info(json_data, year, page_num, logger, base_url=None):
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
    if 'data' in data:
        data_list = data['data']['resultDocs']
        # 遍历新闻列表
        for news_item in data_list:
            title = news_item['subject']
            date = datetime.fromtimestamp(news_item['createdate'] / 1000).strftime('%Y-%m-%d')
            news_url = f"http://www.heze.gov.cn/0530/{news_item['dwid'][0]}/{news_item['xxid']}.html"

            details = news_item['html']
            soup = BeautifulSoup(details, 'html.parser')
            text = soup.get_text()
            # 去除多余的空白字符
            cleaned_text = ' '.join(text.split())

            # 将提取的数据添加到列表中
            news_dict = {'topic': title,
                         'url': news_url,
                         'date': date,
                         'content': cleaned_text
                         }
            # 清理URL字符串
            cleaned_dict = clean_news_data(news_dict)

            # 检查是否符合年份的要求
            if is_in_year(cleaned_dict['date'], year):
                # 将提取的信息存储在字典中，并添加到列表
                news_list.append(cleaned_dict)
                # logger.info(f"{cleaned_dict['topic']} 日期为：{cleaned_dict['date']} 年份属于 {year}")
            else:
                pass
                # logger.warning(f"{cleaned_dict['topic']} 日期为：{cleaned_dict['date']} 不属于 {year}")
        logger.info(f"第{page_num}页 - 符合年份为{year}的新闻有 {len(news_list)}/{len(data_list)} 条")
    else:
        # pass
        logger.warning(f"第{page_num}页 - Json格式设置得有问题，请重新设置")

    # 返回结果列表
    return news_list


if __name__ == '__main__':
    """
    URL获取方式：api post访问
    URL返回格式：json字典
    """

    # 爬虫基本信息
    city_info = {'name': 'Hezhe',
                 'province': 'Shandong',
                 'total_news_num': 2109,
                 'each_page_num': 10,
                 'targeted_year': 2020,
                 'base_url': 'http://www.heze.gov.cn/els-service/search/new'
                 }
    thread_num = 5
    """post信息"""
    data_dict = '{"dq":"0530","fwzt":3,"highlight":"1","isSearch":"1","type":[1,2,3],"tab":"all","starttime":"2019-01-01","endtime":"2019-12-31","txtmemo":"考察学习"}'
    data_dict = json.loads(data_dict)

    off_set = 5
    page_num_name = None
    base_url = 'http://www.taian.gov.cn/jsearchfront/'
    change_url = 'http://www.heze.gov.cn/els-service/search/new/'
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "www.heze.gov.cn",
        "Origin": "http://www.heze.gov.cn",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://www.heze.gov.cn/jiansuo/?keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
    }

    city_info = PageMother(city_info=city_info, is_headless=True, thread_num=thread_num)

    city_info.fetch_web_by_requests(request_type='post_session', data_dict=data_dict, headers=headers,
                                    cleaned_method=extract_news_info, base_url=base_url,
                                    change_url=change_url, data_type='json')
