from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '甘肃省',
        'province_name': '甘肃省',
        'province': 'province_web_data',
        'base_url': 'https://www.gansu.gov.cn/guestweb4/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&column=%25E5%2585%25A8%25E9%2583%25A8&wordPlace=1&orderBy=0&startTime=&endTime=&pageSize=10&pageNum={page_num}&timeStamp=0&siteCode=6200000001&sonSiteCode=&checkHandle=1&strFileType=&govWorkBean=%257B%257D&sonSiteCode=&areaSearchFlag=-1&secondSearchWords=&topical=&pubName=&countKey=0&uc=0&isSonSite=false&left_right_index=0',

        'total_news_num': 33,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[2]/div[1]/div',
                     'title': 'x://div[1]/a',
                     'date': ['x://div[2]/div/p[2]/span'],
                     'next_button': 'x://a[contains(text(),"下一页")]',
                     # 'url': 'x://a'
                     }

    scraper = Scraper(city_info, method='listen', data_type='html',
                      content_xpath=content_xpath, is_headless=False)

    scraper.method_LISTEN()
    scraper.save_files()
