from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '湖南省',
        'province_name': '湖南省',
        'province': 'province_web_data',
        'base_url': 'https://searching.hunan.gov.cn/hunan/001000000/news?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchfields=title&sm=0&columnCN=&iszq=&aggr_iszq=&p={page_num}&timetype=timeqb',

        'total_news_num': 6602,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="hits"]/li',
                     'title': 'x://div/div/a',
                     'date': ['x://div[2]/div/span[2]/text()'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"hunanId=968002454609547264; uid=ChW0mGaDnVd5maltmp80Ag==; AlteonP-8083=ALJXIWWfFgojMg8eKZ26Lw$$","Host":"searching.hunan.gov.cn","Referer":"https://searching.hunan.gov.cn/hunan/001000000/news?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&sm=0&searchfields=title&timetype=timeqb&websiteName=&channelName=&whlx=&publishedYear=&site_name=&org_name2=&iszq=&aggr_iszq=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      page_num_start=0)
    scraper.run()