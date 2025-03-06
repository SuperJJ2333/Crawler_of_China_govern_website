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
        'city_name': '重庆市',
        'province_name': '重庆市',
        'province': '重庆市',
        'base_url': 'https://www.cq.gov.cn/irs/front/search',

        'total_news_num': 2753,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"549","Content-Type":"application/json","Cookie":"SESSION=OTM3ZmM0ZGUtMzk5MC00ZjYwLTgyMzktMTEzYmZjYzFjYzBi; JSESSIONID=D5A9B703D791111405EA0BA99B11FC74; arialoadData=true; ariawapChangeViewPort=false; _trs_uv=lyb6k9gf_3486_j0ss; _trs_ua_s_1=lyb6k9gf_3486_k7s1; _trs_gv=g_lyb6k9gf_3486_j0ss","Host":"www.cq.gov.cn","Origin":"https://www.cq.gov.cn","Referer":"https://www.cq.gov.cn/cqgovsearch/search.html?searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&tenantId=7&configTenantId=7&dataTypeId=7&sign=791435a1-6ea7-41f5-a167-74b2a775967a&searchBy=title","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"id":"7","tenantId":"7","searchWord":"学习考察 考察学习","dataTypeId":"7","pageNo":3,"pageSize":10,"orderBy":"related","searchBy":"all","appendixType":"","granularity":"ALL","beginDateTime":"","endDateTime":"","isSearchForced":0,"filters":[],"sign":"13b2f30e-df74-4b8c-8432-ea027bab5aee","pager":{"pageNo":2740},"searchInfo":{},"dataTypes":[],"configTenantId":"7","historySearchWords":["学习考察 考察学习","学习考察"],"operationType":"search","seniorBox":0,"isDefaultAdvanced":0,"isAdvancedSearch":0,"advancedFilters":[],"customFilters":[],"areaCode":""}'

    post_data = json.loads(post_data)

    page_num_name = 'pageNo'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      is_post_by_json=True)
    scraper.run()