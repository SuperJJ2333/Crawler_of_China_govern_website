from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '商洛市',
        'province_name': '陕西省',
        'province': 'Shannxi',

        'base_url': 'https://www.shangluo.gov.cn/a_ssjgy3.jsp?wbtreeid=1001&keyword=6ICD5a%2Bf5a2m5Lmg&ot=1&rg=2&tg=5&clid=0&currentnum={page_num}',

        'total_news_num': 137,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="text_list"]/ul/div[2]/div',
                     'title': 'x://div/a',
                     'date': ['x://div[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","Accept-Encoding":"gzip, deflate, br, zstd","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","accept-charset":"GB2312,utf-8;q=0.7,*;q=0.7","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Content-Type":"application/x-www-form-urlencoded","Cookie":"JSESSIONID=6C83E9FAFD356523D246564201C5BB2B.vsb_sl; coverlanguage_bb=0","Host":"www.shangluo.gov.cn","Origin":"https://www.shangluo.gov.cn","Referer":"https://www.shangluo.gov.cn/a_ssjgy3.jsp?wbtreeid=1001","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = 'cc=%5B%5D'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post_change', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      verify=False, proxies=fiddler_proxies, post_data=post_data,
                      )
    scraper.run()