from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '泸州市',
        'province_name': '四川省',
        'province': 'Sichuan',
        'base_url': 'https://www.luzhou.gov.cn/s?sid=0&wd=%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0&p={page_num}&vc=',

        'total_news_num': 2697,

        'each_page_news_num': 10,
    }

    # 隧道域名:端口号
    tunnel = "t183.kdltps.com:15818"

    # 用户名密码方式
    username = "t12119257695353"
    password = "lornoi3v"
    proxies = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
        "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
    }

    content_xpath = {'frames': 'x:/html/body/div[5]/div[3]/div[1]/ul/li',
                     'title': 'x://h4/a',
                     'date': ['x://div/text()'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"HWWAFSESID=a5765739a57a732d3d; HWWAFSESTIME=1721188780020; Power::SiteUniqueVisitorKey=/1/; __RequestVerificationToken=JAirHCOkXYjthPJh_E3ScEzHUigNBTB68nHJAQUlHJdFJFL9Mp0kHFPD7KUPUVlaFbHW0g2; arialoadData=false; ASP.NET_SessionId=jp23bwd1kbzfjlwbfycis5c5","Host":"www.luzhou.gov.cn","Referer":"https://www.luzhou.gov.cn/s?sid=0&wd=%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0&p=3&vc=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}
    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      thread_num=1)
    scraper.run()