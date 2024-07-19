from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '邢台市',
        'province_name': '河北省',
        'province': 'Hebei',
        'base_url': 'http://www.xingtai.gov.cn/was5/web/search?page={page_num}&channelid=234439&searchword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&keyword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&orderby=-DOCRELTIME&perpage=10&outlinepage=10&andsen=&total=&orsen=&exclude=&searchscope=&timescope=&timescopecolumn=&orderby=-DOCRELTIME',

        'total_news_num': 238,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body//dl',
                     'title': 'x://dt/a',
                     'date': ['x://p[1]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"JSESSIONID=44D6881AFE1242F3003DBC4D0AF90E8C; security_session_verify=c52c7459d4fe0444f6e46de491b6b9a0","Host":"www.xingtai.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.xingtai.gov.cn/was5/web/search?page=4&channelid=234439&searchword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&keyword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&orderby=-DOCRELTIME&perpage=10&outlinepage=10&andsen=&total=&orsen=&exclude=&searchscope=&timescope=&timescopecolumn=&orderby=-DOCRELTIME","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()