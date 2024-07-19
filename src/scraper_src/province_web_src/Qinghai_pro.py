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

        'total_news_num': 115,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/ul/li',
                     'title': 'x:/a[1]',
                     'date': ['x://p/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"290","Content-Type":"application/x-www-form-urlencoded","Cookie":"_gscu_1919651756=20550522pif21y62; _gscbrs_1919651756=1; _gscs_1919651756=21357251tq4p5z20|pv:1; arialoadData=true; JSESSIONID=E5C202801B196E9416493A188100B9A1.was5.1","Host":"www.qinghai.gov.cn","Origin":"http://www.qinghai.gov.cn","Referer":"http://www.qinghai.gov.cn/was5/web/search","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest"}

    post_data = {'page': '3', 'channelid': '219598', 'searchword': '学习考察考察学习', 'keyword': '学习考察考察学习', 'perpage': '10', 'outlinepage': '10', 'jsessionid': 'E5C202801B196E9416493A188100B9A1', 'templet': 'zwgk_search_content.jsp'}

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