from scraper.scraper import Scraper

if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '包头市',
        'province_name': '内蒙古省',
        'province': 'Neimenggu',

        'base_url': 'https://www.baotou.gov.cn/qwjs_search_list.jsp?wbtreeid=1001&searchScope=0&currentnum={page_num}&newskeycode2=5a2m5Lmg6ICD5a%2BfIOiAg%2BWvn%2BWtpuS5oA%3D%3D',

        'total_news_num': 7707,

        'each_page_news_num': 15,
    }

    content_xpath = {'frames': 'x:/html/body/div[3]/div[2]/div[2]/form[2]/table[1]//tr/td/a[@href]',
                     'title': 'x:/../a',
                     'date': ['x:/../../following-sibling::tr[3]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"arialoadData=false; JSESSIONID=732AE2D2CB93967009F14D54D62DD811","Host":"www.baotou.gov.cn","Referer":"https://www.baotou.gov.cn/qwjs_search_list.jsp?wbtreeid=1001","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True)
    scraper.run()