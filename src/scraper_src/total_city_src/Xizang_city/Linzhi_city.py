from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '林芝市',
        'province_name': '西藏省',
        'province': 'Xizang',
        'base_url': 'https://zs.kaipuyun.cn/s?searchWord=%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&column=%25E5%2585%25A8%25E9%2583%25A8&pageSize=10&pageNum={page_num}&siteCode=5426000013&sonSiteCode=&checkHandle=1&searchSource=0&areaSearchFlag=0&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex=&isSecondSearch=undefined&manualWord=%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=0',

        'total_news_num': 34,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[2]/div/div[1]/div',
                     'title': 'x://div/a',
                     'date': ['x://div[2]/div/p[2]/span'],
                     'url': 'x://a[1]'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"5421000007=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oA==; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; HWWAFSESID=81cc173361d078f575; HWWAFSESTIME=1720194922947; 5426000013=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oA==; JSESSIONID=FE842D944D0FB54EEAEB1FD1D0D74B02; SECKEY_ABVK=dXJHfrf9KF5oT+Q40vG1nKEGHfQCKszyHc0ADfCg8kk%3D; userSearch=siteCode-5426000013&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240705235551&searchUseTime-375; BMAP_SECKEY=Z1ROGlRy-zdYROkyYNTEakIctNyq0Z7UZky4hg7z0e5rbwFp33UbDmUFYvOFPHwMgxoWLgWjypWrVAtQTzts68HGgkw52ORH63zqv2auG9LVwBUOn5d6asp0JDazUz283mMMN_6dhXv6g83p7x9SI4YsaWzrMTJlZa6s1vxBNFRMWfz3ZkfeNOPvRVWnJS92","Host":"zs.kaipuyun.cn","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      page_num_start=0)
    scraper.run()
