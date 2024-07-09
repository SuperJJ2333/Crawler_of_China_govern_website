from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    使用CLASH Proxies
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '合肥市',
        'province_name': '安徽省',
        'province': 'Anhui',
        'base_url': 'https://www.hefei.gov.cn/site/search/6784331?platformCode=&fuzzySearch=false&isAllSite=true&siteId=&columnId=&columnIds=&typeCode=all&beginDate=&endDate=&fromCode=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&oldKeywords=&subkeywords=&filterKeyWords=&excColumns=&dateKey=publishDate&datecode=&sort=intelligent&type=&tableColumnId=&indexNum=&fileNum=&flag=false&pageIndex={page_num}&pageSize=10&colloquial=true',

        # 新闻总数
        # 'total_news_num': 24,
        'total_news_num': 9407,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="search_list"]/ul',
                     'title': 'x://li[1]/a',
                     'date': ['x://li[2]/table//tr[3]/td[2]', 'x://li[3]/span[2]']}

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"__jsluid_s=d4913291e8caeeb03cf8fe23aae051d8; search_history=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; hefei_gova_SHIROJSESSIONID=16105d9b-65c5-4ab7-bba4-0b7448349c9f; arialoadData=false; __jsl_clearance_s=1719648970.674|0|mCJDLOZkvdSCPPd5Yy%2BkNt%2FAOR8%3D","Host":"www.hefei.gov.cn","Referer":"https://www.hefei.gov.cn/site/search/6784331?platformCode=&fuzzySearch=false&isAllSite=true&siteId=&columnId=&columnIds=&typeCode=all&beginDate=&endDate=&fromCode=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&oldKeywords=&subkeywords=&filterKeyWords=&excColumns=&dateKey=publishDate&datecode=&sort=intelligent&type=&tableColumnId=&indexNum=&fileNum=&flag=false&pageIndex=3&pageSize=10&colloquial=true","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True, proxies=proxies)
    scraper.run()
