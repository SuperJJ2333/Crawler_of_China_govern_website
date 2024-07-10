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
        'city_name': '陕西省',
        'province_name': '陕西省',
        'province': 'province_web_data',
        'base_url': 'http://www.shaanxi.gov.cn/irs/front/search',

        'total_news_num': 7166,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Content-Length":"387","Content-Type":"application/json","Cookie":"_trs_uv=ly7k7ben_4366_50ol; JSESSIONID=C1B20D0B1973E83EA95960D6CC1AA6A7; _trs_ua_s_1=lyer2xde_4366_gz3r","Host":"www.shaanxi.gov.cn","Origin":"http://www.shaanxi.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.shaanxi.gov.cn/sxsearch/search.html?tenantId=10&code=183d935ed77&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = '{"tenantId":"10","searchWord":"学习考察 考察学习","dataTypeId":19,"historySearchWords":["学习考察 考察学习"],"orderBy":"related","searchBy":"all","granularity":"ALL","pageNo":3,"pageSize":10,"endDateTime":"","beginDateTime":"","filters":[],"configTenantId":"10","customFilter":{"operator":"and","properties":[],"filters":[]},"sign":"563deeb0-a780-4775-d730-b46dd2becfc6"}'

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