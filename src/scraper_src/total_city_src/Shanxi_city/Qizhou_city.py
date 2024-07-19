from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '忻州市',
        'province_name': '山西省',
        'province': 'Shanxi',

        'base_url': 'https://www.sxxz.gov.cn/was5/web/search?searchscope=&timescope=&timescopecolumn=&orderby=&channelid=260481&andsen=&total=&orsen=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&exclude=&lanmu=&page={page_num}&searchword=&perpage=&token=&templet=',

        'total_news_num': 116,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[1]/div[2]/div[3]/dl',
                     'title': 'x://dt/a',
                     'date': ['x://dd/div[1]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=FD9D98D322A65851F796DCC49027943F; Hm_lvt_2d96809ecdf940120aa7ecb1b5562f6c=1720112924; HMACCOUNT=A202F23FD4E0D795; arialoadData=true; ariawapChangeViewPort=false; Hm_lpvt_2d96809ecdf940120aa7ecb1b5562f6c=1720112978","Host":"www.sxxz.gov.cn","Referer":"https://www.sxxz.gov.cn/was5/web/search?searchscope=&timescope=&timescopecolumn=&orderby=&channelid=260481&andsen=&total=&orsen=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&exclude=&lanmu=&page=2&searchword=&perpage=&token=&templet=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()