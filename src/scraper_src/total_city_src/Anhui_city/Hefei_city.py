from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    使用CLASH Proxies
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '合肥市',
        'province_name': '安徽省',
        'province': 'Anhui',
        'base_url': 'https://www.hefei.gov.cn/site/search/6784331?platformCode=&fuzzySearch=false&isAllSite=true&siteId=&columnId=&columnIds=&typeCode=all&beginDate=&endDate=&fromCode=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&oldKeywords=&subkeywords=&filterKeyWords=&excColumns=&dateKey=publishDate&datecode=&sort=intelligent&type=&tableColumnId=&indexNum=&fileNum=&flag=false&pageIndex={page_num}&pageSize=10&colloquial=true',

        # 新闻总数
        # 'total_news_num': 24,
        'total_news_num': 3407,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="search_list"]/ul',
                     'title': 'x://li[1]/a',
                     'date': ['x://li[2]/table//tr[3]/td[2]', 'x://li[3]/span[2]'],
                     'next_button': 'x://a[contains(text(),"下一页")]',}

    scraper = Scraper(city_info, method='listen', data_type='html',
                      content_xpath=content_xpath, is_headless=True)

    scraper.method_LISTEN()
    scraper.save_files()
