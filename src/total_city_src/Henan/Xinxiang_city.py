from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '新乡市',
        'province_name': '河南省',
        'province': 'Henan',

        'base_url': 'http://www.xinxiang.gov.cn/search/SolrSearch/s',

        'total_news_num': 25,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@class="media"]',
                     'title': 'x://div/h4/a',
                     'date': ['x://div[1]/div/i'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Connection":"keep-alive","Content-Length":"250","Content-Type":"application/x-www-form-urlencoded","Cookie":"mode=2; wzafullscreen=0; Hm_lvt_63a9a12ea3e7580fd15ff8758683c704=1719851725; Hm_lpvt_63a9a12ea3e7580fd15ff8758683c704=1719851725; Hm_lvt_30118f867de1399eb4e7cb998fb4bf47=1719851725; JSESSIONID=a1edb466-c10a-49fc-88b9-54061ba92f10; Hm_lpvt_30118f867de1399eb4e7cb998fb4bf47=1719852713","Host":"www.xinxiang.gov.cn","Origin":"http://www.xinxiang.gov.cn","Referer":"http://www.xinxiang.gov.cn/search/SolrSearch/s","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = {'token4': '85a25b7f477a488fa02f5ff94a4c68a0', 'q': '学习考察 考察学习', 'articlePublishTimeStart': '', 'articlePublishTimeEnd': '', 'siteId': '641a8f75d6d44ac09a68afc6aae73c23', 'rows': '10', 'page': '3', 'catalogLevel': '', 'type': 'articleTitle'}

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