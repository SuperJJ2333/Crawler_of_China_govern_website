from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '德阳市',
        'province_name': '四川省',
        'province': 'Sichuan',
        'base_url': 'https://www.deyang.gov.cn/search/searchNew.jsp?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=&t_id=54&type=&class=0&p={page_num}',

        'total_news_num': 5872,

        'each_page_news_num': 20,
    }

    content_xpath = {'frames': 'x://*[@class="item"]',
                     'title': 'x://h1/a',
                     }

    fiddler_proxy = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"Hm_lvt_166c5db85e2d74ff79c194031065bc78=1720156460,1721146813; HMACCOUNT=A202F23FD4E0D795; Hm_lvt_a43483b93d2eb6101d516c816c057645=1720156461,1721146813; JSESSIONID=3DFDC2124E7966A8D60970E67F990847; Hm_lpvt_a43483b93d2eb6101d516c816c057645=1721147111; Hm_lpvt_166c5db85e2d74ff79c194031065bc78=1721147111","Host":"www.deyang.gov.cn","Referer":"https://www.deyang.gov.cn/search/searchNew.jsp?type=cms&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&t_id=54&class=0","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}
    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxy, verify=False, thread_num=5)
    scraper.run()