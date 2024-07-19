from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '双鸭山市',
        'province_name': '黑龙江省',
        'province': 'HeiLongJiang',

        'base_url': 'http://www.syskfq.gov.cn/NewCMS/index/html/search/sousuo.jsp',

        'total_news_num': 1,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[3]/form/ul/li',
                     'title': 'x://h2/a',
                     'date': ['x://p/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Content-Length":"40","Content-Type":"application/x-www-form-urlencoded","Cookie":"JSESSIONID=224CD8D502BEB0619ED9C81BED483893","Host":"www.syskfq.gov.cn","Origin":"http://www.syskfq.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.syskfq.gov.cn/NewCMS/index/html/search/sousuo.jsp","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = {'sel': '学习考察'}

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