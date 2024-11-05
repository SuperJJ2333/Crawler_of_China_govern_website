import json

from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_code': 335,
        'city_name': '兴安盟',
        'province_name': '内蒙古省',
        'province': '内蒙古省',

        'base_url': 'https://www.xam.gov.cn/search/pcRender?pageId=92b54cc5cdac4ac6908a0762169b2d86',

        'total_news_num': 2058,
        'each_page_news_num': 15,
    }

    content_xpath = {'frames': 'x://*/div[@class="list-article"]',
                     'title': 'x://h3/a',
                     'date': ['x://div/p[2]/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Connection":"keep-alive","Content-Length":"563","Content-Type":"application/x-www-form-urlencoded","Cookie":"aisearchbehavior=be3ea35c899b42bda4c058b67863e980; JSESSIONID=10FA27CFFD752B35122D10DAE38CFA2C; _gscu_1151606483=304592193ogfvd17; aisteUv=1730459221092369752572; _gscbrs_1151606483=1; aisiteJsSessionId=17307134175912876122956; _gscs_1151606483=3071341527wubg17|pv:4","Host":"www.xam.gov.cn","Origin":"https://www.xam.gov.cn","Referer":"https://www.xam.gov.cn/search/pcRender?pageId=92b54cc5cdac4ac6908a0762169b2d86","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = 'qAnd=&qOr=&qAll=&qNot=&startTime=&endTime=&advSearch=&originalSearchUrl=%2Fsearch%2FpcRender%3FpageId%3D92b54cc5cdac4ac6908a0762169b2d86&originalSearch=&app=0cccd7bc673642329c021bcb2101a2f1%2C69c97ba2174e4852b80116c64f247ce2%2Cc56223bb65294b148a4ec93fe0ae4cbc%2C81df96d673a74c75a3111cc5f27759bf%2C1b2816409a4a4f46bbb591cdd7d17b95%2Cec3f0b563a7e412aadd2795611b6fb14%2Cb9d331c441b047b79213a7aa08630876&searchArea=&appName=&sr=score+desc&advtime=&advrange=&articleType=&siteId=300448&siteName=&pNo=2&deviceType=pc&province=&q2=&q=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0'

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