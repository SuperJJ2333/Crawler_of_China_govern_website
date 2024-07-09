from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '聊城市',
        'province_name': '山东省',
        'province': 'Shandong',

        'base_url': 'http://www.liaocheng.gov.cn/search.html?keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&page={page_num}',

        'total_news_num': 95689,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x:/html/body/div[3]/div[2]/div/div[3]/ul/li',
                     'title': 'x://div/div[1]/a[1]',
                     'date': ['x://div/div[2]/span[2]', 'x://div[2]/div[2]/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"yuYin=0; yuYinAccess_token=24.ab9f6f9ef494f72d2124c93c5c7ec7e6.2592000.1722659689.282335-86918437; _gscu_791762522=200676906g9v7g18; _gscbrs_791762522=1; _pk_ref.17.88c4=%5B%22%22%2C%22%22%2C1720067693%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DHQPHCte3IStd-XYsq7LbKZP4ViZL2YctolyfChLFBllr1EM_oAf0CNEGBvV7kJkv%26wd%3D%26eqid%3Da4fe43b80018d5be0000000666862650%22%5D; _pk_id.17.88c4=a1ff8a3eee038bbc.1720067693.; _pk_ses.17.88c4=1; _gscs_791762522=20067690xzmcxd18|pv:2","Host":"www.liaocheng.gov.cn","Referer":"http://www.liaocheng.gov.cn/search.html?keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()