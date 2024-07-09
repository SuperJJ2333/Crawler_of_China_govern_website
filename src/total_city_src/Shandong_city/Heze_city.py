import json

from common.form_utils import convert_timestamp_to_date
from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('resultDocs', {})

    for item in data_dict:

        try:
            topic = item.get('subject', '')
            date = convert_timestamp_to_date(item.get('fwdate', ''))
            url = item.get('url', '')

            if not url:
                url = f"http://www.heze.gov.cn/0530/{item.get('dwid', '')[0]}/{item.get('xxid', '')}.html"

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
    请求方法：POST -- URL -- PARAMS
    获取数据：API
    提取方法：JSON -- resultDocs -- resultDocs -- titleO, docDate, url
    """

    city_info = {
        'city_name': '菏泽市',
        'province_name': '山东省',
        'province': 'Shandong',

        'base_url': 'http://www.heze.gov.cn/els-service/search/new/{page_num}/10',

        'total_news_num': 212,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"222","Content-Type":"application/json;charset=UTF-8","Host":"www.heze.gov.cn","Origin":"http://www.heze.gov.cn","Referer":"http://www.heze.gov.cn/jiansuo/?keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = '{"dq":"0530","fwzt":3,"highlight":"1","isSearch":"1","type":[1,2,3,6],"tab":"all","subject":"学习考察 考察学习","zcwjCatas":["1569654971522224128","1569655015231066112","1569655061443907584","1569655539049304064"]}'

    post_data = json.loads(post_data)

    scraper = Scraper(city_info, method='post_change', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, is_post_by_json=True)
    scraper.run()
