from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '承德市',
        'province_name': '河北省',
        'province': 'Hebei',
        'base_url': 'https://www.chengde.gov.cn/jrobot/search.do?webid=1&pg=12&p={page_num}&tpl=&category=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&pos=&od=&date=&date=',

        'total_news_num': 194,

        'each_page_news_num': 12,
    }

    content_xpath = {'frames': 'x://*[@id="jsearch-result-items"]/div',
                     'title': 'x://div[2]/a[1]',
                     'date': ['x://div[3]/div[1]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"user_sid=b3edf23602314edbbc8dd08a8de1fce9; JSESSIONID=C2BFD199913543B5A2604A097B6A1EB2; Path=/","Host":"www.chengde.gov.cn","Referer":"https://www.chengde.gov.cn/jrobot/search.do?webid=1&pg=12&p=1&tpl=&category=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&pos=&od=&date=&date=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()