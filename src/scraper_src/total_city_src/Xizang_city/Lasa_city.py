from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '拉萨市',
        'province_name': '西藏省',
        'province': 'Xizang',
        'base_url': 'http://sousuo.www.lasa.gov.cn/search4/s?searchWord=%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&column=%25E6%259C%25AC%25E7%25AB%2599&pageSize=10&pageNum={page_num}&siteCode=5401000001&sonSiteCode=&checkHandle=1&searchSource=0&areaSearchFlag=0&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex=&isSecondSearch=undefined&manualWord=%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=0',


        'total_news_num': 78,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[2]/div/div[1]/div',
                     'title': 'x://div/a',
                     'date': ['x://div[2]/div/p[2]/span'],
                     'url': 'x://a[1]'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"proName=search4/; firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; SECKEY_ABVK=dXJHfrf9KF5oT+Q40vG1nLP/2I7KX+x9yxOielkcBag%3D; userSearch=siteCode-5401000001&column-%E6%9C%AC%E7%AB%99&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240705230343&searchUseTime-4942; arialoadData=true; ariawapChangeViewPort=false; 5401000001=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oA==; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; JSESSIONID=CD2ADBF86790A5068056B06906B1D077","Host":"sousuo.www.lasa.gov.cn","Proxy-Connection":"keep-alive","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      page_num_start=0)
    scraper.run()
