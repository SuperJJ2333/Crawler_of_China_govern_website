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
    请求方法：POST
    获取数据：API
    提取方法：JSON -- resultDocs -- resultDocs -- titleO, docDate, url
    """

    city_info = {
        'city_name': '钦州市',
        'province_name': '广西省',
        'province': 'Guangxi',
        'base_url': 'http://www.qinzhou.gov.cn/irs/front/search',

        'total_news_num': 57,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"331","Content-Type":"application/json","Cookie":"_trs_uv=ly2x1j67_5750_7x5j; _trs_ua_s_1=ly2x1j67_5750_5x3r","Host":"www.qinzhou.gov.cn","Origin":"http://www.qinzhou.gov.cn","Referer":"http://www.qinzhou.gov.cn/irs-common-search/search?code=184379028a3&configCode=&sign=9cc99c9d-94aa-44b4-aa79-41227a5385d7&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&orderBy=related&searchBy=all&appendixType=&granularity=ALL&isSearchForced=0&pageNo=1&pageSize=10&isAdvancedSearch&isDefaultAdvanced&advancedFilters&dataTypeId=5606","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = '{"code":"184379028a3","dataTypeId":"5606","configCode":"","searchWord":"学习考察 考察学习","orderBy":"related","searchBy":"title","appendixType":"","granularity":"ALL","isSearchForced":"0","filters":[],"pageNo":2,"pageSize":10,"isAdvancedSearch":null,"isDefaultAdvanced":null,"advancedFilters":null,"historySearchWords":[]}'

    post_data = json.loads(post_data)

    page_num_name = 'pageNo'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, is_post_by_json=True,
                      verify=False, proxies=fiddler_proxies)
    scraper.run()