from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_code': 323,
        'city_name': '甘南藏族自治州',
        'province_name': '甘肃省',
        'province': '甘肃省',

        'base_url': 'http://www.gnzrmzf.gov.cn/gjsous.jsp?wbtreeid=1001&keyword=5a2m5Lmg6ICD5a%2BfIOiAg%2BWvn%2BWtpuS5oA%3D%3D&cc=W10%3D&ot=1&rg=4&tg=5&clid=0&currentnum={page_num}',
        'total_news_num': 1717,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*/div[@class="xwd"]',
                     'title': 'x://div[1]/a',
                     'date': ['xpath://div[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=1300315BDE86E91D9A8B6D06050495C8; coverlanguage_bb=0","Host":"www.gnzrmzf.gov.cn","Referer":"http://www.gnzrmzf.gov.cn/gjsous.jsp?wbtreeid=1001","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()