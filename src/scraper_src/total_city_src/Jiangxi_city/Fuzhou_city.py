from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '抚州市',
        'province_name': '江西省',
        'province': 'Jiangxi',

        'base_url': 'http://www.jxfz.gov.cn/jrobot/search.do?webid=1&pg=12&p={page_num}&tpl=&category=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pos=title&od=&date=&date=',


        'total_news_num': 507,

        'each_page_news_num': 12,
    }

    content_xpath = {'frames': 'x://*[@id="jsearch-result-items"]/div',
                     'title': 'x://div[2]/a',
                     'date': ['x://div[3]/div[1]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"user_sid=01af96ee18ba41f783bf26fb42a6811d; JSESSIONID=432D22A93CB60D09BD07CAF75B7F690F","Host":"www.jxfz.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.jxfz.gov.cn/jrobot/search.do?webid=1&pg=12&p=1&tpl=&category=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pos=title&od=&date=&date=","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    fiddler_proxy = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxy, verify=False)
    scraper.run()
