from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '滁州市',
        'province_name': '安徽省',
        'province': 'Anhui',
        'base_url': 'https://www.chuzhou.gov.cn/site/search/2653861?isAllSite=true&platformCode=&siteId=&columnId=&columnIds=&typeCode=&beginDate=&endDate=&fromCode=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&excColumns=&datecode=&sort=intelligent&type=&tableColumnId=&subkeywords=&orderType=0&indexNum=&fileNum=&pid=&language=&oldKeywords=&flag=false&searchType=&searchTplId=&fuzzySearch=true&internalCall=false&pageIndex={page_num}&pageSize=10',

        # 新闻总数
        'total_news_num': 2553,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://ul[@class="search-list"]',
                     'title': 'x://li[1]/a',
                     'date': ['x://li[2]/span[2]']
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"__jsluid_s=e06d671413fb8b08cf989d36e53ab3a0; search_history=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%2C%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; SHIROJSESSIONID=73c73559-5cb8-47fc-98fa-9030b3f8d9d3; JSESSIONID=CEFFFE85A6445549190F3AFB73ADC57F; __jsl_clearance_s=1720785972.726|0|vklvJS%2FYzA18Y78oFWthkrgfNV0%3D; wzaConfigTime=1720785978162","Host":"www.chuzhou.gov.cn","Referer":"https://www.chuzhou.gov.cn/site/search/2653861?isAllSite=true&platformCode=&siteId=&columnId=&columnIds=&typeCode=&beginDate=&endDate=&fromCode=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&excColumns=&datecode=&sort=intelligent&type=&tableColumnId=&subkeywords=&orderType=0&indexNum=&fileNum=&pid=&language=&oldKeywords=&flag=false&searchType=&searchTplId=&fuzzySearch=true&internalCall=false&pageIndex=6&pageSize=10","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()
