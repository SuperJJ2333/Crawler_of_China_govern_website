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
        'city_name': '阳泉市',
        'province_name': '山西省',
        'province': 'Shanxi',

        'base_url': 'http://www.yq.gov.cn/irs/front/search',

        'total_news_num': 392,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"347","Content-Type":"application/json","Host":"www.yq.gov.cn","Origin":"http://www.yq.gov.cn","Referer":"http://www.yq.gov.cn/irs-c-web/yqszf/search.shtml?code=184d12594d4&codes=&configCode=&searchWord=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&dataTypeId=199&sign=3326965d-82d5-4fa7-a550-492ea99a1a6a&searchBy=title","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest"}

    post_data = '{"code":"184d12594d4","configCode":"","codes":"","searchWord":"考察学习","historySearchWords":["考察学习","学习考察","学习考察 考察学习"],"dataTypeId":"199","orderBy":"related","searchBy":"title","appendixType":"","granularity":"ALL","beginDateTime":"","endDateTime":"","isSearchForced":0,"filters":[],"pageNo":2,"pageSize":10}'

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