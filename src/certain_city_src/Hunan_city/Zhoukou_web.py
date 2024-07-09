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
    if 'rows' in data:
        data_list = data['rows']
        # 遍历新闻列表
        for news_item in data_list:

            try:

                title = news_item['articleTitle']
                news_url = news_item['articleUri']
                date = news_item['articlePublishTime']

            except Exception as e:
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
    URL获取方式：api post访问
    URL返回格式：HTMl字典
    """

    # 爬虫基本信息
    city_info = {'name': 'Zhoukou',
                 'province': 'Henan',
                 'total_news_num': 823,
                 'each_page_num': 10,
                 'targeted_year': 2018,
                 'base_url': 'https://www.zhoukou.gov.cn/search/SolrSearch/searchData'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    data_dict = {'q': '学习考察 考察学习', 'forCatalogType': '0',
                 'token4': 'a62697497d1643e8810f115bab011ffc',
                 'siteId': '9752499e88b94e1881e46bbeeef1376e', 'offset': '0', 'limit': '10'}

    page_num_name = 'offset'
    off_set = 10
    base_url = 'https://www.zhoukou.gov.cn'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'

    headers = {
  "Accept": "*/*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "Cookie": "wzafullscreen=0; shiro.sesssion=a1995907-6652-4e5e-a9db-61d2afff8fae",
  "Host": "www.zhoukou.gov.cn",
  "Origin": "https://www.zhoukou.gov.cn",
  "Referer": "https://www.zhoukou.gov.cn/search/SolrSearch/s",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
  "sec-ch-ua": "\"Microsoft Edge\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\""
}

    city_info = PageMother(city_info=city_info, is_headless=True)

    city_info.fetch_web_by_requests(request_type='post_session', data_dict=data_dict, off_set=off_set,
                                    page_num_name=page_num_name, data_type='data', headers=headers,
                                    cleaned_method=extract_news_info, base_url=base_url, is_begin_from_zero=True, )
