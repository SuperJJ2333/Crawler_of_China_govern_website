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
    if 'result' in data:
        data_list = data['result']['records']
        # 遍历新闻列表
        for news_item in data_list:

            try:
                # 提取发布日期
                date = news_item['webdate']
                # 提取新闻标题
                title = news_item['title']
                # 提取新闻URL
                news_url = news_item['linkurl']

            except Exception as e:
                logger.warning(f"部分数据不存在：{e}")
                continue

            # 将提取的数据添加到列表中
            news_dict = {'topic': title,
                         'url': news_url if news_url.startswith(('http://', 'https://')) else base_url + news_url,
                         'date': date,
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
    URL获取方式：Session 获取post数据
    URL返回格式：json
    """

    # 爬虫基本信息
    city_info = {'name': 'Yinkou',
                 'province': 'Liaoning',
                 'total_news_num': 104,
                 'each_page_num': 10,
                 'targeted_year': 2021,
                 'base_url': 'http://www.yingkou.gov.cn/inteligentsearch/rest/inteligentSearch/getFullTextData'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    data_dict = {
        "token": "",
        "pn": 10,
        "rn": 10,
        "sdt": "2020-12-31T16:00:00.000Z",
        "edt": "2021-12-30T16:00:00.000Z",
        "wd": "考察学习",
        "inc_wd": "",
        "exc_wd": "",
        "fields": "title;content",
        "cnum": "001;002;",
        "sort": "{\"sysscore\":\"0\"}",
        "ssort": "title",
        "cl": 500,
        "terminal": "",
        "condition": None,
        "time": None,
        "highlights": "title;content",
        "statistics": None,
        "unionCondition": None,
        "accuracy": "",
        "noParticiple": "0",
        "searchRange": None
    }

    page_num_name = "pn"
    off_set = 10
    base_url = 'http://www.yingkou.gov.cn'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'

    headers = {
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Content-Length": "423",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "Cookie": "HttpOnly; HttpOnly; fontZoomState=0",
  "Host": "www.yingkou.gov.cn",
  "Origin": "http://www.yingkou.gov.cn",
  "Proxy-Connection": "keep-alive",
  "Referer": "http://www.yingkou.gov.cn/search/fullsearch.html?wd=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
  "X-Requested-With": "XMLHttpRequest"
}

    """get信息"""

    """xpath信息"""

    city_info = PageMother(city_info=city_info, is_headless=True)

    city_info.fetch_web_by_requests(request_type='post_session', cleaned_method=extract_news_info,
                                    data_dict=data_dict, page_num_name=page_num_name, data_type='json', off_set=off_set,
                                    base_url=base_url, is_begin_from_zero=True, headers=headers)