from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '沧州市',
        'province_name': '河北省',
        'province': 'Hebei',
        'base_url': 'https://www.cangzhou.gov.cn/guestweb4/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&column=%25E5%2585%25A8%25E9%2583%25A8&wordPlace=1&orderBy=0&startTime=&endTime=&pageSize=10&pageNum={page_num}&timeStamp=0&siteCode=1309000040&sonSiteCode=&checkHandle=1&strFileType=&govWorkBean=%257B%257D&sonSiteCode=&areaSearchFlag=0&secondSearchWords=&topical=&pubName=&countKey=0&uc=0&left_right_index=0',

        'total_news_num': 6964,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[3]/div[1]/div',
                     'title': 'x://div[1]/a',
                     'date': ['x://div[2]/div/p[2]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"Path=/; firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; userSearch=siteCode-1309000040&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240714012143&searchUseTime-6; HWWAFSESID=faa1a7312f41df1b02; HWWAFSESTIME=1720885923936; Path=/; yfx_c_g_u_id_10000002=_ck24071323542018715906166607152; yfx_f_l_v_t_10000002=f_t_1720886060873__r_t_1720886060873__v_t_1720886060873__r_c_0; yfx_mr_10000002=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_mr_f_10000002=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_key_10000002=","Host":"www.cangzhou.gov.cn","Referer":"https://www.cangzhou.gov.cn/guestweb4/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&column=%25E5%2585%25A8%25E9%2583%25A8&wordPlace=1&orderBy=0&startTime=&endTime=&pageSize=10&pageNum=0&timeStamp=0&siteCode=1309000040&sonSiteCode=&checkHandle=1&strFileType=&govWorkBean=%257B%257D&sonSiteCode=&areaSearchFlag=0&secondSearchWords=&topical=&pubName=&countKey=0&uc=0&left_right_index=0","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()