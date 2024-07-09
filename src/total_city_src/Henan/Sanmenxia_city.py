from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '三门峡市',
        'province_name': '河南省',
        'province': 'Henan',

        'base_url': 'http://www.smxsfq.gov.cn/pageView/classifiedSearch.html?pageNum={page_num}&searchText=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&s_lmnrlx=-1&s_fbsj_s=&s_fbsj_e=&sortType=1',

        'total_news_num': 1513,

        'each_page_news_num': 15,
    }

    content_xpath = {'frames': 'x://*[@id="searchForm"]/div[2]/div[2]/div[1]/div[2]/div/p[1]',
                     'title': 'x://a',
                     'date': ['x:..//p[3]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"_gscu_1611217242=19853861m7bp3l46; _gscbrs_1611217242=1; zh_choose=n; JSESSIONID=AA3F46C9B6C89C1199943688EECB8A69; _gscs_1611217242=19853861wqnq4u46|pv:3","Host":"www.smxsfq.gov.cn","Referer":"http://www.smxsfq.gov.cn/pageView/classifiedSearch.html?searchText=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&s_lmnrlx=-1&sortType=1&protocol=null%3A%3A&s_fbsj_s=&s_fbsj_e=&anyKeyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&noKeyword=&searchRange=2&s_fbsj_s=&s_fbsj_e=","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()