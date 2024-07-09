import json

from scraper.scraper import Scraper


if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：API
    提取方法：JSON -- data -- data -- title, createDate, url
    """

    city_info = {
        'city_name': '广元市',
        'province_name': '四川省',
        'province': 'Sichuan',

        'base_url': 'https://www.cngy.gov.cn/isearch.html?q=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60',

        'total_news_num': 622,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="dataList"]/div/ul/li',
                     'title': 'x://h1/a',
                     'date': ['x://h2/span[2]'],
                     'next_button': 'x://a[contains(text(),"下一页")]',
                     # 'url': 'x://a'
                     }

    scraper = Scraper(city_info, method='listen', data_type='html',
                      content_xpath=content_xpath, is_headless=False)

    scraper.method_LISTEN()
    scraper.save_files()
