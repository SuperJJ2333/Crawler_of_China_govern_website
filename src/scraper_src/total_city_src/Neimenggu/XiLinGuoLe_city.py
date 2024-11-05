from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_code': 336,
        'city_name': '锡林郭勒盟',
        'province_name': '内蒙古',
        'province': '内蒙古省',

        'base_url': 'https://www.xlgl.gov.cn/search/pcRender?pageId=a76aa585450240478eb8287dcbe39db4',

        'total_news_num': 3700,
        'each_page_news_num': 6,
    }

    content_xpath = {'frames': 'x://*/div[@class="list-article"]',
                     'title': 'x://h3/a',
                     'date': ['x://div/p[2]/span[2]',
                              'x://div/div[3]/p[1]/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Connection":"keep-alive","Content-Length":"540","Content-Type":"application/x-www-form-urlencoded","Cookie":"JSESSIONID=3C0B9403ECD5B1B25DD9BEC82210468E; aisteUv=17304598222642301366923; aisiteJsSessionId=17307137884382520507664","Host":"www.xlgl.gov.cn","Origin":"null","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = 'qAnd=&qOr=&qAll=&qNot=&startTime=&endTime=&advSearch=&originalSearchUrl=%2FpcRender%3FpageId%3Da76aa585450240478eb8287dcbe39db4&originalSearch=&app=3703c47ec4e942149f6978cb88101b2c%2Ce211ddcdd27b4a04abb00b16fec320ac%2Cd51c8d504a284a11a98ff41a2dda89a7%2Ce3201b2163b44356bf359a01183b7153%2Cbe4365c89dd141168b8377a1463beedb%2C3176aa30f3824d699d64e5aac6c04f15&searchArea=&appName=&sr=score+desc&advtime=&siteId=bacf76d7a50f47189d9e8316a6fb8dcc&articleType=&advrange=&ext=&pNo=2&deviceType=pc&province=&q2=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    page_num_name = 'pNo'

    scraper = Scraper(city_info, method='post', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      verify=False, proxies=fiddler_proxies, post_data=post_data,
                      page_num_name=page_num_name
                      )
    scraper.run()