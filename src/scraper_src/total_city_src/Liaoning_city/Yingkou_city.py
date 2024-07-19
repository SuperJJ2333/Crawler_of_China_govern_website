import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('result', {}).get('records', [])

    for item in data_dict:
        try:
            topic = item.get('title', '')
            date = item.get('webdate', '')
            url = item.get('linkurl', '')
        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        if url.startswith('http') is False:

            url = 'http://www.yingkou.gov.cn' + url

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
        'city_name': '营口市',
        'province_name': '辽宁省',
        'province': 'Liaoning',
        'base_url': 'http://www.yingkou.gov.cn/inteligentsearch/rest/inteligentSearch/getFullTextData',

        'total_news_num': 582,
        'each_page_news_num': 10,
    }

    headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", "Content-Length": "415",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Cookie": "HttpOnly; HttpOnly; fontZoomState=0", "Host": "www.yingkou.gov.cn",
               "Origin": "http://www.yingkou.gov.cn", "Proxy-Connection": "keep-alive",
               "Referer": "http://www.yingkou.gov.cn/search/fullsearch.html?wd=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
               "X-Requested-With": "XMLHttpRequest"}
    post_data = r"""
    {
  "token": "",
  "pn": 0,
  "rn": "",
  "sdt": "",
  "edt": "",
  "wd": "%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0",
  "inc_wd": "",
  "exc_wd": "",
  "fields": "title;content",
  "cnum": "001;002;",
  "sort": "{\"sysscore\":\"0\"}",
  "ssort": "title",
  "cl": 500,
  "terminal": "",
  "condition": null,
  "time": null,
  "highlights": "title;content",
  "statistics": null,
  "unionCondition": null,
  "accuracy": "",
  "noParticiple": "0",
  "searchRange": null
}

    """
    post_data = json.loads(post_data)

    page_num_name = 'pn'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, page_num_start=0,
                      num_added_each_time=10,
                      verify=False, proxies=fiddler_proxies, is_post_by_json=True)
    scraper.run()
