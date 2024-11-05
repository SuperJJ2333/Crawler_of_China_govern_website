from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_code': 300,
        'city_name': '阿克苏地区',
        'province_name': '新疆省',
        'province': '新疆省',

        'base_url': 'http://www.aksu.gov.cn/ssxjcms/front/aisearch/loaddata.do?tplid=0&indexids=1&siteid=0&searchscope=0&timescope=0&sorttype=0&lastwd=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&secondsearch=&curpageno={page_num}&pagesize=10&categorycode=&wd=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0',

        'total_news_num': 450,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html//table//tr/td[2]',
                     'title': 'x://table[1]//tr/td/a',
                     'date': ['xpath://table[3]//tr/td[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"0","Cookie":"Secure; VISIT_UV=203501172918506049268","Host":"www.aksu.gov.cn","Origin":"http://www.aksu.gov.cn","Referer":"http://www.aksu.gov.cn/ssxjcms/front/aisearch/search.do?indexids=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","X-Requested-With":"XMLHttpRequest"}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=False,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()