from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '淮南市',
        'province_name': '安徽省',
        'province': 'Anhui',
        'base_url': 'https://www.huainan.gov.cn/site/search/4964522?platformCode=&fuzzySearch=false&orderType=0&isAllSite=true&siteId=&columnId=&columnIds=&typeCode=all&beginDate=&endDate=&fromCode=title&keywords=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&oldKeywords=&subkeywords=&excColumns=&datecode=&sort=desc&type=&tableColumnId=&indexNum=&catIds=&fileNum=&flag=false&colloquial=&pageIndex={page_num}&pageSize=10',

        # 新闻总数
        'total_news_num': 330,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="search_list"]/ul',
                     'title': 'x://li[1]/a',
                     'date': ['x://li[2]/span[3]', 'x://li[2]/span[2]']
                     # 'url': 'x://a'
                     }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
        }

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()
