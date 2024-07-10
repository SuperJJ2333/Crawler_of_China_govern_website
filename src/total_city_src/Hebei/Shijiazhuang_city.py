import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('search', {}).get('searchs', [])

    for item in data_dict:
        try:
            topic = item.get('title', '')
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
        'city_name': '石家庄市',
        'province_name': '河北省',
        'province': 'Hebei',

        'base_url': 'https://api.so-gov.cn/s',

        'total_news_num': 48,
        'each_page_news_num': 20,
    }

    headers = {"Host":"api.so-gov.cn","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","Accept":"application/json, text/javascript, */*; q=0.01","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","sec-ch-ua-mobile":"?0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","suid":"385574c778699dddd356e1f05e0c6266","sec-ch-ua-platform":"\"Windows\"","Origin":"https://www.sjz.gov.cn","Sec-Fetch-Site":"cross-site","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://www.sjz.gov.cn/","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"}

    post_data = {'siteCode': '1301000003', 'tab': 'all', 'timestamp': '1720592594299', 'wordToken': '98ba6297f2e5414f920f142e6ab4264a', 'page': '2', 'pageSize': '20', 'qt': '学习考察 考察学习', 'timeOption': '0', 'sort': 'relevance', 'keyPlace': '1', 'fileType': '', 'toolsStatus': '1'}

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