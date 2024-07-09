import json

from common.form_utils import convert_timestamp_to_date
from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {})

    for item in data_dict:
        try:
            topic = item.get('title', '')
            date = convert_timestamp_to_date(item.get('inputtime', ''))
            url = item.get('url', '')

            if url.startswith('http') is False:
                url = 'https://www.wulanchabu.gov.cn' + url
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
    提取方法：JSON -- data -- search -- searchs -- title, docDate, viewUrl
    """

    city_info = {
        'city_name': '乌兰察布市',
        'province_name': '内蒙古省',
        'province': 'Neimenggu',

        'base_url': 'https://www.wulanchabu.gov.cn/es/query?',

        'total_news_num': 31,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"1059","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"pageNo=1; pageSize=4","Host":"www.wulanchabu.gov.cn","Origin":"https://www.wulanchabu.gov.cn","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'index': 'document', 'siteid': '["c1e76ccbcf9e45ee90fdf38dbffd1e15","d2bb937d081e44699a9c74ebadb997b8","7a76b13ed4e54194bd4e086a5c8cd390","b61c60832bc94affa0626f03959dbaa5","ef61459674e04b75a34ff5e9b5f1ff55","98b4f3d7995046738c5eb8a41dc1e28c","6f73571f6a5f4c33893743a1cc8b6ad1","5ad6b56f682a41b59dcb4fb39b814023","ae40eeac00e14185ad979ec67c528cb0","8838100fac4440c29783c9da4c86e4d6","b476c730b660417f8c72e5d23b3cf91f","1440ab9d2fe844df89b56be43d2ab1dd","94d0845c116a4b0485764025e2e8c8b6","ccf4a2560fee45ff9447164cc4dd3e5f","e12bc255660f4bdaa7cf40c547816822","bc9101c1f66043f4b0ae937858a54db0","12df4dde1d43490aa17089dbe1554ed0","a76f6dfac580423283ba1fe5faeda88c","814e24c558804e0d851faf96fc5f63e1","f8633fc1cde44c08b70a15bdf4620abc","8d01edbbe34a420cb5ea43a74b9c87a9"]', 'keyword': '考察学习', 'issuedno': '考察学习', 'page': '3', 'size': '9', 'sortType': 'desc', 'searchType': '1', 'tcontesType': '1', 'othertype': '!znwd', 'sortField': ''}

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