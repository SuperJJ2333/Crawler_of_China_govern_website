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

    content_xpath = {'frames': 'x://*/div[3]/div[1]/div[1]/ul/li',
                     'title': 'x://a',
                     'date': ['x://div[2]/p[3]',
                              'x://li[2]/span[2]']
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"__jsluid_s=e06d671413fb8b08cf989d36e53ab3a0; __jsl_clearance_s=1719667154.247|0|1tX74tZ%2BkbZ72za1XXjPfEaYsME%3D; SHIROJSESSIONID=daf2f30a-e502-4488-b5b0-be225a04c935; wzaConfigTime=1719667159310; search_history=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%2C%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Host":"www.chuzhou.gov.cn","Referer":"https://www.chuzhou.gov.cn/site/search/2653861?typeCode=all&oldKeywords=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&beginDate=&endDate=&fromCode=&models=news%2CworkGuide%2Cpublic_content%2CmessageBoard&isAllSite=true&platformCode=&siteId=&columnId=&fuzzySearch=true&sort=intelligent&orderType=0&subkeywords=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()
