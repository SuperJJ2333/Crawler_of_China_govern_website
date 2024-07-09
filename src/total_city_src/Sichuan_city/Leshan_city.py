from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '乐山市',
        'province_name': '四川省',
        'province': 'Sichuan',
        'base_url': 'https://www.leshan.gov.cn/ls/s?qt=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteCode=5111000002&database=%5Bobject%20HTMLInputElement%5D&isNullSession=true&sort=relevance&ot=timedesc&page={page_num}',

        'total_news_num': 1282,

        'each_page_news_num': 20,
    }

    content_xpath = {'frames': 'x:/html/body/div[1]/div[2]/div[3]/ul/li',
                     'title': 'x://h1/a',
                     'date': ['x://h2/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"Hm_lvt_5fda478391278e1a06bc820b9b3020e6=1720160445; Hm_lpvt_5fda478391278e1a06bc820b9b3020e6=1720160445; HMACCOUNT=A202F23FD4E0D795; JSESSIONID=6A834B26BE027E07FB9C299A73457EDF","Host":"www.leshan.gov.cn","Referer":"https://www.leshan.gov.cn/ls/s?qt=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteCode=5111000002&database=%5Bobject%20HTMLInputElement%5D&isNullSession=true&sort=relevance&ot=timedesc&page=2","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888',
                       'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()