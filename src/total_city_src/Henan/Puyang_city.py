from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：listen -- GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '濮阳市',
        'province_name': '河南省',
        'province': 'Henan',

        'base_url': 'https://www.puyang.gov.cn/zwxx/zwxx_search.asp?words=%BF%BC%B2%EC%D1%A7%CF%B0&token=1719851856&dtime=1719851853&page={page_num}',
        'total_news_num': 21,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="jsearch-result-items"]/div',
                     'title': 'x://div[1]/a',
                     'date': ['x://div[2]/div[1]/span'],
                     'next_button': 'x://a[contains(text(),"下一页")]',
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"firstname=Alex; puyang=visiter=1719851750; ASPSESSIONIDQADSQCTB=DJEJPPPAMNLEMMFBFHDLDINA; zh_choose=n; toolsInit={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22colortype%22:0%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; __51uvsct__KAOjtYBUtPXuEYsB=1; __51vcke__KAOjtYBUtPXuEYsB=a0a6a1ba-4bc9-5d23-9d28-d3ca09673427; __51vuft__KAOjtYBUtPXuEYsB=1719851752977; security_session_verify=89f09c334985014892fcfdc65b5ff19f; __vtins__KAOjtYBUtPXuEYsB=%7B%22sid%22%3A%20%22e43274f4-6619-58ef-b8b1-6ed9cceefe86%22%2C%20%22vd%22%3A%208%2C%20%22stt%22%3A%20162820%2C%20%22dr%22%3A%204119%2C%20%22expires%22%3A%201719853715793%2C%20%22ct%22%3A%201719851915793%7D","Host":"www.puyang.gov.cn","Referer":"https://www.puyang.gov.cn/zwxx/zwxx_search.asp?words=%BF%BC%B2%EC%D1%A7%CF%B0&token=1719851856&dtime=1719851853&page=1","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}\

    listen_name = 'www.puyang.gov.cn/zwxx/zwxx_search.asp'

    scraper = Scraper(city_info, method='listen', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=False, listen_name=listen_name)

    scraper.method_LISTEN()
    scraper.save_files()
