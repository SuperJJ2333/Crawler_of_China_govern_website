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
        data_list = data['data']['middle']['listAndBox']
        # 遍历新闻列表
        for news_item in data_list:

            try:
                news_item = news_item['data']
                # 提取发布日期
                date = news_item['time']
                # 提取新闻标题
                title = news_item['title_no_tag']
                # 提取新闻URL
                news_url = news_item['url']

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
    city_info = {'name': 'Guigan',
                 'province': 'Guangxi',
                 'total_news_num': 87,
                 'each_page_num': 10,
                 'targeted_year': 2019,
                 'base_url': 'http://www.gxgg.gov.cn/irs/front/search'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    data_dict = {"code": "181aedaa74b", "dataTypeId": "5723", "configCode": "", "searchWord": "考察学习",
                 "orderBy": "related", "searchBy": "all", "appendixType": "", "granularity": "ALL",
                 "beginDateTime": 1514736000000, "endDateTime": 1546185600000, "isSearchForced": "0", "filters": [],
                 "pageNo": 1, "pageSize": 10,
                 "historySearchWords": ["考察学习", "考察学习 学习考察", "学习考察 考察学习", "学习考察"]}
    page_num_name = "pageNo"
    # off_set = 5
    # base_url = 'https://www.gswuwei.gov.cn/jsearchfront/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'
    """get信息"""

    city_info = PageMother(city_info=city_info, is_headless=True)

    city_info.fetch_web_by_requests(request_type='post_session', cleaned_method=extract_news_info,
                                    data_dict=data_dict, page_num_name=page_num_name, data_type='json', )
