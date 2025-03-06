from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '三亚市',
        'province_name': '海南省',
        'province': 'Hainan',
        'base_url': 'https://search.sanya.gov.cn/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&column=%25E5%2585%25A8%25E7%25AB%2599&pageSize=10&pageNum={page_num}&siteCode=4602000035&sonSiteCode=&checkHandle=1&searchSource=0&areaSearchFlag=0&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex=&isSecondSearch=undefined&manualWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=1',


        'total_news_num': 317,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://body/div[2]/div/div/div',
                     'title': 'x://div[1]/a',
                     'date': ['x://div[2]/div[2]/p[2]/span', 'x://div[2]/div/p/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"_gscu_987887131=19837775xslq3l13; _gscbrs_987887131=1; _gscs_987887131=19837775dw70un13|pv:1; Hm_lvt_27c50e3b66fcc41c9b249a5a8c7e3dba=1719837788; Hm_lpvt_27c50e3b66fcc41c9b249a5a8c7e3dba=1719837788; Hm_lvt_db413f01b29d57c4ef867a316f0f5d04=1719837788; Hm_lpvt_db413f01b29d57c4ef867a316f0f5d04=1719837788; arialoadData=false; 4602000035=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oA==; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; userSearch=siteCode-4602000035&column-%E5%85%A8%E7%AB%99&uc-1&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240701204312&searchUseTime-372; SECKEY_ABVK=ronpiFc8YLl9QEEwQ/xDFNKLmgNueViZbj4p9136C1pf7ZZ/zzGAzWZ+by1T6gLo5WHXrVsJVY9nJYBTuUDDmA%3D%3D","Host":"search.sanya.gov.cn","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True, page_num_start=0)
    scraper.run()