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
            topic = item.get('title_no_tag', '')
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
        'city_name': '贵州省',
        'province_name': '贵州省',
        'province': 'province_web_data',
        'base_url': 'https://www.guizhou.gov.cn/irs/front/search',

        'total_news_num': 4995,
        'each_page_news_num': 9,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"348","Content-Type":"application/json","Cookie":"SESSION=N2JmNjUwZTUtNjdlNy00MTcwLWE3NDMtYWQ4Njc0YTFlZTAz; _trs_uv=ly2xqa6g_367_y58; _trs_ua_s_1=lyeleqqw_367_4p79; _yfxkpy_ssid_10000921=%7B%22_yfxkpy_firsttime%22%3A%221719835631648%22%2C%22_yfxkpy_lasttime%22%3A%221720540531860%22%2C%22_yfxkpy_visittime%22%3A%221720540531860%22%2C%22_yfxkpy_domidgroup%22%3A%221719835631648%22%2C%22_yfxkpy_domallsize%22%3A%22100%22%2C%22_yfxkpy_cookie%22%3A%2220240701200711650474946353493585%22%2C%22_yfxkpy_returncount%22%3A%221%22%7D; arialoadData=false","Host":"www.guizhou.gov.cn","Origin":"https://www.guizhou.gov.cn","Referer":"https://www.guizhou.gov.cn/so/search.shtml?tenantId=186&tenantIds=&configTenantId=&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&dataTypeId=963&sign=78e2f8a8-cfff-4f0f-a197-88b81435697f&searchBy=title","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"tenantId":"186","configTenantId":"","tenantIds":"","searchWord":"学习考察考察学习","historySearchWords":["学习考察考察学习","学习考察 考察学习","学习考察"],"dataTypeId":"963","orderBy":"related","searchBy":"all","appendixType":"","granularity":"ALL","beginDateTime":"","endDateTime":"","isSearchForced":0,"filters":[],"pageNo":3,"pageSize":9}'

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