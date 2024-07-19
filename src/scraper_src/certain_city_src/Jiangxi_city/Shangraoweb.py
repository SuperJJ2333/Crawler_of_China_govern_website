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
    city_info = {'name': 'Shangrao',
                 'province': 'Jiangxi',
                 'total_news_num': 168,
                 'each_page_num': 10,
                 'targeted_year': 2019,
                 'base_url': 'https://zs.kaipuyun.cn/search4/s?searchWord=%25E8%2580%2583%25E5%25AF%259F%25E5%25AD'
                             '%25A6%25E4%25B9%25A0&column=%25E5%2585%25A8%25E9%2583%25A8&pageSize=10&pageNum={page_num}'
                             '&siteCode=3611000001&sonSiteCode=&checkHandle=1&searchSource=0&areaSearchFlag=0'
                             '&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0'
                             '&searchBoxSettingsIndex=&isSecondSearch=undefined&manualWord=%25E8%2580%2583%25E5%25AF'
                             '%259F%25E5%25AD%25A6%25E4%25B9%25A0&orderBy=0&startTime=2018-01-01%2000:00:00&endTime'
                             '=2018-12-31%2023:59:59&timeStamp=5&strFileType=&wordPlace=0'
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
    headers ={
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Cookie": "proName=search4/; firstWord=%u5B66%u4E60%u8003%u5BDF; userSearch=siteCode-3611000001&column-%E5%85%A8%E9%83%A8&uc-1&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&searchTime-20240521112513&searchUseTime-70; SECKEY_ABVK=TXuIX6p6HNd6ayGiHg9HgI6ldeWjn3o3pYGvESOkF8c%3D; BMAP_SECKEY=Z1ROGlRy-zdYROkyYNTEapwAHg4TCeyI2m_LKZfEtOLRORScV8vd3bH_kjOnchQ4NdXmPJcWWGy7TJlHv1qOlfZ0Ig8BoWy0YQDpslSNR50N56PasnrWRx3SjSVfXJcuuEyhgwRcOMAUQdkqtOlw53dYchjh3kYrQgA7nbALrvRgNAZxDYFoqQQzDZUtoN2e; proName=search4/; firstWord=%u5B66%u4E60%u8003%u5BDF; userSearch=siteCode-3611000001&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&searchWord-%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240521112547&searchUseTime-528; SECKEY_ABVK=TXuIX6p6HNd6ayGiHg9HgPupSCXDQbrd6F3OkwfyrBQ%3D; BMAP_SECKEY=Z1ROGlRy-zdYROkyYNTEanx3mpgWhn-N1xHmO7l8GBaGJd9P5IuAH3caXr_E_qy1GQOaSI7ZYNJNmcATW3ZMixJBF4is0wEs-y714RCQFDZ2nVt2kNJVyI3ISIJGsKJ7blSSv_5c8ubOaFa_lVZffElVstkVowIZOHLzIy8Lwi4u-Z4Epcy3yyxwprcpmN3D; HWWAFSESID=5d52d735252931f515; HWWAFSESTIME=1716213073175; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; firstWord=%u5B66%u4E60%u8003%u5BDF; 3607000056=5a2m5Lmg6ICD5a+fLOiAg+Wvn+WtpuS5oCzlrabkuaDogIPlr58g6ICD5a+f5a2m5Lmg; userSearch=siteCode-3607000056&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&searchTime-20240520220114&searchUseTime-525; SECKEY_ABVK=TXuIX6p6HNd6ayGiHg9HgLhk+B+qs42m3bdsof1ptcU%3D; BMAP_SECKEY=Z1ROGlRy-zdYROkyYNTEarMqiy5s1JmS0DSTc7CL5W70czld19ooZSNiGHYfWw_JscGm1RKdYMnYxBhWhvu81tkn8myzqAQjUc4haPIxmxTiDlOITmk0cY9uAsnXGX51RA63vHMSFBxI07GaBboDR6ztMkP9TREBMGBeBt0huEmsvFrUDdovmCgr2g8AuqgC; 3611000001=6ICD5a+f5a2m5LmgLOWtpuS5oOiAg+WvnyDogIPlr5/lrabkuaAs5a2m5Lmg6ICD5a+f; JSESSIONID=71FBA324B37CBE768EDCC5A13643676B",
  "Host": "zs.kaipuyun.cn",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-User": "?1",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
  "sec-ch-ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\""
}

    """get信息"""

    """xpath信息"""
    frames_xpath = 'x://body/div[2]/div/div[1]/div'
    title_xpath = 'x://div[1]/a'
    date_xpath = ['x://div[2]/div/p[2]/span', "x://p/span"]
    content_xpath = {'frames': frames_xpath,
                     'title': title_xpath,
                     'date': date_xpath}

    city_info = PageMother(city_info=city_info, is_headless=True, content_xpath=content_xpath,
                           thread_num=thread_num, proxies=proxies)

    city_info.fetch_web_by_requests(request_type='get_xpath',
                                    headers=headers, is_begin_from_zero=True, is_versify=False,)
