from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '青海省',
        'province_name': '青海省',
        'province': 'province_web_data',

        'base_url': 'http://www.qinghai.gov.cn/was5/web/search',

        'total_news_num': 54,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/ul/li',
                     'title': 'x:/a[1]',
                     'date': ['x://p/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Transfer-Encoding":"chunked","Access-Control-Allow-Headers":"DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization","Access-Control-Allow-Origin":"*","Connection":"keep-alive","Content-Encoding":"gzip","Content-Type":"text/html;charset=UTF-8","Date":"Tue, 09 Jul 2024 19:00:15 GMT","Expires":"Wed, 31 Dec 1969 23:59:59 GMT","Keep-Alive":"timeout=4","Max-Age":"Thu, 01 Jan 1970 00:00:00 GMT","Proxy-Connection":"keep-alive","Server":"nginx","Vary":"Accept-Encoding"}

    post_data = {'page': '3', 'channelid': '219598', 'searchword': '学习考察 考察学习', 'keyword': '学习考察 考察学习', 'perpage': '10', 'outlinepage': '10', 'jsessionid': 'E4BB5956EAAF64C6AAB75981B242CAEB', 'templet': 'zwgk_search_content.jsp'}

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