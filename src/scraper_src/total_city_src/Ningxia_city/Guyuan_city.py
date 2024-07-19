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
        'city_name': '固原市',
        'province_name': '宁夏省',
        'province': 'Ningxia',
        'base_url': 'http://www.nxgy.gov.cn/irs/front/search',

        'total_news_num': 208,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Content-Length":"358","Content-Type":"application/json","Cookie":"SESSION=NDcxNWI3ZWYtYjY0Ni00MGU3LThlZTYtNjhjYjY1YTBmMzVj; TS01559ac8=01f68ff1a1fc877b86e9a87d6c0b8363f41d1de89050a8bbad00153c8c0f719fa000c9d16a64bc83de33d4db01034c8f9094971cbd; _trs_uv=ly9pd9t2_1328_juht; _trs_ua_s_1=ly9pd9t2_1328_in10; TS015bb401=01f68ff1a1fc877b86e9a87d6c0b8363f41d1de89050a8bbad00153c8c0f719fa000c9d16a64bc83de33d4db01034c8f9094971cbd","Host":"www.nxgy.gov.cn","Origin":"http://www.nxgy.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.nxgy.gov.cn/nxsearch/search.html?code=17c793b048a&tenantId=8&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = '{"tenantIds":"8","tenantId":"8","searchWord":"学习考察 考察学习","dataTypeId":4,"historySearchWords":[],"orderBy":"related","searchBy":"all","pageNo":3,"pageSize":10,"filters":[],"configTenantId":"19","customFilter":{"operator":"and","properties":[],"filters":[]},"sign":"2b358654-603b-406a-dc6d-349538e842be"}'

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