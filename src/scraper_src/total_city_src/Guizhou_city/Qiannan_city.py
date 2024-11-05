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
        # item = item.get('data', {})
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
        'city_code': 312,
        'city_name': '黔南布依族苗族自治州',
        'province_name': '贵州省',
        'province': '贵州省',

        'base_url': 'https://www.qiannan.gov.cn/irs/front/search',

        'total_news_num': 2152,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"333","Content-Type":"application/json","Cookie":"SESSION=MTVkMTliNWMtNTIwYi00MGI1LTgxNDctMjk2NzJkNzgyNzI5; _trs_uv=m2yuoni0_2505_50zf; _trs_ua_s_1=m2yzf8ku_2505_5bl","Host":"www.qiannan.gov.cn","Origin":"https://www.qiannan.gov.cn","Referer":"https://www.qiannan.gov.cn/so/search.shtml?tenantId=155&tenantIds=&configTenantId=&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&dataTypeId=165&sign=b719f40d-65f0-4964-a8dd-8916bb5bc69e","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"tenantId":"155","configTenantId":"","tenantIds":"","searchWord":"学习考察","historySearchWords":["学习考察","学习考察 考察学习"],"dataTypeId":"165","orderBy":"related","searchBy":"all","appendixType":"","granularity":"ALL","beginDateTime":"","endDateTime":"","isSearchForced":0,"filters":[],"pageNo":2,"pageSize":9}'

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