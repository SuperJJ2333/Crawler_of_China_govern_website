from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '宜昌市',
        'province_name': '河南省',
        'province': 'Hubei',

        'base_url': 'http://so.yichang.gov.cn/so/search',

        'total_news_num': 24,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="main"]/div/div[2]/div[1]/div',
                     'title': 'x://div[1]/a',
                     'date': ['x://div[2]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Connection":"keep-alive","Content-Length":"137","Content-Type":"application/x-www-form-urlencoded","Cookie":"Hm_lvt_4ae480935d61ee0ea0a491a5215a50f2=1720962112; Hm_lpvt_4ae480935d61ee0ea0a491a5215a50f2=1720962112; HMACCOUNT=A202F23FD4E0D795; sl-session=erkQctUdlWZr+kZf26YMrA==; _gscu_1720901129=20962132kd6adi13; _gscbrs_1720901129=1; _gscs_1720901129=20962132wvtrie13|pv:5","Host":"so.yichang.gov.cn","Origin":"http://so.yichang.gov.cn","Referer":"http://so.yichang.gov.cn/so/search","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = {'key': '考察学习', 'depid': '0', 'sourcefrom': 'ALL', 'interval': 'ALL', 'begintime': '', 'endtime': '', 'sortrule': 'SCORE', 'searchtype': 'CONTENT', 'page': '3'}

    page_num_name = 'page'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      verify=False, proxies=fiddler_proxies, post_data=post_data,
                      page_num_name=page_num_name
                      )
    scraper.run()