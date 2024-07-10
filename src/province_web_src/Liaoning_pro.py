from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '辽宁省',
        'province_name': '辽宁省',
        'province': 'province_web_data',

        'base_url': 'https://www.ln.gov.cn/search/pcRender?pageId=fe81c5eea00a4b72921268a33446352a',

        'total_news_num': 1423,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="panel-middle"]/div/div[2]/div[2]/div',
                     'title': 'x://div[1]/h3/a',
                     'date': ['x://div/div/p[3]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Connection":"keep-alive","Content-Length":"456","Content-Type":"application/x-www-form-urlencoded","Cookie":"aisearchbehavior=cc79974e2c8b47069173184e044e6446; JSESSIONID=708a2078ae33855828333b2aac92; Path=/; aisteUv=1720005268287698574279; Path=/; aisiteJsSessionId=172052081219977848192; arialoadData=true; ariawapChangeViewPort=true","Host":"www.ln.gov.cn","Origin":"https://www.ln.gov.cn","Referer":"https://www.ln.gov.cn/search/pcRender?sr=score+desc&app=18c96345cf0f439a87f154ccb9975848%2Cd15ce429a8954732a5a78da66fbe9aa2%2C0f013e4297ff420daf5dc55045df5022%2C5ebd6414b438490480a75d1f2232a316&pageId=fe81c5eea00a4b72921268a33446352a&ext=d8b2a4c4514647cfa4ed0c9107403478&pNo=1&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'qAnd': '', 'qOr': '', 'qAll': '', 'qNot': '', 'startTime': '', 'endTime': '', 'advSearch': '', 'originalSearchUrl': '/search/pcRender?pageId=fe81c5eea00a4b72921268a33446352a', 'originalSearch': '', 'app': '0f013e4297ff420daf5dc55045df5022,5ebd6414b438490480a75d1f2232a316', 'searchArea': '', 'appName': '', 'sr': 'score desc', 'advtime': '', 'advrange': '', 'articleType': '', 'siteId': 'd8b2a4c4514647cfa4ed0c9107403478', 'siteName': '', 'ext': '', 'pNo': '3', 'deviceType': 'pc', 'province': '', 'q2': '', 'q': '学习考察 考察学习'}

    page_num_name = 'pNo'

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