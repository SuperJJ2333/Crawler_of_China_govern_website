from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '新余市',
        'province_name': '江西省',
        'province': 'Jiangxi',

        'base_url': 'http://www.xinyu.gov.cn/search4/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&column=%25E5%2585%25A8%25E9%2583%25A8&pageSize=10&pageNum={page_num}&siteCode=3605000002&sonSiteCode=&checkHandle=1&searchSource=0&areaSearchFlag=0&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex=&isSecondSearch=undefined&manualWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=1',


        'total_news_num': 317,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': "x://div[@class='wordGuide Residence-permit']",
                     'title': 'x://div[1]/a',
                     'date': ['x://div[2]/div/p[2]/span', 'x://div[2]/div[2]/p/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"proName=search4/; firstWord=%u5B66%u4E60%u8003%u5BDF; userSearch=siteCode-3605000002&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240703170511&searchUseTime-440; SECKEY_ABVK=HYb3JD1UOa4nn9D2DnvzLseY8HJwy8SbctFAy0mUaRA%3D; _yfxkpy_ssid_10008935=%7B%22_yfxkpy_firsttime%22%3A%221719997443490%22%2C%22_yfxkpy_lasttime%22%3A%221719997443490%22%2C%22_yfxkpy_visittime%22%3A%221719997443490%22%2C%22_yfxkpy_domidgroup%22%3A%221719997443490%22%2C%22_yfxkpy_domallsize%22%3A%22100%22%2C%22_yfxkpy_cookie%22%3A%2220240703170403492631072252493235%22%7D; Hm_lvt_51710e264808f8ef475cc8f492e3f3bb=1719997444; Hm_lpvt_51710e264808f8ef475cc8f492e3f3bb=1719997444; arialoadData=true; ariawapChangeViewPort=true; HWWAFSESID=a74d473f197babe08b; HWWAFSESTIME=1719997489891; JSESSIONID=EFF7F68DE8E56CA2554818C496372E88; 3605000002=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oCzlrabkuaDogIPlr58=","Host":"www.xinyu.gov.cn","Proxy-Connection":"keep-alive","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()