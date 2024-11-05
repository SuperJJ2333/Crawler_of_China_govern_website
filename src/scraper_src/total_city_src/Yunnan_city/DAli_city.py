from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_code': 318,
        'city_name': '大理白族自治州',
        'province_name': '云南省',
        'province': '云南省',

        'base_url': 'https://www.dali.gov.cn/search4/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&column=%25E6%259C%25AC%25E7%25AB%2599&pageSize=10&pageNum={page_num}&siteCode=5329000057&sonSiteCode=&checkHandle=1&searchSource=0&areaSearchFlag=0&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index=0&searchBoxSettingsIndex=&isSecondSearch=undefined&manualWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=1',

        'total_news_num': 30,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@class="wordGuide Residence-permit"]',
                     'title': 'x://div[1]/a',
                     'date': ['xpath://div[2]/div/p[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; proName=search4/; userSearch=siteCode-5329000057&column-%E6%9C%AC%E7%AB%99&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20241102173326&searchUseTime-256; nS_wcI_5f=v73h9X7arWzQoLXGytgXtTbh7WxvZPj0O5ZLBA==; _yfxkpy_ssid_10005788=%7B%22_yfxkpy_firsttime%22%3A%221730539959929%22%2C%22_yfxkpy_lasttime%22%3A%221730539959929%22%2C%22_yfxkpy_visittime%22%3A%221730539959929%22%2C%22_yfxkpy_cookie%22%3A%2220241102173239930359192258659625%22%7D; arialoadData=true; ariawapChangeViewPort=false; HWWAFSESID=8a0ef7302977433354; HWWAFSESTIME=1730539962490; yfx_c_g_u_id_10000001=_ck24110217324410675381524407477; yfx_f_l_v_t_10000001=f_t_1730539964062__r_t_1730539964062__v_t_1730539964062__r_c_0; 5329000057=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oCzlrabkuaDogIPlr58=; JSESSIONID=47A18D8B53CD88E4FA472ADB117AF0A6; nS_wSI_5f=HeoQifEQ1CUvit3sFAsmOLd88biQ8yVnPg09ZA==","Host":"www.dali.gov.cn","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()