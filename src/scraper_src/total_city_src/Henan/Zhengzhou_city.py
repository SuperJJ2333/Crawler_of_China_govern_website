from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '郑州市',
        'province_name': '河南省',
        'province': 'Henan',

        'base_url': 'https://www.zhengzhou.gov.cn/search_{page_num}.jspx?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&result_type=2&source=&place=&cid=&mid=&orderby=',

        'total_news_num': 6596,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="full_text_search_form"]/div[2]/div/div[3]/div[2]/a',
                     'title': 'x:..//a',
                     'date': ['x://em[1]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"clientlanguage=zh-CN; Hm_lvt_3916fbf06400bbbf67a1f28f721a5cb3=1719841588,1720953338; HMACCOUNT=A202F23FD4E0D795; Hm_lpvt_3916fbf06400bbbf67a1f28f721a5cb3=1720953373","Host":"www.zhengzhou.gov.cn","Referer":"https://www.zhengzhou.gov.cn/search_5.jspx?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()