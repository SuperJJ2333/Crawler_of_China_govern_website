import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('resultDocs', {})

    for item in data_dict:
        item = item.get('data', {})
        try:
            topic = item.get('titleO', '')
            date = item.get('docDate', '')
            url = item.get('url', '')
        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

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
    获取数据：API -- by_json
    提取方法：JSON -- resultDocs -- data：titleO, docDate, url
    """

    city_info = {
        'city_name': '南宁市',
        'province_name': '广西省',
        'province': 'Guangxi',
        'base_url': 'https://api.so-gov.cn/query/s',

        'total_news_num': 989,
        'each_page_news_num': 20,
    }

    headers = {"Host":"api.so-gov.cn","Connection":"keep-alive","Content-Length":"201","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","Accept":"application/json, text/javascript, */*; q=0.01","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","sec-ch-ua-mobile":"?0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua-platform":"\"Windows\"","Origin":"https://www.nanning.gov.cn","Sec-Fetch-Site":"cross-site","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://www.nanning.gov.cn/","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"}

    post_data = {'keyPlace': '0', 'sort': 'relevance', 'fileType': '', 'timeOption': '0', 'locationCode': '450000000000', 'siteCode': '4501000060', 'tab': 'all', 'page': '1', 'pageSize': '20', 'qt': '考察学习', 'ie': '59715e1d-8703-47df-83a5-5814ec517468'}

    page_num_name = 'page'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      verify=False, proxies=fiddler_proxies)
    scraper.run()
