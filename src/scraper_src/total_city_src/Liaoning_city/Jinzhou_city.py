from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '锦州市',
        'province_name': '辽宁省',
        'province': 'Liaoning',

        'base_url': 'http://www.jz.gov.cn/hhjsjgy.jsp?wbtreeid=1001&keyword=5a2m5Lmg6ICD5a%2BfIOiAg%2BWvn%2BWtpuS5oA%3D%3D&cc=W10%3D&ot=1&rg=4&tg=5&clid=0&currentnum={page_num}',

        'total_news_num': 840,

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@class="xwd"]',
                     'title': 'x://div/a',
                     'date': ['x://div[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"HWWAFSESID=c577b76ea28eb052a6; HWWAFSESTIME=1720005968201; _gscu_262868561=200060817krv6567; _gscbrs_262868561=1; JSESSIONID=88ab546ba2e72e472b38dbe4da54; _gscs_262868561=t20009274uxejb317|pv:2","Host":"www.jz.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.jz.gov.cn/hhjsjgy.jsp?wbtreeid=1001","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()