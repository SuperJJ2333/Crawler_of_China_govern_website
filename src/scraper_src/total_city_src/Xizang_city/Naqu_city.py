from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '那曲市',
        'province_name': '西藏省',
        'province': 'Xizang',
        'base_url': 'http://www.naqu.gov.cn/guestweb4/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F&column=%25E6%259C%25AC%25E7%25AB%2599&pageSize=10&pageNum={page_num}&siteCode=5424000010&sonSiteCode=&checkHandle=1&searchSource=0&govWorkBean=%257B%257D&sonSiteCode=&areaSearchFlag=-1&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex=&manualWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=1',

        'total_news_num': 278,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[2]/div/div[1]/div',
                     'title': 'x://div/a',
                     'date': ['x://div[2]/div/p[2]/span'],
                     'url': 'x://a[1]'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=97CF3A218BF55C20D68F33132F8253A1; firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; userSearch=siteCode-5424000010&column-%E6%9C%AC%E7%AB%99&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&searchTime-20240706033005&searchUseTime-35; SECKEY_ABVK=ronpiFc8YLl9QEEwQ/xDFBAmRNaIQV4LaPpj58z/xFbnnElfZtKUq/DcTTq8an9QbQji9eb5W29iuEy+dc7how%3D%3D; yfx_c_g_u_id_10000002=_ck24070523553910719889575633573; ariaStatus=false; ariacheckAutoFixedBtn=false; arialoadData=false; ariaoldFixedStatus=false; ariawapForceOldFixed=false; yfx_f_l_v_t_10000002=f_t_1720194939069__r_t_1720194939069__v_t_1720207932134__r_c_0; 5424000010=6ICD5a+f5a2m5LmgLOWtpuS5oOiAg+WvnyzlrabkuaDogIPlr58g6ICD5a+f5a2m5Lmg","Host":"www.naqu.gov.cn","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      page_num_start=0)
    scraper.run()
