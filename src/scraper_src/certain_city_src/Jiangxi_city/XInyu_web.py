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
    爬虫代理
    
    URL获取方式：Session 获取post数据
    URL返回格式：json
    """

    # 爬虫基本信息
    city_info = {'name': 'Xinyu',
                 'province': 'Jiangxi',
                 'total_news_num': 18,
                 'each_page_num': 10,
                 'targeted_year': 2022,
                 'base_url': 'http://www.xinyu.gov.cn/search4/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580'
                             '%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0'
                             '&column=%25E5%2585%25A8%25E9%2583%25A8&pageSize=10&pageNum={page_num}&siteCode=3605000002'
                             '&sonSiteCode=&checkHandle=1&searchSource=0&areaSearchFlag=0&secondSearchWords=&topical'
                             '=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex'
                             '=&isSecondSearch=undefined&manualWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583'
                             '%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0'
                             '&orderBy=0&startTime=2021-01-01%2000:00:00&endTime=2021-12-31%2023:59:59&timeStamp=5'
                             '&strFileType=&wordPlace=1'
                 }
    # 可选参数
    thread_num = 5

    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888"
    }

    """post信息"""
    # 将JSON字符串转换成字典
    # data_dict = '{"code":"181936c3700","configCode":"","codes":"","searchWord":"学习考察 考察学习","historySearchWords":["学习考察 考察学习","学习考察"],"dataTypeId":"1823","orderBy":"related","searchBy":"all","appendixType":"","granularity":"CUSTOM","beginDateTime":1609430400000,"endDateTime":1640966399999,"isSearchForced":0,"filters":[],"pageNo":2,"pageSize":10}'

    # data_dict = json.loads(data_dict)

    # page_num_name = "pageNo"
    # off_set = 10
    # base_url = 'https://www.wuxi.gov.cn/search/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "proName=search4/; firstWord=%u5B66%u4E60%u8003%u5BDF; SECKEY_ABVK=TXuIX6p6HNd6ayGiHg9HgARe+HClyHiIuD+gVDICCeA%3D; userSearch=siteCode-3605000002&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240520145616&searchUseTime-491; SESSION_WEB_CACHE_KEY=efa1b79178c449eea12a3869e076b595; _yfxkpy_ssid_10008935=%7B%22_yfxkpy_firsttime%22%3A%221716188123470%22%2C%22_yfxkpy_lasttime%22%3A%221716188123470%22%2C%22_yfxkpy_visittime%22%3A%221716188123470%22%2C%22_yfxkpy_domidgroup%22%3A%221716188123470%22%2C%22_yfxkpy_domallsize%22%3A%22100%22%2C%22_yfxkpy_cookie%22%3A%2220240520145523480456865936459899%22%7D; Hm_lvt_51710e264808f8ef475cc8f492e3f3bb=1716188124; Hm_lpvt_51710e264808f8ef475cc8f492e3f3bb=1716188124; arialoadData=true; ariawapChangeViewPort=true; HWWAFSESID=28f4776b10faabfa81; HWWAFSESTIME=1716188128853; 3605000002=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oCzlrabkuaDogIPlr58=; JSESSIONID=ECF3F4E91512661111D03D1185FCB87B",
        "Host": "www.xinyu.gov.cn",
        "Proxy-Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
    }

    """get信息"""

    """xpath信息"""
    frames_xpath = 'x://body/div[2]/div/div[3]/div'
    title_xpath = 'x://div[1]/a'
    date_xpath = ['x://div[2]/div/p[2]/span']
    content_xpath = {'frames': frames_xpath,
                     'title': title_xpath,
                     'date': date_xpath}

    city_info = PageMother(city_info=city_info, is_headless=True, content_xpath=content_xpath,
                           thread_num=thread_num, proxies=proxies)

    city_info.fetch_web_by_requests(request_type='get_xpath',
                                    headers=headers, is_begin_from_zero=True, is_versify=False,)
