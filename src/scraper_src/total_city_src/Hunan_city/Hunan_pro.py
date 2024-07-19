from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '长沙市',
        'province_name': '湖南省',
        'province': 'Hunan',

        'base_url': 'https://searching.hunan.gov.cn/hunan/{city_code}/news?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchfields=title&sm=0&columnCN=&iszq=&aggr_iszq=&p={page_num}&timetype=timeqb',

        'total_news_num': 1000,

        'each_page_news_num': 10,
    }

    base_url = 'https://searching.hunan.gov.cn/hunan/{city_code}/news?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchfields=&sm=0&columnCN=&iszq=&aggr_iszq=&p={page_num}&timetype=timeqb'

    content_xpath = {'frames': 'x://*[@id="hits"]/li',
                     'title': 'x://div/div/a',
                     'date': ['x://div[2]/div/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\""}

    city_code = {
        # '岳阳市': [976000000, 15301], '永州市': [981101000, 10368],
        #          '株洲市': [973000000, 1901],
        '郴州市': [980000000, 21050],
        # '湘潭市': [974000000, 1847],
        '娄底市': [983101000, 4999],
        # '怀化市': [982001000, 30547], '常德市': [977001000, 17683],
        #          '邵阳市': [975101000, 12701],
        # '益阳市': [979000000, 12558], '张家界市': [978101000, 25409],
        #          '衡阳市': [972101000, 47480], '长沙市': [971101000, 1801],
    }

    for city_name, code in city_code.items():
        city_info['city_name'] = city_name
        city_info['total_news_num'] = code[1]

        city_info['base_url'] = base_url.format(city_code=code[0], page_num='{page_num}')

        scraper = Scraper(city_info, method='get', data_type='html',
                          content_xpath=content_xpath, headers=headers, is_headless=False, page_num_start=0,
                          thread_num=1)
        scraper.run()
