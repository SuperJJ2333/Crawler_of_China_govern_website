from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '日喀则市',
        'province_name': '西藏省',
        'province': 'Xizang',
        'base_url': 'http://www.rikaze.gov.cn/search-page.thtml?page={page_num}&searchModelId=&keyword=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&classId=',


        'total_news_num': 4171,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/section/div/div[2]/div/div[2]/div[1]/div[2]/ul/li',
                     'title': 'x://a[1]/h2',
                     'date': ['x://a/p/span[2]'],
                     'url': 'x://a[1]'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Host":"www.rikaze.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.rikaze.gov.cn/search-page.thtml?page=1&searchModelId=&keyword=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()