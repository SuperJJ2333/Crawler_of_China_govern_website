from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_code': 303,
        'city_name': '塔城地区',
        'province_name': '新疆省',
        'province': '新疆省',

        'base_url': 'https://www.xjtc.gov.cn/s?wd=%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f&sid=0&p={page_num}',

        'total_news_num': 39,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://div[5]/div[3]/div[1]/ul/li',
                     'title': 'x://h4/a',
                     'date': ['xpath://div'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"Power_SiteUniqueVisitorKey=%2F1%2F; showGuide=true; .AspNetCore.Antiforgery.MFWShTntNEc=CfDJ8Ki7PIP5OWhAsCzXsku7YuPZ0OPCt1VrcS2Wj6T33m6QYxUMdBBwdg6-AinZty3-VQ74xDQ9yERHFRlGCQsfEkFAwU3AKvc9ay1Wm_0E2EsMu_yBF9mBta24m_W6ofRN3cweHKDYWmzASoH1QCGVWvc; .AspNetCore.Session=CfDJ8Ki7PIP5OWhAsCzXsku7YuPHXb%2BzsyoJcuFlqMgvEPEXRRActhwmyaE9ZcJpiBGQLbucSExgDY92732G4XcYwuHmgfZzRLNzdhvVaOwUy8ZWG9RgGJW80JToaFE%2F86TZIYIe60zMgxR0VzRn7Otr2N6QXbT3Z2xBGqJlb2LAMCam","Host":"www.xjtc.gov.cn","Referer":"https://www.xjtc.gov.cn/s?wd=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&sid=0&vc=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()