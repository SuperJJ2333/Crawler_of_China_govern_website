from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '海南省',
        'province_name': '海南省',
        'province': 'province_web_data',
        'base_url': 'https://www.hainan.gov.cn/s?siteCode=4600000001&searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&column=2675&wordPlace=1&orderBy=4&startTime=&endTime=&isSecondSearch=undefined&pageSize=10&pageNum={page_num}&timeStamp=0&labelHN=&uc=0&checkHandle=1&strFileType=0&countKey=%200&sonSiteCode=&areaSearchFlag=&secondSearchWords=&left_right_flag=1',

        'total_news_num': 103,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[1]/div[2]/div/div[1]/div/div',
                     'title': 'x://h3/a',
                     'date': ['x://span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"firstWord=%u5B66%u4E60%u8003%u5BDF; _trs_uv=ly2yv92a_4549_cjp3; user_id=0.3505415515459631; HttpOnly=true; HA_STICKY_web=web.srv26; HA_STICKY_apps=apps.srv35; Hm_lvt_b23dcf9fcb01d857002fb0a0edee33b3=1719837542,1720537071; Hm_lpvt_b23dcf9fcb01d857002fb0a0edee33b3=1720537071; HMACCOUNT=A202F23FD4E0D795; _trs_ua_s_1=lyejcldx_4549_ay30; _yfxkpy_ssid_10005682=%7B%22_yfxkpy_firsttime%22%3A%221719837543345%22%2C%22_yfxkpy_lasttime%22%3A%221720537072616%22%2C%22_yfxkpy_visittime%22%3A%221720537072616%22%2C%22_yfxkpy_domidgroup%22%3A%221719837543345%22%2C%22_yfxkpy_domallsize%22%3A%22100%22%2C%22_yfxkpy_cookie%22%3A%2220240701203903348418616874937682%22%2C%22_yfxkpy_returncount%22%3A%221%22%7D; arialoadData=true; 4600000001=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oA==; JSESSIONID=2C289A985C05DE56E00FDF00A3632F6A; firstWord=%u5B66%u4E60%u8003%u5BDF; userSearch=siteCode-4600000001&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240709230952&searchUseTime-353","Host":"www.hainan.gov.cn","Referer":"https://www.hainan.gov.cn/s?siteCode=4600000001&searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&column=2675&wordPlace=1&orderBy=4&startTime=&endTime=&isSecondSearch=undefined&pageSize=10&pageNum=2&timeStamp=0&labelHN=&uc=0&checkHandle=1&strFileType=0&countKey=%200&sonSiteCode=&areaSearchFlag=&secondSearchWords=&left_right_flag=1","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()