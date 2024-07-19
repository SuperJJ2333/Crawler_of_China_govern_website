from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：listen -- GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '景德镇市',
        'province_name': '江西省',
        'province': 'Jiangxi',

        'base_url': 'https://www.jdz.gov.cn/site/search/#/all?type=所有&siteId=8&name=%E6%99%AF%E5%BE%B7%E9%95%87%E5%B8%82%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C&wcmSiteId=38&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0',
        'total_news_num': 2008,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="app"]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/ul/li',
                     'title': 'x://div/div[1]/a',
                     'date': ['x://div//tr[2]/td[1]/span[2]', 'x://div/div[3]/div/span[2]'],
                     'next_button': "x://button[@class='btn-next ']",
                     # 'url': 'x://a'
                     }

    scraper = Scraper(city_info, method='listen', data_type='html',
                      content_xpath=content_xpath, is_headless=True)

    scraper.method_LISTEN()
    scraper.save_files()
