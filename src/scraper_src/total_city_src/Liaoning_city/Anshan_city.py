import json

from scraper.scraper import Scraper


if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：API
    提取方法：JSON -- data -- data -- title, createDate, url
    """

    city_info = {
        'city_name': '鞍山市',
        'province_name': '辽宁省',
        'province': 'Liaoning',

        'base_url': 'http://www.anshan.gov.cn/search/search.ct?siteCode=ASSZF&isAll=0&offset={page_num}&limit=15&template=ASSZF&resultOrderBy=2&ssfw=1&sswjlx=1&timefw=1&columnTypeId=&searchKey=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0',

        'total_news_num': 28,
        'each_page_news_num': 20,
    }

    content_xpath = {'frames': 'x://*[@class="result-li"]',
                     'title': 'x://a',
                     'date': ['x://div[2]/span[1]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"SESSION=32b0caf3-88fc-4aae-808c-bc4cb713a4c2","Host":"www.anshan.gov.cn","Referer":"http://www.anshan.gov.cn/search/search.ct?siteCode=ASSZF&isAll=0&offset=0&limit=15&template=ASSZF&resultOrderBy=2&ssfw=2&sswjlx=1&timefw=1&columnTypeId=&searchKey=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0+%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()
