from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '上海市',
        'province_name': '上海市',
        'province': 'Shanghai',

        'base_url': 'https://search.sh.gov.cn/searchResult',

        'total_news_num': 200,
        'each_page_news_num': 20,
    }

    content_xpath = {'frames': 'x://*[@class="result result-elm "]',
                     'title': 'x:/a[1]',
                     'date': ['x://div/div[1]/font[1]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"401","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"JSESSIONID=F3554F9C42BBA939092FB8AEF59DE75D; arialoadData=true; wondersLog_zwdt_sdk=%7B%22persistedTime%22%3A1720250306370%2C%22updatedTime%22%3A1720250307132%2C%22sessionStartTime%22%3A1720250306374%2C%22sessionReferrer%22%3A%22https%3A%2F%2Fsearch.sh.gov.cn%2Fsearch%3FsiteId%3Dwww.shanghai.gov.cn%26text%3D%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0%22%2C%22recommend_code%22%3A3250647175078949%2C%22sessionUuid%22%3A8512547222510211%2C%22LASTEVENT%22%3A%7B%22eventId%22%3A%22wondersLog_pv%22%2C%22time%22%3A1720250307131%7D%2C%22deviceId%22%3A%224068cbf949e83b55a1a6aa48c7e39503-4451%22%2C%22costTime%22%3A%7B%22wondersLog_unload%22%3A1720250307132%7D%7D; wondersLog_zwdt_G_D_I=4068cbf949e83b55a1a6aa48c7e39503-4451; ariawapChangeViewPort=false; AlteonP=BlYDFxvgEqxx1Wh5EZ3LQw$$","Host":"search.sh.gov.cn","Origin":"https://search.sh.gov.cn","Referer":"https://search.sh.gov.cn/search?siteId=www.shanghai.gov.cn&text=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'text': '学习考察考察学习', 'pageNo': '2', 'newsPageNo': '2', 'pageSize': '20', 'resourceType': '', 'channel': '', 'category1': '', 'category2': '', 'category3': '', 'category4': '', 'category6': '', 'category7': 'www.shanghai.gov.cn', 'sortMode': '', 'searchMode': '1', 'timeRange': '', 'accurateMode': '', 'district': '', 'street': '', 'stealthy': '1', 'showItemAgency': 'false', 'searchText': '学习考察考察学习'}

    page_num_name = ['pageNo', 'newsPageNo']

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      verify=False, proxies=fiddler_proxies, post_data=post_data,
                      page_num_name=page_num_name
                      )
    scraper.run()