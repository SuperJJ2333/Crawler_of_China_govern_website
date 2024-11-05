import json

from scraper.scraper import Scraper


if __name__ == '__main__':
    """
    请求方法：LISTEN
    获取数据：API
    提取方法：JSON -- data -- dataList -- xq_title, xq_pudate, xq_url
    """

    city_info = {
        'city_code': 329,
        'city_name': '玉树藏族自治州',
        'province_name': '青海省',
        'province': '青海省',

        'base_url': 'http://110.166.69.34:8808/mcms/search.do',
        'total_news_num': 2,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="searchcontainer"]/ul/li',
                     'title': 'x://span/a',
                     'date': ['x://span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Content-Length":"82","Content-Type":"application/x-www-form-urlencoded","Cookie":"wza-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; GOV_SHIRO_SESSION_ID=8a47d900-ca90-4e59-b852-1da11e7b7a23","Host":"110.166.69.34:8808","Origin":"http://110.166.69.34:8808","Proxy-Connection":"keep-alive","Referer":"http://110.166.69.34:8808/mcms/search.do","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}

    post_data = 'style=yushu-gov&tmpl=search.htm&content_title=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    page_num_name = 'page'

    scraper = Scraper(city_info, method='post', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      verify=False, proxies=fiddler_proxies, post_data=post_data,
                      page_num_name=page_num_name
                      )
    scraper.run()