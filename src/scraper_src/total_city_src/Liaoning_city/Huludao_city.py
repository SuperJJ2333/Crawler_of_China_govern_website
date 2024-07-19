from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '葫芦岛市',
        'province_name': '辽宁省',
        'province': 'Liaoning',
        'base_url': 'http://search.hld.gov.cn/was5/web/search?page={page_num}&channelid=211543&searchword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&keyword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&orderby=-DOCRELTIME&StringEncoding=UTF-8&perpage=10&outlinepage=10&searchscope=&timescope=&timescopecolumn=&orderby=-DOCRELTIME&andsen=&total=&orsen=&exclude=',

        'total_news_num': 5000,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[3]/div/div[2]/div[1]/ul/li',
                     'title': 'x://p[1]/a',
                     'date': ['x://p[3]/text()'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"JSESSIONID=89BF6841293A86A6C27C1B58AE858895","Host":"search.hld.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://search.hld.gov.cn/was5/web/search?page=1&channelid=211543&searchword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&orderby=-DOCRELTIME&StringEncoding=UTF-8&perpage=10&outlinepage=10&searchscope=&timescope=&timescopecolumn=&orderby=-DOCRELTIME&andsen=&total=&orsen=&exclude=","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()