import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('middle', {}).get('listAndBox', {})

    for item in data_dict:
        item = item.get('data', {})
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
        'city_name': '南充市',
        'province_name': '四川省',
        'province': 'Sichuan',

        'base_url': 'https://www.nanchong.gov.cn/irs/front/search',

        'total_news_num': 6517,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"446","Content-Type":"application/json","Cookie":"_gscu_651081769=19297691tckkrc17; _gscbrs_651081769=1; _trs_uv=ly8iw1cn_5533_h64z; _trs_ua_s_1=ly8iw1cn_5533_tmf; _gscs_651081769=201734999cl0nh12|pv:2","Host":"www.nanchong.gov.cn","Origin":"https://www.nanchong.gov.cn","Referer":"https://www.nanchong.gov.cn/irs-c-web/search.html?code=17f3e45d275&tenantId=2&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"tenantId":2,"searchWord":"学习考察 考察学习","dataTypeId":22,"historySearchWords":["建党100周年","经济建设","人文南充","新村新貌","投资南充"],"orderBy":"related","searchBy":"all","pageNo":3,"pageSize":10,"endDateTime":"","beginDateTime":"","filters":[],"configTenantId":2,"customFilter":{"operator":"and","properties":[],"filters":[{"operator":"or","properties":[]}]},"sign":"1086b585-fe17-4031-e0ad-595a34b65308"}'

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