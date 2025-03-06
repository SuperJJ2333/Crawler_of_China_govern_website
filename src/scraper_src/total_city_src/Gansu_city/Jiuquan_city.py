from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '酒泉市',
        'province_name': '甘肃省',
        'province': '安徽省',
        'base_url': 'https://www.jiuquan.gov.cn/guestweb4/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%25E4%25BA%25A4%25E6%25B5%2581%25E5%25AD%25A6%25E4%25B9%25A0&column=%25E5%2585%25A8%25E9%2583%25A8&pageSize=10&pageNum={page_num}&siteCode=6209000004&sonSiteCode=&checkHandle=1&searchSource=0&govWorkBean=%257B%257D&sonSiteCode=&areaSearchFlag=-1&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex=&manualWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E4%25BA%25A4%25E6%25B5%2581%25E5%25AD%25A6%25E4%25B9%25A0&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=0',
        'total_news_num': 366,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@class="wordGuide Residence-permit"]',
                     'title': 'x://div[1]/a',
                     'date': ['x:/div[2]/div/p[2]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=3D246049BEA5C1E64811BC3EDB2AA097; firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; userSearch=siteCode-6209000004&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240701171844&searchUseTime-444; yfx_c_g_u_id_10000001=_ck24070117205612815334893456584; yfx_f_l_v_t_10000001=f_t_1719825656196__r_t_1719825656196__v_t_1719825656196__r_c_0; 6209000004=5a2m5Lmg6ICD5a+f6ICD5a+f5a2m5LmgLOWtpuS5oOiAg+WvnyzlrabkuaDogIPlr58g6ICD5a+f5a2m5Lmg","Host":"www.jiuquan.gov.cn","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      page_num_start=0)
    scraper.run()