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
        'base_url': 'https://www.zgqingyang.gov.cn/s?sid=0&wd=%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f%20%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0&p={page_num}&vc=',
        'total_news_num': 621,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[5]/div[2]/div[2]/ul/li',
                     'title': 'x://h4/a',
                     'date': ['x://div/text()[1]'],
                     # 'url': 'x://a'
                     }

    headers = {"Host":"www.zgqingyang.gov.cn","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\"","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"navigate","Sec-Fetch-User":"?1","Sec-Fetch-Dest":"document","Referer":"https://www.zgqingyang.gov.cn/s?sid=0&wd=%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f%20%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0&p=59&vc=","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"4hP44ZykCTt5S=60ESf7Ivp0kWRaMlurfICu7BpGrAIHrUfEQYSlJ184DxLvn6TrKcTyZx0oyz8Z.LByIp2cI_YS_Fxs8LgL8ku98a; _gscu_1155815754=198266081q03zd34; HWWAFSESID=8cad4a02beb23e40be; HWWAFSESTIME=1720850772852; Power::SiteUniqueVisitorKey=/1/; __RequestVerificationToken=b5Ioarsn3ry_6ghjaF9TCV18XIbbl5RZXMxWCWpQ_Aejo2k_tQezPxGxlENxZC4KFbAXxA2; showGuide=true; _gscbrs_1155815754=1; ASP.NET_SessionId=igu4bpnkusier4adjgmfxnfh; _gscs_1155815754=20850778sml7jt21|pv:12"}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()

