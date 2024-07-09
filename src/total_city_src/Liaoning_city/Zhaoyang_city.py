from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '朝阳市',
        'province_name': '辽宁省',
        'province': 'Liaoning',

        'base_url': 'http://www.chaoyang.gov.cn/search/search.ct',

        'total_news_num': 41,
        'each_page_news_num': 15,
    }

    content_xpath = {'frames': 'x://*[@class="result-li"]',
                     'title': 'x://div/a',
                     'date': ['x://div[3]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Content-Length":"207","Content-Type":"application/x-www-form-urlencoded","Cookie":"c_search_key=%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; JSESSIONID=95F655DFB6C574707C5F755CE4556F68","Host":"www.chaoyang.gov.cn","Origin":"http://www.chaoyang.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.chaoyang.gov.cn/search/search.ct","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = {'siteCode': 'CYSZF', 'isAll': '0', 'offset': '1', 'limit': '15', 'template': 'CYSZF', 'resultOrderBy': '0', 'ssfw': '2', 'sswjlx': '1', 'timefw': '1', 'columnTypeId': '', 'columnType': '1', 'searchKey': '学习考察 考察学习'}

    page_num_name = 'offset'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      verify=False, proxies=fiddler_proxies, post_data=post_data,
                      page_num_name=page_num_name, page_num_start=0
                      )
    scraper.run()