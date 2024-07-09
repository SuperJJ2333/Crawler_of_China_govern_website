from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_name': '宣城市',
        'province_name': '安徽省',
        'province': 'Anhui',
        'base_url': 'https://search.xuancheng.gov.cn/searchData?keyword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&field=title&page={page_num}',

        'total_news_num': 792,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="ui-view"]/div/ul/li',
                     'title': 'x://h1/a',
                     'date': ['xpath://p[2]/span[2]',
                              'xpath://li[2]/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"Hm_lvt_96da6bb9c6240d1fcc3e26827fb60319=1719756414; SearchHistory=+%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0+'+%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f+%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0+'+%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f+; SearchLog=%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0%2f04052e98dba04244aed59ac01fac3324'%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f+%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0%2f600b6f95bc364829b512f0be5e261059'%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f%2fbce2b6c77353460ab7863151df462c70; Hm_lpvt_96da6bb9c6240d1fcc3e26827fb60319=1719756469","Host":"search.xuancheng.gov.cn","Referer":"https://search.xuancheng.gov.cn/searchData?keyword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&field=title&page=1","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()
