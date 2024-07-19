from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '资阳市',
        'province_name': '四川省',
        'province': 'Sichuan',

        'base_url': 'http://www.ziyang.gov.cn/search.aspx?key=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0',

        'total_news_num': 4,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@class="res_title_box"]',
                     'title': 'x://div[2]/a',
                     'date': ['x:/following-sibling::div[2]'],
                     'next_button': 'x://a[contains(text(),"下一页")]',
                     # 'url': 'x://a'
                     }

    scraper = Scraper(city_info, method='listen', data_type='html',
                      content_xpath=content_xpath, is_headless=True)

    scraper.method_LISTEN()
    scraper.save_files()
