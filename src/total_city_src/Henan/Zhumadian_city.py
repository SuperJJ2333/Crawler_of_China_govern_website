from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_name': '驻马店市',
        'province_name': '河南省',
        'province': 'Henan',

        'base_url': 'https://www.zhumadian.gov.cn/plus/seek/index.php?currpage={page_num}&pagesize=20&skey=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F',

        'total_news_num': 23,

        'each_page_news_num': 20,
    }

    content_xpath = {'frames': 'x:/html/body/div[2]/div[3]/div',
                     'title': 'x://a',
                     'date': ['xpath:../div/text()'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; Hm_lvt_7b83a411615ae3b2830482befdd9c41f=1719855774; __51huid__KRBJH09Q0bR4rTzP=421ad881-745a-58ee-a6bc-e73b64fa4d1f; PHPSESSID=nqhif14uav57olj8o6lsqvcbe1; Hm_lpvt_7b83a411615ae3b2830482befdd9c41f=1719855853","Host":"www.zhumadian.gov.cn","Referer":"https://www.zhumadian.gov.cn/plus/seek/index.php","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()