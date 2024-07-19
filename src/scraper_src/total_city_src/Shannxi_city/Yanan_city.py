from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '延安市',
        'province_name': '陕西省',
        'province': 'Shannxi',

        'base_url': 'http://www.yanan.gov.cn/search.html?keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&size=15&tab=all&isAll=1&page={page_num}&scope=title,mc_listtitle',

        'total_news_num': 1019,

        'each_page_news_num': 15,
    }

    content_xpath = {'frames': 'x:/html/body/div[5]/div[1]/div/div[11]/ul/li',
                     'title': 'x://div/div/div/a',
                     'date': ['x://div/div[3]/span[1]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"zh_choose=s; Hm_lvt_c12d8745147100fd4bb3065c824a3e62=1720116328; HMACCOUNT=A202F23FD4E0D795; Hm_lpvt_c12d8745147100fd4bb3065c824a3e62=1720116765","Host":"www.yanan.gov.cn","Referer":"http://www.yanan.gov.cn/search.html?keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&size=15&tab=all&page=2&scope=title,mc_listtitle","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()