from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_name': '邯郸市',
        'province_name': '河北省',
        'province': 'Hebei',
        'base_url': 'https://www.hd.gov.cn/was5/web/search?page={page_num}&channelid=256510&searchword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&keyword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&orderby=RELEVANCE&was_custom_expr=doctitle%3D%28%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%29&perpage=10&outlinepage=10&searchscope=doctitle&timescope=&timescopecolumn=&orderby=RELEVANCE&andsen=&total=&orsen=&exclude=',

        'total_news_num': 100,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="column1"]/div/table//tr/td[2]/ol/li',
                     'title': 'x://div[1]/a',
                     'date': ['xpath://div[3]',
                              'xpath://li[2]/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=945ED281F6F7441597852BCAA096AD22","Host":"www.hd.gov.cn","Referer":"https://www.hd.gov.cn/was5/web/search?page=2&channelid=256510&searchword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&keyword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&orderby=RELEVANCE&was_custom_expr=doctitle%3D%28%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%29&perpage=10&outlinepage=10&searchscope=doctitle&timescope=&timescopecolumn=&orderby=RELEVANCE&andsen=&total=&orsen=&exclude=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()