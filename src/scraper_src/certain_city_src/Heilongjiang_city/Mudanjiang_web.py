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
    if 'searchResultAll' in data:
        data_list = data['searchResultAll']['searchTotal']
        # 遍历新闻列表
        for news_item in data_list:

            try:
                # 提取发布日期
                date = news_item['pubDate']
                # 提取新闻标题
                title = news_item['title']
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
    city_info = {'name': 'Mudanjiang',
                 'province': 'Heilongjiang',
                 'total_news_num': 46,
                 'each_page_num': 10,
                 'targeted_year': 2020,
                 'base_url': 'https://www.mdj.gov.cn/search5/search/s'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888"
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "JSESSIONID=96698DCCFF35EB9C48002ACBC4B2A198; arialoadData=false; slb-route=3385c4ac18ca471d5a195048a601b27c; 2310000002=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oCzogIPlr5/lrabkuaAs5a2m5Lmg6ICD5a+f",
        "Host": "www.mdj.gov.cn",
        "Origin": "https://www.mdj.gov.cn",
        "Referer": "https://www.mdj.gov.cn/search5/html/searchResult_mudanjiang.html?siteCode=2310000002&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }

    data_dict = {'searchWord': '%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0',
                 'siteCode': '2310000002', 'column': '%E5%85%A8%E9%83%A8', 'pageSize': '10',
                 'pageNum': '2', 'checkHandle': '1', 'searchSource': '0', 'areaSearchFlag': '0',
                 'countKey': '0', 'uc': '0', 'left_right_index=': '0', 'orderBy': '1',
                 'timeStamp': '0', 'wordPlace': '1'}

    page_num_name = "pageNum"
    # off_set = 5
    # base_url = 'https://www.gswuwei.gov.cn/jsearchfront/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'

    """get信息"""
    city_info = PageMother(city_info=city_info, is_headless=True, proxies=proxies)

    city_info.fetch_web_by_requests(request_type='post', cleaned_method=extract_news_info,
                                    data_dict=data_dict, page_num_name=page_num_name, data_type='data', headers=headers,
                                    is_versify=False)
