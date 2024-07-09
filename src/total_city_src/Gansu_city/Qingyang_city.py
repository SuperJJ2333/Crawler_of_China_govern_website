from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '庆阳市',
        'province_name': '甘肃省',
        'province': 'Gansu',
        'base_url': 'https://www.zgqingyang.gov.cn/s?as=true&qal=&qad=&qo=%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f%20%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0&qn=&bt=&et=&kp=1&ps=10&sids=&siids=&p={page_num}&vc=',

        'total_news_num': 80,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[5]/div[2]/div[2]/ul/li',
                     'title': 'x://h4/a',
                     'date': ['x://div/text()[1]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"4hP44ZykCTt5S=60ESf7Ivp0kWRaMlurfICu7BpGrAIHrUfEQYSlJ184DxLvn6TrKcTyZx0oyz8Z.LByIp2cI_YS_Fxs8LgL8ku98a; _gscu_1155815754=198266081q03zd34; __ST__=1; HWWAFSESID=491a61755fd01eb8407; HWWAFSESTIME=1719899037388; showGuide=true; _gscbrs_1155815754=1; __RequestVerificationToken=iR2BlsZL1nn34bEQtodSISD7OAvgtxAhKnCa6gQbMmz67XetvQhyMQL-c8cBXTr70hIxnQ2; ASP.NET_SessionId=tod4a2tb3xolef3q4zk1mr5k; _gscs_1155815754=19899037nd2jad20|pv:5","Host":"www.zgqingyang.gov.cn","Referer":"https://www.zgqingyang.gov.cn/s?as=true&qal=&qad=&qo=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&qn=&bt=&et=&kp=1&ps=10&sids=&siids=&vc=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()
