from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '铁岭市',
        'province_name': '辽宁省',
        'province': 'Liaoning',

        'base_url': 'http://tielingxian.gov.cn/search/pcRender?pageId=b0827679e8314f909380e8f47211e958',

        'total_news_num': 9069,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="panel-left"]/div/div[2]/div[2]/div',
                     'title': 'x://div/h3/a',
                     'date': ['x://div/div/p[2]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Content-Length":"352","Content-Type":"application/x-www-form-urlencoded","Cookie":"JSESSIONID=807208107A7AF470724EC5C168DFCD03; aisearchbehavior=850a471a9b06477ead2d74bb95d84842; aisteUv=17200104461521243064401; aisiteJsSessionId=17200104461532972431873","Host":"tielingxian.gov.cn","Origin":"http://tielingxian.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://tielingxian.gov.cn/search/pcRender?pageId=b0827679e8314f909380e8f47211e958","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = {'qAnd': '', 'qOr': '', 'qAll': '', 'qNot': '', 'startTime': '', 'endTime': '', 'advSearch': '', 'originalSearchUrl': '/search/pcRender?pageId=b0827679e8314f909380e8f47211e958', 'originalSearch': '', 'app': '', 'searchArea': '', 'appName': '', 'sr': 'score desc', 'advtime': '', 'siteId': '', 'articleType': '', 'advrange': '', 'ext': '', 'pNo': '2', 'deviceType': 'pc', 'province': '', 'q2': '', 'q': '学习考察 考察学习'}

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