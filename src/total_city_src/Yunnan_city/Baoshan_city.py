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
        'city_name': '保山市',
        'province_name': '云南省',
        'province': 'Yunnan',
        'base_url': 'https://www.baoshan.gov.cn/aop_component//webber/search/search/search/queryPage',

        'total_news_num': 49,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Authorization":"tourist","Connection":"keep-alive","Content-Length":"595","Content-Type":"application/json;charset=UTF-8","Cookie":"JSESSIONID=E65587B7E206C0ADC5ADA93F70E11702; appsearch_sessionid=E02B2C6D971921033C25F551ABA24705","Host":"www.baoshan.gov.cn","Origin":"https://www.baoshan.gov.cn","Referer":"https://www.baoshan.gov.cn/views/search/modules/resultpcegov/soso.html?query=eyJrZXlXb3JkIjoi5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oCIsIm93bmVyIjoiMTg4ODk4Njk2NyIsInRva2VuIjoidG91cmlzdCIsInVybFByZWZpeCI6Ii9hb3BfY29tcG9uZW50LyIsImxhbmciOiJpMThuX3poX0NOIn0=","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","owner":"1888986967","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"aliasName":"article_data,open_data,mailbox_data","keyWord":"学习考察 考察学习","lastkeyWord":"学习考察 考察学习","orderType":"score","searchType":"text","searchScope":"1","searchDateType":"","searchDateName":"时间不限","beginDate":"","endDate":"2024-07-05","showId":"ddad926c9acf4ab250f807b832b80d0b","auditing":["1"],"owner":"1888986967","token":"tourist","urlPrefix":"/aop_component/","costTime":52,"page":{"current":2,"size":10,"pageSizes":[2,5,10,20,50,100],"total":49,"totalPage":5,"indexs":[1,2,3,4,5]},"filter":{},"searchAggregation":false,"aggFields":{"_index":""}}'
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