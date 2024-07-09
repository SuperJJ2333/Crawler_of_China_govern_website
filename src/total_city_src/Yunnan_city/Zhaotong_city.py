import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('result', {}).get('list', [])

    for item in data_dict:
        try:
            topic = item.get('title', '')
            date = item.get('addDate', '')
            url = f'http://www.zt.gov.cn/content.html?channelid={item.get("channelId")}&id={item.get("id")}'
        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        if url.startswith('http') is False:
            url = 'https://' + url

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
        'city_name': '昭通市',
        'province_name': '云南省',
        'province': 'Yunnan',
        'base_url': 'http://www.zt.gov.cn/searchApi/search',

        'total_news_num': 367,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Content-Length":"131","Content-Type":"application/json;charset=UTF-8","Cookie":"arialoadData=false","Host":"www.zt.gov.cn","Origin":"http://www.zt.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.zt.gov.cn/search.html?words=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = '{"siteId":1,"keyword":"学习考察 考察学习","searchType":0,"thisSite":1,"sortType":0,"pageNum":3,"channelId":0,"pageSize":10}'

    post_data = json.loads(post_data)

    page_num_name = 'pageNum'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json', is_post_by_json=True,
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      verify=False, proxies=fiddler_proxies, page_num_start=0)
    scraper.run()