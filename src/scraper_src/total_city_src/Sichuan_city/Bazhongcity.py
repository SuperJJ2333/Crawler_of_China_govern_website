from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '巴中市',
        'province_name': '四川省',
        'province': 'Sichuan',

        'base_url': 'https://www.cnbz.gov.cn/site/tpl/6780041?isAllSite=true&platformCode=&siteId=&columnId=&columnIds=&typeCode=&beginDate=&endDate=&fromCode=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&oldKeywords=&subkeywords=&excColumns=&datecode=&sort=intelligent&type=&tableColumnId=&indexNum=&fileNum=&pid=&flag=false&orderType=0&pageIndex={page_num}&pageSize=10',

        'total_news_num': 2328,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="search_hasreslut"]/div[2]/div[2]/div[1]/div[2]/ul',
                     'title': 'x://li/a',
                     'date': ['x://li[2]/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"SHIROJSESSIONID=25d1ecc0-37f8-4222-98fe-ff07f040e528; wzaConfigTime=1720175132312","Host":"www.cnbz.gov.cn","Referer":"https://www.cnbz.gov.cn/site/tpl/6780041?keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&typeCode=&orderType=&sort=intelligent&isAllSite=true&fromCode=title","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888',
                       'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()