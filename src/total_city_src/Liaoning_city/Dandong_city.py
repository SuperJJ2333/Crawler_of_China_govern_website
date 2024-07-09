from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '丹东市',
        'province_name': '辽宁省',
        'province': 'Liaoning',

        'base_url': 'https://www.dandong.gov.cn/search/search.ct?siteCode=DDSZF',

        'total_news_num': 2,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@class="result-li"]',
                     'title': 'x://a',
                     'date': ['x://div[2]/span[1]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Connection":"keep-alive","Content-Length":"146","Content-Type":"application/x-www-form-urlencoded","Cookie":"c_search_key=%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%2C%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; __51vcke__Jw2HJdH8OtJrOI4K=c6004116-f7ca-5273-9558-0346f082186e; __51vuft__Jw2HJdH8OtJrOI4K=1720006059411; JSESSIONID=894cd3f04dd733e81b159098e8e7; __51uvsct__Jw2HJdH8OtJrOI4K=2; __vtins__Jw2HJdH8OtJrOI4K=%7B%22sid%22%3A%20%22aba62348-3e3f-5c1a-8658-f14424b682ef%22%2C%20%22vd%22%3A%204%2C%20%22stt%22%3A%2016517%2C%20%22dr%22%3A%206134%2C%20%22expires%22%3A%201720011753096%2C%20%22ct%22%3A%201720009953096%7D","Host":"www.dandong.gov.cn","Origin":"https://www.dandong.gov.cn","Referer":"https://www.dandong.gov.cn/","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'searchKey': '学习考察 考察学习', 'siteCode': 'DDSZF', 'limit': '15', 'template': 'DDSZF', 'isAll': '0', 'resultOrderBy': '0'}

    page_num_name = 'page'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      verify=False, proxies=fiddler_proxies, post_data=post_data,
                      page_num_name=page_num_name
                      )
    scraper.run()