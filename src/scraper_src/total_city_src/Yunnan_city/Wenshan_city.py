from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_code': 316,
        'city_name': '文山壮族苗族自治州',
        'province_name': '云南省',
        'province': '云南省',
        'base_url': 'https://www.ynws.gov.cn/news/search.jsp?wbtreeid=1001&searchScope=1&currentnum={page_num}&newskeycode2=5a2m5Lmg6ICD5a%2BfIOiAg%2BWvn%2BWtpuS5oA%3D%3D',
        'total_news_num': 2190,

        'each_page_news_num': 20,
    }

    content_xpath = {'frames': 'x://ul[@class="list"]/li',
                     'title': 'x://a',
                     'date': ['xpath://span[1]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=838B5F5A99742303B0CA90A7E03FB4EB","Host":"www.ynws.gov.cn","Referer":"https://www.ynws.gov.cn/news/search.jsp?wbtreeid=1001","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()