import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('page', []).get('records', [])

    for item in data_dict:
        try:
            topic = item.get('title', '')
            date = item.get('createDate', '')
            url = item.get('url', '')
        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        if url.startswith('http') is False:
            url = 'https://' + url

        news_info = {
            'topic': topic,
            'date': date,
            'url': url,
        }
        extracted_news_list.append(news_info)

    return extracted_news_list


if __name__ == '__main__':
    """
    请求方法：POST -- verify
    获取数据：API
    提取方法：JSON -- resultDocs -- data：titleO, docDate, url
    """

    city_info = {
        'city_name': '临沧市',
        'province_name': '云南省',
        'province': 'Yunnan',
        'base_url': 'https://www.lincang.gov.cn/aop_component//webber/search/search/search/queryPage',

        'total_news_num': 2297,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Authorization":"tourist","Connection":"keep-alive","Content-Length":"658","Content-Type":"application/json;charset=UTF-8","Cookie":"JSESSIONID=0CE0A685E2C8775299752BA443BDB337; arialoadData=false; appsearch_sessionid=DDD41D7F1A46CEB04A6543D661A78A97","Host":"www.lincang.gov.cn","Origin":"https://www.lincang.gov.cn","Referer":"https://www.lincang.gov.cn/views/search/modules/resultpc/soso.html?query=eyJrZXlXb3JkIjoi5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oCIsIm93bmVyIjoiMTc4NTQzMTAxMyIsInRva2VuIjoiXG5cblxuXG5cblxuXG5cblxuXG5cbnRvdXJpc3RcbiIsInVybFByZWZpeCI6Ii9hb3BfY29tcG9uZW50LyIsImxhbmciOiJpMThuX3poX0NOIn0=","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","owner":"1785431013","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = r'{"aliasName":"article_data,open_data,mailbox_data,guest_book","keyWord":"学习考察考察学习","lastkeyWord":"学习考察考察学习","searchKeyWord":false,"orderType":"score","searchType":"text","searchScope":"3","searchOperator":0,"searchDateType":"","searchDateName":"time.any_time","beginDate":"","endDate":"2024-07-17","showId":"f8d03086e1bc3b9c9f3bc4040d99a900","auditing":["1"],"owner":"1785431013","token":"\n\n\n\n\n\n\n\n\n\n\ntourist\n","urlPrefix":"/aop_component/","page":{"current":2,"size":10,"pageSizes":[2,5,10,20,50,100],"total":2297,"totalPage":230,"indexs":[1,2,3,4,5,6,7,8,9,10]},"advance":false,"advanceKeyWord":"","lang":"i18n_zh_CN"}'

    post_data = json.loads(post_data)

    page_num_name = 'page.current'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json', is_post_by_json=True,
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      verify=False, proxies=fiddler_proxies, page_num_start=0)
    scraper.run()