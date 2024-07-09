from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '攀枝花市',
        'province_name': '四川省',
        'province': 'Sichuan',

        'base_url': 'http://bot.panzhihua.gov.cn/search/index.html?keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20&isLocalWebSite=false&sortType=timeSort&siteId=14',

        'total_news_num': 2014,
        'each_page_news_num': 15,
    }

    content_xpath = {'frames': 'x://*[@id="results"]/div/a',
                     'title': 'x:/../a',
                     'date': ['x:/../div/div/div/div[1]/font'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Content-Length":"223","Content-Type":"application/x-www-form-urlencoded","Host":"bot.panzhihua.gov.cn","Origin":"http://bot.panzhihua.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://bot.panzhihua.gov.cn/search/index.html?keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20&isLocalWebSite=false&sortType=timeSort&siteId=14","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = {'searchType': 'fullSearch', 'keyword': '学习考察 考察学习', 'isLocalWebSite': 'false', 'siteId': '14', 'channel': 'all', 'timeCondition': 'unlimitedTime', 'dateRange': '', 'queryFilter': '', 'sortType': 'timeSort', 'page': '3'}

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