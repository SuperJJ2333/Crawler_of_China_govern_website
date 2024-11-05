from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_code': 307,
        'city_name': '湘西土家族苗族自治州',
        'province_name': '湖南省',
        'province': '湖南省',
        'base_url': 'https://searching.hunan.gov.cn/hunan/984101000/news?q=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchfields=&sm=&columnCN=&iszq=&aggr_iszq=&p={page_num}&timetype=',

        'total_news_num': 7945,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="hits"]/li',
                     'title': 'x://div/div/a',
                     'date': ['xpath://div[2]/div/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"hunanId=1012334123877224448; AlteonP-8083=AKAxY2WfFgrWbXFl9vt+Ow$$","Host":"searching.hunan.gov.cn","Referer":"https://searching.hunan.gov.cn/hunan/984101000/news?q=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchfields=&sm=&columnCN=&iszq=&aggr_iszq=&p=1&timetype=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False, page_num_start=0)
    scraper.run()