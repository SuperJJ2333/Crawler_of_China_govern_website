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
        'city_name': '中卫市',
        'province_name': '宁夏省',
        'province': 'Ningxia',
        'base_url': 'https://www.nxzw.gov.cn/irs/front/search',

        'total_news_num': 5,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"362","Content-Type":"application/json","Cookie":"SESSION=NjYzNTUwMTYtNGVmNy00OTc1LWI1NzItMTViOTdhY2UxN2Yz; TS01dbc741=0138b8b160c90fb69d72c5d000262c9d1ed96afa639394f8dae9249bc847e1fa0c0fce583f2de4d543d0bf0dcc3d616b391c0f76fa; _trs_uv=ly9pdo5h_1697_806h; _trs_ua_s_1=ly9pdo5h_1697_8tih; TS01d5e988=0138b8b160c90fb69d72c5d000262c9d1ed96afa639394f8dae9249bc847e1fa0c0fce583f2de4d543d0bf0dcc3d616b391c0f76fa","Host":"www.nxzw.gov.cn","Origin":"https://www.nxzw.gov.cn","Referer":"https://www.nxzw.gov.cn/nxsearch/search.html?code=17ccab70a79&tenantId=167&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"tenantIds":"167","tenantId":"167","searchWord":"学习考察 考察学习","dataTypeId":4,"historySearchWords":[],"orderBy":"related","searchBy":"title","pageNo":"1","pageSize":10,"endDateTime":"","beginDateTime":"","filters":[],"configTenantId":"19","customFilter":{"operator":"and","properties":[],"filters":[]},"sign":"a00e3209-9658-4373-ed50-4770d4e460f8"}'

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