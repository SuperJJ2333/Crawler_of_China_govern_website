from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_code': 319,
        'city_name': '德宏傣族景颇族自治州',
        'province_name': '云南省',
        'province': '云南省',

        'base_url': 'https://www.dh.gov.cn/search/Web/index.do?page={page_num}&search=%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0',
        'total_news_num': 1350 ,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="hits"]/li',
                     'title': 'x://div[1]/div[1]/a',
                     'date': ['xpath://div[2]/div[1]/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"hrbas_session=sj53ok1eewjgzvfvpwi25tff; arialoadData=false","Host":"www.dh.gov.cn","Referer":"https://www.dh.gov.cn/search/Web/index.do?page=2&search=%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()