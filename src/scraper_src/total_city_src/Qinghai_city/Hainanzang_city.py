from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_code': 324,
        'city_name': '海南藏族自治州',
        'province_name': '青海省',
        'province': '青海省',

        'base_url': 'https://www.hainanzhou.gov.cn/s?wd=%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0&tt=0&bt=&et=&kp=1&st=1&iiid=0&siid=0&csid=0&sid=0&p={page_num}',
        'total_news_num': 34,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://div[5]/div[3]/div[1]/ul/li',
                     'title': 'x://h4/a',
                     'date': ['xpath://div'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"Power_SiteUniqueVisitorKey=%2F1%2F; .Antiforgery=CfDJ8E5vOt_wYupGnCJdfC8BiaLjrjpF8MBv_8nxxsFSh-KBfl3aHsFCeJcvnlJYrXvftjaPY5x5eI9Jm0_JLSFBQLYfmZR8Wu5rjMVHXOrPl6NmQflBoXzh_jdoXEMl73kjcDwKyvJL6SfZsEBCH8urpnc; SessionVerify=6cc4aa0b-7dc1-4bff-8539-a3d23e7d0b5d; .PowerSession=CfDJ8E5vOt%2FwYupGnCJdfC8BiaLTQ0V8bjweBst11c39qlLk7PURY8kYZoRWZFM8vty7DiASpTKwmNLwg%2BM2ky8xW4Puq2OATwNWbToQ7%2BV7ptwwW5DT41G2C2NpZ6mGU%2B0lm1%2F89vCucKVYPIlqczPRAnn6iU0daQ2XUvkfJN6wS%2Fda","Host":"www.hainanzhou.gov.cn","Referer":"https://www.hainanzhou.gov.cn/s?wd=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&tt=0&bt=&et=&kp=1&st=1&iiid=0&siid=0&csid=0&sid=0","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()