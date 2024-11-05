from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_code': 325,
        'city_name': '海西蒙古族藏族自治州',
        'province_name': '青海省',
        'province': '青海省',

        'base_url': 'https://www.haixi.gov.cn/zsgkml/hhjs.jsp?wbtreeid=1001&keyword=6ICD5a%2Bf5a2m5Lmg&cc=W10%3D&ot=1&rg=4&tg=5&clid=0&currentnum={page_num}',
        'total_news_num': 101,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="zwgkbg"]//div[@class="xwd"]',
                     'title': 'x://div[1]/a',
                     'date': ['xpath://div[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=FB661280FA876670CFB23D4DAC85A4F7; TS01d09d05=0193150fa3054f1e58fb13405f6c9b2dd53461694c1b948daf20ec22dfeb6902d85ecc4219cceb784c5c1c248525bf0dfc56326d0d","Host":"www.haixi.gov.cn","Referer":"https://www.haixi.gov.cn/zsgkml/hhjs.jsp?wbtreeid=1001","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()