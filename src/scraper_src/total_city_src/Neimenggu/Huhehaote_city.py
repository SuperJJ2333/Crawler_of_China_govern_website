import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('search', []).get('searchs', [])

    for item in data_dict:
        try:
            topic = item.get('disPlayTitle', '')
            date = item.get('docDate', '')
            url = item.get('viewUrl', '')
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
    获取数据：API
    提取方法：JSON -- data -- search -- searchs -- title, docDate, viewUrl
    """

    city_info = {
        'city_name': '呼和浩特市',
        'province_name': '内蒙古省',
        'province': 'Neimenggu',

        'base_url': 'https://api.so-gov.cn/s',

        'total_news_num': 271,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"253","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Host":"api.so-gov.cn","Origin":"http://www.huhhot.gov.cn","Referer":"http://www.huhhot.gov.cn/so/s","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"cross-site","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\"","suid":"c85c8c9cb733c04a84380fa1cf4d09e5"}

    post_data = {'siteCode': '1501000001', 'tab': 'all', 'timestamp': '1721044991272', 'wordToken': 'f602e3f1405e559e621eec49cfe49e42', 'page': '3', 'pageSize': '20', 'qt': '学习考察 考察学习', 'timeOption': '0', 'sort': 'relevance', 'keyPlace': '0', 'fileType': ''}

    page_num_name = 'page'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      verify=False, proxies=fiddler_proxies)
    scraper.run()