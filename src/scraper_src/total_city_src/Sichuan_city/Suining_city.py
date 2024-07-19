from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '遂宁市',
        'province_name': '四川省',
        'province': 'Sichuan',
        'base_url': 'https://www.suining.gov.cn/search.html?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&page={page_num}',

        'total_news_num': 500,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://section[4]/div',
                     'title': 'x://a',
                     'date': ['x://div[2]/text()'],
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"__jsluid_s=5ec85c44241a179cfbe3cc750d1c8e77; Hm_lvt_04894bddc914b5373a794a477b8a29c5=1719130939,1720160432,1721191035; HMACCOUNT=A202F23FD4E0D795; JSESSIONID=F44872CFD6F5DC4C68FA873BB9A50776; Hm_lpvt_04894bddc914b5373a794a477b8a29c5=1721191118","Host":"www.suining.gov.cn","Referer":"https://www.suining.gov.cn/search.html?t=&ot=&content=1&dt=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}
    fiddler_proxies = {'http': 'http://127.0.0.1:8888',
                       'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False, thread_num=2)
    scraper.run()