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
    获取数据：API
    提取方法：JSON -- resultDocs -- data：titleO, docDate, url
    """

    city_info = {
        'city_name': '荆州市',
        'province_name': '湖北省',
        'province': 'Hubei',
        'base_url': 'https://api.so-gov.cn/query/s',

        'total_news_num': 3032,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"200","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Host":"api.so-gov.cn","Origin":"https://www.jingzhou.gov.cn","Referer":"https://www.jingzhou.gov.cn/","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"cross-site","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'siteCode': '4210000002', 'tab': 'qs', 'qt': '考察学习', 'keyPlace': '0', 'sort': 'relevance', 'fileType': '', 'timeOption': '0', 'locationCode': '421000000000', 'page': '3', 'pageSize': '20', 'ie': 'bc3080f4-0843-414c-a2c7-ef5271267329'}

    page_num_name = 'page'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:7890',
        'https': 'http://127.0.0.1:7890'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=False,
                      post_data=post_data, page_num_name=page_num_name,
                      verify=True, proxies=fiddler_proxies)
    scraper.run()