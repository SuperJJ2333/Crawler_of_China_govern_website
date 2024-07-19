from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '孝感市',
        'province_name': '湖北省',
        'province': 'Hubei',
        'base_url': 'http://www.xiaogan.gov.cn/search_{page_num}.jspx?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&torc=all&orderBy=Correlation',

        'total_news_num': 53089,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="res"]/div[1]/ul/li',
                     'title': 'x://h2/a',
                     'date': ['x://p[2]/a/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"Hm_lvt_d6b6c7f82e14a35f60f4c25b44d895b8=1720266074,1720781264,1720965661; HMACCOUNT=A202F23FD4E0D795; Hm_lvt_e44f7210835046e58582a29167d49099=1720266074,1720781264,1720965661; _site_id_cookie=1; viewTimes=1; _front_site_id_cookie=1; clientlanguage=zh_CN; shrio_sessionid=16f50ec456a542c5bded541de8845ed9; animateKey=1; history=%5B%22%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%22%5D; Hm_lpvt_e44f7210835046e58582a29167d49099=1720965702; Hm_lpvt_d6b6c7f82e14a35f60f4c25b44d895b8=1720965702","Host":"www.xiaogan.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.xiaogan.gov.cn/search.jspx?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&torc=all&orderBy=Correlation","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()