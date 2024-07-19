from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '本溪市',
        'province_name': '辽宁省',
        'province': 'Liaoning',
        'base_url': 'https://www.benxi.gov.cn/s?wd=%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f%20%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0&sid=1&siid=1&p={page_num}',


        'total_news_num': 10291,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[3]/div[2]/div[2]/ul/li',
                     'title': 'x://h4/a',
                     'date': ['x://div/text()'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"showGuide=true; __vtins__JkwZnxz6gsFrTIGW=%7B%22sid%22%3A%20%22735c7d42-0a27-5271-8809-dbcee5b61fdb%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201720007847568%2C%20%22ct%22%3A%201720006047568%7D; __51uvsct__JkwZnxz6gsFrTIGW=1; __51vcke__JkwZnxz6gsFrTIGW=b4ffefd7-517b-5d46-ab3b-c9bd0638265e; __51vuft__JkwZnxz6gsFrTIGW=1720006047571; _gscu_841053871=20006048lpdywg13; _gscbrs_841053871=1; __RequestVerificationToken=D_2kZdiqMHmT2KGxoVu4Jhq1C7zjk-cnFAvgmiOwZO3Ne9T4dzXPKN7NyDjZWml6RIGsTQ2; ASP.NET_SessionId=2qneupfagrx2gae3hf1svqjq; PowerLeaveSitePrompts=OnlyGovNoShow; PowerUniqueVisitor=a9b1d8d0-41d6-476e-aa25-27195fa0c0a4_2024%2F7%2F3%200%3A00%3A00","Host":"www.benxi.gov.cn","Referer":"https://www.benxi.gov.cn/s?wd=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&sid=1&siid=1","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()