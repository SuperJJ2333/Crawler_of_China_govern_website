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
        'city_name': '银川市',
        'province_name': '宁夏省',
        'province': 'Ningxia',
        'base_url': 'https://www.yinchuan.gov.cn/irs/front/search',

        'total_news_num': 47,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"358","Content-Type":"application/json","Cookie":"SESSION=Y2YwMjY2NTItMWE2ZC00MzI0LTk0ZjMtOTQyMGM5NmQ5ZWVk; TS014935bd=0153d9a1131effc9cecd14f4afa39a950b065b538fa2116c32cc2339a012b8c7f4af07747bec8c02fd3be1f490a02f9b830fa75c99; Hm_lvt_55df24e09fbc429a2b25401c301c30a8=1720244339; Hm_lpvt_55df24e09fbc429a2b25401c301c30a8=1720244339; HMACCOUNT=A202F23FD4E0D795; _trs_uv=ly9p2b61_6060_185b; _trs_ua_s_1=ly9p2b61_6060_5b2q; TS01471b74=0153d9a1131effc9cecd14f4afa39a950b065b538fa2116c32cc2339a012b8c7f4af07747bec8c02fd3be1f490a02f9b830fa75c99","Host":"www.yinchuan.gov.cn","Origin":"https://www.yinchuan.gov.cn","Referer":"https://www.yinchuan.gov.cn/nxsearch/search.html?code=17cc9e163e5&tenantId=62&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"tenantIds":"62","tenantId":"62","searchWord":"学习考察 考察学习","dataTypeId":4,"historySearchWords":[],"orderBy":"related","searchBy":"title","pageNo":3,"pageSize":10,"endDateTime":"","beginDateTime":"","filters":[],"configTenantId":"19","customFilter":{"operator":"and","properties":[],"filters":[]},"sign":"ad69ffb9-8afe-4663-ce17-a63db321995c"}'

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