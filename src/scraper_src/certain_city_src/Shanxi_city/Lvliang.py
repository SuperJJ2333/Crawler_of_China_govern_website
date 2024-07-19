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
        data_list = data['data']['data']
        # 遍历新闻列表
        for news_item in data_list:

            try:
                # 提取发布日期
                date = news_item['docpubtime']
                # 提取新闻标题
                title = news_item['title']
                # 提取新闻URL
                news_url = news_item['docpuburl']

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
    爬虫代理
    
    URL获取方式：Session 获取post数据
    URL返回格式：json
    """

    # 爬虫基本信息
    city_info = {'name': 'Lvliang',
                 'province': 'Shanxi',
                 'total_news_num': 909,
                 'each_page_num': 10,
                 'targeted_year': 2019,
                 'base_url': 'http://www.lvliang.gov.cn/trs-search/trssearch/v2/searchAll.do?siteId=5&searchTag=all'
                             '&allKeywords=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&fullKeywords=&orKeywords=&notKeywords'
                             '=&sort=&position=0&startTime=2018-01-01&endTime=2018-12-31&organization=&pageNum={page_num}'
                             '&pageSize=10&zcYear=&isAlways=1&fileTag='
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    # 将JSON字符串转换成字典
    # data_dict = '{"code":"181936c3700","configCode":"","codes":"","searchWord":"学习考察 考察学习","historySearchWords":["学习考察 考察学习","学习考察"],"dataTypeId":"1823","orderBy":"related","searchBy":"all","appendixType":"","granularity":"CUSTOM","beginDateTime":1609430400000,"endDateTime":1640966399999,"isSearchForced":0,"filters":[],"pageNo":2,"pageSize":10}'

    # data_dict = json.loads(data_dict)

    # page_num_name = "pageNo"
    # off_set = 10
    # base_url = 'https://www.wuxi.gov.cn/search/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'
    headers = {
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Cookie": "_gscu_1275628695=15947186vx506t17; _gscbrs_1275628695=1; _trs_uv=lwamngbm_1490_9cbt; _trs_ua_s_1=lwanule8_1490_cb04",
  "Host": "www.lvliang.gov.cn",
  "Proxy-Connection": "keep-alive",
  "Referer": "http://www.lvliang.gov.cn/search-web/",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}

    """get信息"""

    """xpath信息"""
    frames_xpath = 'x:/html/body/div[5]/div[3]/div[1]/ul/li'
    title_xpath = 'x://h4/a'
    date_xpath = ['x://div[1]/text()']
    content_xpath = {'frames': frames_xpath,
                     'title': title_xpath,
                     'date': date_xpath}

    city_info = PageMother(city_info=city_info, is_headless=True,
                           thread_num=thread_num)

    city_info.fetch_web_by_requests(request_type='get',
                                    headers=headers, cleaned_method=extract_news_info)
