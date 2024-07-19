import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('result', {}).get('data', {}).get('middle', {}).get('list', {})

    for item in data_dict:
        try:
            topic = item.get('title', '')
            date = item.get('time', '')
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
    提取方法：JSON -- data -- middle -- listAndBox -- titleO, docDate, url
    """

    city_info = {
        'city_name': '中国政府',
        'province_name': '中国政府',
        'province': 'province_web_data',
        'base_url': 'https://sousuoht.www.gov.cn/athena/forward/2B22E8E39E850E17F95A016A74FCB6B673336FA8B6FEC0E2955907EF9AEE06BE',

        'total_news_num': 4566,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"403","Content-Type":"application/json;charset=UTF-8","Host":"sousuoht.www.gov.cn","Origin":"https://sousuo.www.gov.cn","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-site","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","athenaAppKey":"LjFtgckyFPZ0QbFXoLUcW4sTKbKwZXz64mGV0qnJGVgojkw6vvnpSHepwU0NhMDIxcgRfaKsytsPfkdE%2BGBTbdrbV3kkVwblFo9PYhcgzIhhrtpwaw7%2BJh614sAdwMLFxhsxgnC0oVPo0Kge8t7Zsx8iAWYoe7NnGSdqC0iqw8U%3D","athenaAppName":"%E5%9B%BD%E7%BD%91%E6%90%9C%E7%B4%A2","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\"","transformRequest":"function(t){return\"object\"===zt(t)&&\"[object File]\"!==String(t)?bt(t):t}"}

    post_data = '{"code":"17da70961a7","historySearchWords":["学习考察考察学习","学习考察 考察学习","学习考察","考察学习"],"dataTypeId":"107","orderBy":"time","searchBy":"all","appendixType":"","granularity":"ALL","trackTotalHits":true,"beginDateTime":"","endDateTime":"","isSearchForced":0,"filters":[],"pageNo":2,"pageSize":10,"customFilter":{"operator":"and","properties":[]},"searchWord":"学习考察考察学习"}'

    post_data = json.loads(post_data)

    page_num_name = 'pageNo'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, proxies=fiddler_proxies, verify=False,
                      is_post_by_json=True)
    scraper.run()