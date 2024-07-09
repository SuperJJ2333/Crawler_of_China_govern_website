from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_name': '鄂尔多斯市',
        'province_name': '内蒙古省',
        'province': 'Neimenggu',

        'base_url': 'http://www.ordos.gov.cn/was40/search',

        'total_news_num': 10,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html//ol/script',
                     'title': 'x://div[1]/a',
                     'date': ['xpath://div[2]/span'],
                     'next_button': 'x://a[contains(text(),"下一页")]',
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Content-Length":"64","Content-Type":"application/x-www-form-urlencoded","Cookie":"_gscbrs_232331937=1; _gscs_232331937=20252113k4fv5i51|pv:2","Host":"www.ordos.gov.cn","Origin":"null","Proxy-Connection":"keep-alive","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = {'channelid': '297461', 'searchword': '学习考察'}

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      verify=False, proxies=fiddler_proxies, post_data=post_data,
                      )
    scraper.run()