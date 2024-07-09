import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('pageData', {})

    for item in data_dict:
        try:
            topic = item.get('title', '')
            date = item.get('publishdate', '')
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
    获取数据：API
    提取方法：JSON -- resultDocs -- data：titleO, docDate, url
    """

    city_info = {
        'city_name': '昆明市',
        'province_name': '云南省',
        'province': 'Yunnan',

        'base_url': 'https://govsearch.kunming.cn/new/api/v2/search',

        'total_news_num': 67724,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"265","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Host":"govsearch.kunming.cn","Origin":"https://www.km.gov.cn","Referer":"https://www.km.gov.cn/","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"cross-site","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'app_id': '526056d3b9f7410b8', 'keyword': '学习考察+考察学习', 'position': '1', 'orderField': '', 'page_index': '3', 'page_length': '20', 'order': 'desc', 'pattern': '1', 'date_from': '1262275200', 'date_to': '1720189645', 'sub_type': '', 'site_id': '', 'platform_id': '', 'sub_type_id': ''}

    page_num_name = 'page_index'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      verify=False, proxies=fiddler_proxies)
    scraper.run()