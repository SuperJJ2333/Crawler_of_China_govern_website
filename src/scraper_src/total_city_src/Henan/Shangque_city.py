from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '商丘市',
        'province_name': '河南省',
        'province': 'Henan',

        'base_url': 'https://www.shangqiu.gov.cn/s?sid=0&wd=%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f%20%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0&p={page_num}&vc=',

        'total_news_num': 17030,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[5]/div[2]/div[2]/ul/li',
                     'title': 'x://h4/a',
                     'date': ['x://div/text()'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"arialoadData=true; ariawapChangeViewPort=true; ASP.NET_SessionId=yabuq4paf3umzzklftg3ebjy; Power::SiteUniqueVisitorKey=/1/; __RequestVerificationToken=75D0TbPnYJJGBisCYiJtpzjppcAaJrGPbk1sfh2S0L8SjAB5FsfD1DAj6xdr1Qb8OwKv_Q2","Host":"www.shangqiu.gov.cn","Referer":"https://www.shangqiu.gov.cn/s?wd=%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f%20%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0&tt=0&bt=&et=&kp=1&as=true&qal=&qad=%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f%20%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0&qo=%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f&qn=&ps=10&st=2&siid=1&sid=1&p=2&vc=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)

    scraper.run()