from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_code': 317,
        'city_name': '西双版纳傣族自治州',
        'province_name': '云南省',
        'province': '云南省',

        'base_url': 'https://www.xsbn.gov.cn/customhc.news.search.dhtml',

        'total_news_num': 4338,
        'each_page_news_num': 12,
    }

    content_xpath = {'frames': 'x://*[@class="col-md-6"]/div',
                     'title': 'x://div[1]/div/a',
                     'date': ['x://span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
               "Cache-Control":"max-age=0","Connection":"keep-alive","Content-Length":"250","Content-Type":"application/x-www-form-urlencoded",
               "Cookie": "arialoadData=false; Secure; Hm_lvt_a2b5dcee7b7b7ea90e0916ee1bc7af99=1730481561,1730539175; HMACCOUNT=3DE9BC176CD975E6; name=value; JSESSIONID=A46F8F3162045B053AE549DB112DD067; Hm_lpvt_a2b5dcee7b7b7ea90e0916ee1bc7af99=1730539459",
               "Origin":"https://www.xsbn.gov.cn",
               "Referer":"https://www.xsbn.gov.cn/",
               "Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = 'keyname=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&number_size=12&siteId=&blockId=&page=2&queryScope=title&sort=score&timeRangeStart=&timeRangeEnd='

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    page_num_name = 'page'

    scraper = Scraper(city_info, method='post', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      verify=False, proxies=fiddler_proxies, post_data=post_data,
                      page_num_name=page_num_name
                      )
    scraper.run()