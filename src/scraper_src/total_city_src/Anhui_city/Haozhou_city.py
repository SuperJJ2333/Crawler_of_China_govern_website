from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '亳州市',
        'province_name': '安徽省',
        'province': '安徽省',
        'base_url': 'https://search.bozhou.gov.cn/searchData?keyword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&field=all&page={page_num}',
        # 新闻总数
        # 'total_news_num': 24,
        'total_news_num': 1448,

        'each_page_news_num': 15,
    }

    content_xpath = {'frames': 'x://body/div[3]/div[2]/div/section[1]/div[1]/ul/li',
                     'title': 'x://a/h1/text()',
                     'date': ['x://div[2]/p[2]'],
                     'url': 'x://a',
                     'next_button': 'x://a[contains(text(),"下页")]',
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"SearchHistory=+%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0+'+%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f+%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0+'+%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f+; SearchLog=%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0%2f5ba1b9adf7e44c368e96bbf1df2c940c'%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f+%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0%2fc081a67639f2419e8237b9c80f7f2c28'%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f%2f0d3f7ede812942659bd291cdd4c069e9; wzws_sessionid=gTVmNDU5MYAxMjAuMjM2LjE2My4xMTCgZpE1qoJkZWRmOGQ=; arialoadData=true","Host":"search.bozhou.gov.cn","Referer":"https://search.bozhou.gov.cn/searchData?keyword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&field=all&page=2","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='listen', data_type='html',
                      content_xpath=content_xpath, is_headless=True)

    scraper.method_LISTEN()
    scraper.save_files()
