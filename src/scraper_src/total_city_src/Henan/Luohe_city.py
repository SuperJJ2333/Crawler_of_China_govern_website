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
            url = 'http://www.luohe.gov.cn' + url

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
        'city_name': '漯河市',
        'province_name': '河南省',
        'province': 'Henan',

        'base_url': 'http://www.luohe.gov.cn/search/SolrSearch/searchData',

        'total_news_num': 179,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"205","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"zh_choose_undefined=s; shiro.sesssion=0b2e3c3f-4b8d-4b75-bf2b-82bcdbe61ca4; wzafullscreen=0","Host":"www.luohe.gov.cn","Origin":"http://www.luohe.gov.cn","Referer":"http://www.luohe.gov.cn/search/SolrSearch/s","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest"}

    post_data = {'q': '考察学习', 'type': '', 'timeType': '', 'sort': '', 'order': '', 'forCatalogType': '0', 'token4': '0b7cc84405384c5bbda7ad9346b5bcf2', 'siteId': 'efc127c860d248459e9b75bc458977d7', 'offset': '10', 'limit': '10', 'infoType': ''}

    page_num_name = 'offset'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      num_added_each_time=10, page_num_start=0)
    scraper.run()

