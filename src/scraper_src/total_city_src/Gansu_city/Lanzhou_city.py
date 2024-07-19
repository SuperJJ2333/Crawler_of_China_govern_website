from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：listen -- GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '兰州市',
        'province_name': '甘肃省',
        'province': 'Gansu',
        'base_url': 'https://www.lanzhou.gov.cn/jrobot/search.do?webid=1&pg=10&p={page_num}&tpl=&category=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pos=&od=2&date=&date=',

        'total_news_num': 329,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="jsearch-result-items"]/div',
                     'title': 'x://div[2]/a',
                     'date': ['x://div[3]/div[1]/span'],
                     'next_button': 'x://a[contains(text(),"下一页")]',
                     # 'url': 'x://a'
                     }

    headers = {"Host":"www.lanzhou.gov.cn","Connection":"keep-alive","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\"","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"navigate","Sec-Fetch-User":"?1","Sec-Fetch-Dest":"document","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"user_sid=cc33f3981cbe45a3a5444f2bc4397c84; JSESSIONID=AB6188B0FACC61299ADD71564429407D; rgHdgRP9MKUJO=5ENG936wNNatxBEvbiw936hYCVQAAeDvikAckbNa36NUO49wH8NIFav61vClBEW.Ebx8HjxXZ3DMtzYn3OEwH5A; _gscu_1846752234=19814477162igt90; _gscbrs_1846752234=1; _gscs_1846752234=19814477iu15si90|pv:1; rgHdgRP9MKUJP=5RLxEwDFc1U7qqqDAMH6WHGGoZd1M8koK8hk3YyifcqkVwtVz4Weh2fy4yYlojEJMa9RD3nO_uSxzbE7PTuM7SKftThxBbXjBWqu9h.J2jT5UeFn2pjegGz6JnWSzsRxZF5QTMd9CmA4nfdpMKwBYaaqACZvUl0Go9UXjfb2hoZ6k7u1pskr8DB4IM8.w_966TC56u942RFe68zVfF7Dwrl2uH.tZ64N3JKz_gN5rhk9gMrjW_p6dGcbIJtytD.BSCI3gxjQEf32_H4OGQcjYvbAiuFmq_CAUD0D4aoXLQ6_Y_GHlQnhdtwrbmqLK5Mv8XKtqtAJan5J.esIeKcM0eh"}

    listen_name = 'www.lanzhou.gov.cn/jrobot/search.do'

    scraper = Scraper(city_info, method='listen', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=False, listen_name=listen_name)

    scraper.method_LISTEN()
    scraper.save_files()
