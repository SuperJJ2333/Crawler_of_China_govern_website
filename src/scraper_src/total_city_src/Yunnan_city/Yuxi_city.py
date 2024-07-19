from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '玉溪市',
        'province_name': '云南省',
        'province': 'Yunnan',

        'base_url': 'http://www.yuxi.gov.cn/yxgovfront/search_{page_num}.jspx?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&orderBy=time&_s_=1&dir=desc&rangeBy=&channelName=',

        'total_news_num': 1585,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[1]/div[3]/div/div[2]/dl',
                     'title': 'x://dt/a',
                     'date': ['x://dd[3]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"JSESSIONID=DA9F3C267CFE0A784BD2AFF9E1854EB1; _site_id_cookie=1; _site_id_cookie=1; clientlanguage=zh_CN","Host":"www.yuxi.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.yuxi.gov.cn/yxgovfront/search_2.jspx?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&orderBy=time&_s_=1&dir=desc&rangeBy=title&channelName=","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()