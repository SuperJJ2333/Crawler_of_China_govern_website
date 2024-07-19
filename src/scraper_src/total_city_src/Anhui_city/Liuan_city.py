from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '六安市',
        'province_name': '安徽省',
        'province': 'Anhui',
        'base_url': 'https://www.luan.gov.cn/site/search/6789941?platformCode=&isAllSite=true&siteId=&columnId=&columnIds=&typeCode=&beginDate=&endDate=&fromCode=title&keywords=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&oldKeywords=&subkeywords=&filterKeyWords=&excColumns=&datecode=&sort=intelligent&orderType=1&fuzzySearch=false&type=&tableColumnId=&indexNum=&fileNum=&flag=false&pageIndex={page_num}&pageSize=10&pid=&leaderTypeId=&liId=',
        # 新闻总数
        'total_news_num': 784,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="search_list"]/ul',
                     'title': 'x://li[1]/a',
                     'date': ['xpath://li[4]/span[2]',
                              'xpath://li[3]/span[2]',
                              'xpath://li[2]/table//tr[3]/td[2]/text()']
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Connection":"keep-alive","Cookie":"luan_gova_SHIROJSESSIONID=2526abbe-53f9-45ed-b5ef-27fc5dbe77c0; __jsluid_s=d21e5957232c95e5fd7c3175be26edc9; wzaConfigTime=1719667408522; search_history=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%40%7C%40%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%40%7C%40%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Host":"www.luan.gov.cn","Referer":"https://www.luan.gov.cn/site/search/6789941?oldKeywords=&keywords=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&beginDate=&endDate=&fromCode=title&orderType=1&sort=intelligent&fuzzySearch=false&isAllSite=true&platformCode=&siteId=&columnId=&models=news%2CworkGuide%2CmessageBoard%2Cpublic_content%2Cla_video&subkeywords=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()
