from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_code': 308,
        'city_name': '阿坝藏族羌族自治州',
        'province_name': '四川省',
        'province': '四川省',
        'base_url': 'https://abazhou.gov.cn/search4/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F&column=%25E5%2585%25A8%25E9%2583%25A8&pageSize=10&pageNum={page_num}&siteCode=5132000003&sonSiteCode=&checkHandle=1&searchSource=0&areaSearchFlag=0&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex=&isSecondSearch=undefined&manualWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=0',
        'total_news_num': 867,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://div[@class="wordGuide Residence-permit"]',
                     'title': 'x://div[1]/a',
                     'date': ['xpath://div[2]/div/p[2]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; proName=search4/; userSearch=siteCode-5132000003&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&searchTime-20241101223012&searchUseTime-278; yfx_c_g_u_id_10000067=_ck24110122295012133719651578994; yfx_f_l_v_t_10000067=f_t_1730471390210__r_t_1730471390210__v_t_1730471390210__r_c_0; 5132000003=5a2m5Lmg6ICD5a+fLOWtpuS5oOiAg+WvnyDogIPlr5/lrabkuaA=; JSESSIONID=68D574E1807BD447D81EA931A1E19B8E","Host":"abazhou.gov.cn","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}
    
    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()