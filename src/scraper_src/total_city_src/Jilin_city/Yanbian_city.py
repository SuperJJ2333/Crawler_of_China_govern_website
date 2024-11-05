from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_code': 303,
        'city_name': '延边朝鲜族自治州',
        'province_name': '吉林省',
        'province': '吉林省',

        'base_url': 'http://111.26.49.117:8082/was5/web/search?page={page_num}&channelid=230770&searchword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&perpage=10&outlinepage=10',

        'total_news_num': 29,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://ul[@class="write_list"]/li',
                     'title': 'x://a/div[2]/div',
                     'date': ['xpath://a/div[1]'],
                     'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=260F3CC21AA5D43C5008B061D335F402","Host":"111.26.49.117:8082","Referer":"http://111.26.49.117:8082/was5/web/search?channelid=230770&searchword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()