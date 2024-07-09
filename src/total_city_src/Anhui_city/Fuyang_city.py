from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '阜阳市',
        'province_name': '安徽省',
        'province': 'Anhui',
        'base_url': 'https://www.fy.gov.cn/index.php?c=search&site_id=543740479a05c26f4be2861a&type=&keywords=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&sort=&field=title&forceSearch=&wrongSearch=&page={page_num}',

        # 新闻总数
        'total_news_num': 72,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="search-result"]/div',
                     'title': 'x://h3/a',
                     'date': ['x://span[3]']
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"wzws_sessionid=gjViMTBhY4AyMjEuNC4zMi4yNKBmgADhgTVmNDU5MQ==; FYSESSID=l0pentiue2katu5igje36a9vs0; Hm_lvt_47f0853208dd4de1ee348e52899781d0=1717656926,1719664866; arialoadData=false; history=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0+%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; wzws_cid=bcb08a7dd60df3215266c3e31a97ef89d5e724c773537750922bf940f54fad881c7df84b81ec283cabd148b69d7875b606cb3f5e6acd87bbefef9c012e029a16b85c4edc1c2a4296f9dd96c3a4887f43; Hm_lpvt_47f0853208dd4de1ee348e52899781d0=1719664937","Host":"www.fy.gov.cn","Referer":"https://www.fy.gov.cn/index.php?c=search&site_id=543740479a05c26f4be2861a&type=&keywords=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&sort=&field=title&forceSearch=&wrongSearch=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()
