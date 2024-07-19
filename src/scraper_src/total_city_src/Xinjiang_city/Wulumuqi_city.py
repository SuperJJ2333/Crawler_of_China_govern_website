from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '乌鲁木齐市',
        'province_name': '新疆省',
        'province': 'Xinjiang',
        'base_url': 'http://www.urumqi.gov.cn/search/searchResult.jsp?t_id=727&scope=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&btnOK=&p={page_num}',

        'total_news_num': 34,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="searchcon"]/div/a',
                     'title': 'x:/../a[1]',
                     'date': ['x:/../following-sibling::div[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"HttpOnly=true; HttpOnly=true; Hm_lvt_b8f3f83de99064e460a9e4618f73db07=1720245101; Hm_lpvt_b8f3f83de99064e460a9e4618f73db07=1720245101; HMACCOUNT=A202F23FD4E0D795; Hm_lvt_54951bed9473f69845fb549eef4c1cfd=1720245101; Hm_lpvt_54951bed9473f69845fb549eef4c1cfd=1720245101; JSESSIONID=08896AA83A7BC660CC399A9D64999C4D","Host":"www.urumqi.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.urumqi.gov.cn/search/searchResult.jsp?t_id=727&scope=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&btnOK=","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()