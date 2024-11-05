from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_code': 302,
        'city_name': '和田地区',
        'province_name': '新疆省',
        'province': '新疆省',

        'base_url': 'https://www.xjht.gov.cn/article/so.php?moduleid=5&searchid=1&fields=2&catid=0&kw=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F',

        'total_news_num': 20,

        'each_page_news_num': 20,
    }

    content_xpath = {'frames': 'x://div[6]/div/div[3]/div[1]/ul/li',
                     'title': 'x://p[1]/a',
                     'date': ['xpath:/p[3]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
               }
    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()