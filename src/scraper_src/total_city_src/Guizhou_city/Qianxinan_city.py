import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('middle', {}).get('list', {})

    for item in data_dict:
        # item = item.get('data', {})
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
        'city_code': 313,
        'city_name': '黔西南布依族苗族自治州',
        'province_name': '贵州省',
        'province': '贵州省',

        'base_url': 'https://www.qxn.gov.cn/irs/front/search',

        'total_news_num': 918,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"331","Content-Type":"application/json","Cookie":"SESSION=YmE5NWNhMTgtZTY5YS00NjRmLWI3MDItOGYwMDkyMjY2ZWRj; _yfxkpy_ssid_10000622=%7B%22_yfxkpy_firsttime%22%3A%221730480724037%22%2C%22_yfxkpy_lasttime%22%3A%221730480724037%22%2C%22_yfxkpy_visittime%22%3A%221730480724037%22%2C%22_yfxkpy_cookie%22%3A%2220241102010524039267649779481644%22%7D; _trs_uv=m2yzjkol_3300_ip1; _trs_ua_s_1=m2yzjkol_3300_slj","Host":"www.qxn.gov.cn","Origin":"https://www.qxn.gov.cn","Referer":"https://www.qxn.gov.cn/so/search.shtml?tenantId=158&tenantIds=&configTenantId=&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&dataTypeId=517&sign=04aff656-d640-4219-ef6f-0f1857932f7b","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"tenantId":"158","configTenantId":"","tenantIds":"","searchWord":"学习考察 考察学习","historySearchWords":["学习考察 考察学习"],"dataTypeId":"517","orderBy":"related","searchBy":"all","appendixType":"","granularity":"ALL","beginDateTime":"","endDateTime":"","isSearchForced":0,"filters":[],"pageNo":2,"pageSize":9}'

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