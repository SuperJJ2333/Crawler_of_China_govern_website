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
        'city_name': '安顺市',
        'province_name': '贵州省',
        'province': 'Guizhou',
        'base_url': 'https://www.anshun.gov.cn/irs/front/search',

        'total_news_num': 816,
        'each_page_news_num': 9,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"334","Content-Type":"application/json","Cookie":"SESSION=NjJlMzFkNTctMDcwNy00ZTY0LThhNmQtYzZiYjcyM2NiNWRm; _trs_user=; SESSION=M2NjZmFmZTQtZTkwYS00NmJhLTllMDktNDliNGRkMzU1NWMy; authentication=IN+/ivdsDnBgUCZqfVQrVRKj4FvUhVCRfig46+AqtFotAn8FgvyyAkJ94bB9j2bnTscJmWAk2pP5T4B8gtBpIw==; barrier-free={%22show%22:false%2C%22audio%22:false%2C%22continuousRead%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22view%22:false%2C%22colorMatch%22:%22original%22%2C%22bigtextTraditional%22:false}; _trs_uv=ly2y88e9_3037_he21; _trs_ua_s_1=ly2y88e9_3037_9a8w","Host":"www.anshun.gov.cn","Origin":"https://www.anshun.gov.cn","Referer":"https://www.anshun.gov.cn/sosuo/search.shtml?tenantId=244&tenantIds=&configTenantId=&dataTypeId=1374&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchBy=title","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"tenantId":"244","configTenantId":"","tenantIds":"","searchWord":"学习考察 考察学习","historySearchWords":["学习考察 考察学习"],"dataTypeId":"1374","orderBy":"related","searchBy":"all","appendixType":"","granularity":"ALL","beginDateTime":"","endDateTime":"","isSearchForced":0,"filters":[],"pageNo":1,"pageSize":9}'

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