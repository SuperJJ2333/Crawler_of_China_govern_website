from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '上饶市',
        'province_name': '江西省',
        'province': 'Jiangxi',

        'base_url': 'https://zs.kaipuyun.cn/search4/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F&column=%25E5%2585%25A8%25E9%2583%25A8&pageSize=10&pageNum={page_num}&siteCode=3611000001&sonSiteCode=&checkHandle=1&searchSource=0&areaSearchFlag=0&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex=&isSecondSearch=undefined&manualWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=0',

        'total_news_num': 708,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://body/div[2]/div/div[1]/div',
                     'title': 'x://div[1]/a',
                     'date': ['x://div[2]/div/p[2]/span', 'x://p/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"proName=search4/; SECKEY_ABVK=ronpiFc8YLl9QEEwQ/xDFOKkjlI+T4u9aYq6hZ8VNw9znWMMoyxUxQxVZX4v5zzG+j+oQlLEHvbC7O+4f9tL0w%3D%3D; firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; userSearch=siteCode-3611000001&column-%E5%85%A8%E9%83%A8&uc-1&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240703174741&searchUseTime-55; BMAP_SECKEY=ronpiFc8YLl9QEEwQ_xDFOKkjlI-T4u9aYq6hZ8VNw-kyACGAwb_Ze598GZrW_QlZzuArs9CU004xV4XyteLs54-_trmcMhZB-5ZSnyzTQVxL00v3yrPlFbe6aovlrBe2hkOmiC8RNJS4pMMhmhEkWqANVGHxyzqIUzWBUBbUyS1wSWLKfi2IbnfESQEskb49UW3ZERnhMIEIWQJjrSoYA; proName=search4/; firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; userSearch=siteCode-3611000001&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord-%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240703174822&searchUseTime-423; SECKEY_ABVK=ronpiFc8YLl9QEEwQ/xDFOKkjlI+T4u9aYq6hZ8VNw/aVNBdvFY0c/pBzpLNrAWlYbJNnbG0FsjBgccSDOOfng%3D%3D; BMAP_SECKEY=ronpiFc8YLl9QEEwQ_xDFOKkjlI-T4u9aYq6hZ8VNw-kyACGAwb_Ze598GZrW_QlE1jeWKIFxIeZmWQsQNGlOQ1EnKLjJkPKnHY7b5WxTOc5h8IGWhYfH7R6YNZbdHIX7sFPN_7mXSBDv7iIBpY1udxoSn3E79XmG61JlNa1Up77lH2BT-dA80mHrk4vWpiH0rx2XbGw2uSQiIhbSFh7wS1yThJ64uVFdhoGl_zB7SM; HWWAFSESID=5d0ea767038c1986d0; HWWAFSESTIME=1720000057734; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; 3611000001=6ICD5a+f5a2m5LmgLOWtpuS5oOiAg+WvnyzlrabkuaDogIPlr58g6ICD5a+f5a2m5Lmg; JSESSIONID=EAD248179E9993D17C12C519DC10CD2A","Host":"zs.kaipuyun.cn","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxy = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True, page_num_start=0,
                      proxies=fiddler_proxy, verify=False)
    scraper.run()
