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
        'city_code': 310,
        'city_name': '凉山彝族自治州',
        'province_name': '四川省',
        'province': '四川省',

        'base_url': 'https://www.lsz.gov.cn/irs/front/search',

        'total_news_num': 1425,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"426","Content-Type":"application/json","Cookie":"arialoadData=false; _trs_uv=m2yudubl_1248_j31b; _trs_ua_s_1=m2yudubl_1248_atgl","Host":"www.lsz.gov.cn","Origin":"https://www.lsz.gov.cn","Referer":"https://www.lsz.gov.cn/irs-c-web/search.html?code=18a074e0123&tenantId=1&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"tenantId":"1","searchWord":"学习考察","dataTypeId":1,"historySearchWords":["医保","公积金","住房保障","公务员"],"orderBy":"related","searchBy":"title","pageNo":2,"pageSize":10,"endDateTime":"","beginDateTime":"","filters":[],"configTenantId":"1","customFilter":{"operator":"and","properties":[],"filters":[{"operator":"or","properties":[]}]},"granularity":"ALL","sign":"74321c2e-6d77-4ec6-d6d9-230ca4e5f5e1"}'

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