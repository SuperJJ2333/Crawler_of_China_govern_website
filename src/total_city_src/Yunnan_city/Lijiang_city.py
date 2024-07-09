from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '丽江市',
        'province_name': '云南省',
        'province': 'Yunnan',

        'base_url': 'https://www.lijiang.gov.cn/search4/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&column=%25E5%2585%25A8%25E9%2583%25A8&pageSize=10&pageNum=0&siteCode=5307000001&sonSiteCode=&checkHandle=1&searchSource=0&areaSearchFlag=0&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex=&isSecondSearch=undefined&manualWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=0',


        'total_news_num': 6,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[2]/div/div[1]/div',
                     'title': 'x://div/a',
                     'date': ['x://p[2]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Connection":"keep-alive","Cookie":"proName=search4/; firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; userSearch=siteCode-5307000001&column-%E5%85%A8%E9%83%A8&uc-1&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240705225003&searchUseTime-256; SECKEY_ABVK=dXJHfrf9KF5oT+Q40vG1nNn2onVYt8Y64V+inMzbURU%3D; proName=search4/; firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; userSearch=siteCode-5307000001&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240705225015&searchUseTime-171; SECKEY_ABVK=dXJHfrf9KF5oT+Q40vG1nNaK2OZWDfIPOW/29OVBRdw%3D; _yfxkpy_ssid_10009046=%7B%22_yfxkpy_firsttime%22%3A%221720190714097%22%2C%22_yfxkpy_lasttime%22%3A%221720190714097%22%2C%22_yfxkpy_visittime%22%3A%221720190714097%22%2C%22_yfxkpy_cookie%22%3A%2220240705224514100437748333926335%22%7D; Hm_lvt_4f631e6f858486f56e16dda003fd2de8=1720190714; Hm_lpvt_4f631e6f858486f56e16dda003fd2de8=1720190714; HMACCOUNT=A202F23FD4E0D795; Hm_lvt_63e945f7620482cf0e34c24501c01752=1720190715; Hm_lpvt_63e945f7620482cf0e34c24501c01752=1720190715; arialoadData=false; 5307000001=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oA==; JSESSIONID=5931E2174B9E280BA2792C1B29376972","Host":"www.lijiang.gov.cn","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()