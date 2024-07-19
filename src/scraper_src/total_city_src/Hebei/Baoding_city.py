from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '保定市',
        'province_name': '河北省',
        'province': 'Hebei',

        'base_url': 'https://www.baoding.gov.cn/index.do?view=search',

        'total_news_num': 2513,
        'each_page_news_num': 20,
    }

    content_xpath = {'frames': 'x:/html/body//table//tr/td[1]/a',
                     'title': 'x:/..//a',
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Connection":"keep-alive","Content-Length":"168","Content-Type":"application/x-www-form-urlencoded","Cookie":"authentication=qK+vJ8nkyMQctGRQlrDwln5zTcly/ic3yWN/HL855ezXCkCEfdk2O6HPHqHnJ9Nhxw0ml1xiowfNLz71rGs2ug==; barrier-free={%22show%22:false%2C%22audio%22:false%2C%22continuousRead%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22view%22:false%2C%22colorMatch%22:%22original%22%2C%22bigtextTraditional%22:false}; JSESSIONID=0060CB8D064DD1D025957CED2A5BFFB4-n1","Host":"www.baoding.gov.cn","Origin":"https://www.baoding.gov.cn","Referer":"https://www.baoding.gov.cn/index.do?view=search","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'keyword': '学习考察 考察学习', 'page': '', 'view': 'search', 'fields': 'title,contents', 'ctime': '0', 'orderStr': '0', 'ccid': ''}

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