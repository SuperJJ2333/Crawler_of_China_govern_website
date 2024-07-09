import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('rows', {})

    for item in data_dict:

        try:
            topic = item.get('articleTitle', '')
            date = item.get('articlePublishTime', '')
            url = item.get('articleUri', '')
        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        if url.startswith('http') is False:
            url = 'https://www.zhoukou.gov.cn' + url

        news_info = {
            'topic': topic,
            'date': date,
            'url': url,
        }
        extracted_news_list.append(news_info)

    return extracted_news_list


if __name__ == '__main__':
    """
    请求方法：POST -- 0
    获取数据：API -- offset
    提取方法：JSON -- resultDocs -- resultDocs -- titleO, docDate, url
    """

    city_info = {
        'city_name': '周口市',
        'province_name': '河南省',
        'province': 'Henan',

        'base_url': 'https://www.zhoukou.gov.cn/search/SolrSearch/searchData',

        'total_news_num': 826,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"230","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"wzafullscreen=0; shiro.sesssion=0a480d17-4522-4174-a279-4e9bc4ce8379","Host":"www.zhoukou.gov.cn","Origin":"https://www.zhoukou.gov.cn","Referer":"https://www.zhoukou.gov.cn/search/SolrSearch/s","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'q': '学习考察 考察学习', 'type': '', 'timeType': '', 'sort': '', 'order': '', 'forCatalogType': '0', 'token4': '788b54d467bd4e2d8d7e320c32a946e1', 'siteId': '9752499e88b94e1881e46bbeeef1376e', 'offset': '10', 'limit': '10', 'infoType': ''}

    page_num_name = 'offset'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      num_added_each_time=10, page_num_start=0)
    scraper.run()

