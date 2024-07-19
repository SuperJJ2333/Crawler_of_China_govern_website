from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '乌海市',
        'province_name': '内蒙古省',
        'province': 'Neimenggu',

        'base_url': 'http://www.wuhai.gov.cn/search/pcRender?pageId=63493493b61047b8be9bc396fa236e60',

        'total_news_num': 950,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="panel-page"]/div/div[2]/div[2]/div',
                     'title': 'x://div/h3/a',
                     'date': ['x://div/div/p[2]/span'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Connection":"keep-alive","Content-Length":"565","Content-Type":"application/x-www-form-urlencoded","Cookie":"AMJ-VISIT=\"B407A486B18B4342945FFA33A8E8498C,8A3BCFBC76FFC30B4228A0B798FC0281,1720182079000\"; JSESSIONID=8A3BCFBC76FFC30B4228A0B798FC0281; _gscu_1831468369=201792847y5fgw39; _gscbrs_1831468369=1; _gscs_1831468369=20182077j2zsfd39|pv:9","Host":"www.wuhai.gov.cn","Origin":"http://www.wuhai.gov.cn","Referer":"http://www.wuhai.gov.cn/search/pcRender?pageId=63493493b61047b8be9bc396fa236e60","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = {'originalSearchUrl': '/search/pcRender?pageId=63493493b61047b8be9bc396fa236e60', 'originalSearch': '', 'app': 'e0f5bd4c17f64784a4e8ea47a25bbb27,2d2145bfde734f20b3a746f5040a2752,b46547d5770e4c1794e9a337836ba34d,ab217b6d91d64085bd05924b218abbc8,4536d378b2a843d79ad0cbb2d5433ce1,fcff548c7a114dd3b3970d3866191820,57cddb86829c4d1e83ceed3c85dc4942', 'appName': '', 'sr': 'score desc', 'advtime': '', 'advrange': '', 'ext': 'siteId:1862', 'pNo': '4', 'searchArea': '', 'advepq': '', 'advoq': '', 'adveq': '', 'advSiteArea': '', 'q': '学习考察 考察学习'}

    page_num_name = 'pNo'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      verify=False, proxies=fiddler_proxies, post_data=post_data, page_num_name=page_num_name
                      )
    scraper.run()