from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '池州市',
        'province_name': '安徽省',
        'province': '安徽省',
        'base_url': 'https://search.chizhou.gov.cn/searchData?collection=&Field=title&siteGroupId=1&keyword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&page={page_num}',
        'total_news_num': 555,

        'each_page_news_num': 15,
        'city_code': 107,
    }

    content_xpath = {'frames': 'x://*/div[3]/div[1]/div[1]/ul/li',
                     'title': 'x://a',
                     'date': ['xpath://div[2]/p[3]',
                              'xpath://li[2]/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", "Connection": "keep-alive",
        "Cookie": "Hm_lvt_88d3314545011934a215cb84e7dcbaa7=1716373541; SearchHistory=+%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0+'+%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f+%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0+'+%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f+",
        "Host": "search.chizhou.gov.cn",
        "Referer": "https://search.chizhou.gov.cn/searchData?collection=&Field=title&siteGroupId=1&keyword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0",
        "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()
