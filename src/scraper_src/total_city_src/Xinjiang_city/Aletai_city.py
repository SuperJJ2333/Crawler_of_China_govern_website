import json

from common.form_utils import convert_timestamp_to_date
from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('result', {}).get('records', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('infodate', '')
            url = item.get('linkurl', '')

            if not url.startswith('http'):
                url = f"http://wap.xjalt.gov.cn{url}"

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
        'city_code': 304,
        'city_name': '阿勒泰地区',
        'province_name': '新疆省',
        'province': '新疆省',

        'base_url': 'http://wap.xjalt.gov.cn/inteligentsearch/rest/esinteligentsearch/getFullTextDataNew',

        'total_news_num': 107,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"383","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"fontZoomState=0","Host":"wap.xjalt.gov.cn","Origin":"http://wap.xjalt.gov.cn","Referer":"http://wap.xjalt.gov.cn/search/fullsearch.html?wd=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","X-Requested-With":"XMLHttpRequest"}

    post_data = '{"token":"","pn":10,"rn":10,"sdt":"","edt":"","wd":"%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F","inc_wd":"","exc_wd":"","fields":"title;content","cnum":"001001;001002;001003;001004;001005;","sort":"","ssort":"title","cl":500,"terminal":"","condition":null,"time":null,"highlights":"title;content","statistics":null,"unionCondition":null,"accuracy":"","noParticiple":"0","searchRange":null}'
    post_data = json.loads(post_data)

    page_num_name = 'pn'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, is_post_by_json=True,
                      page_num_name=page_num_name, num_added_each_time=10, page_num_start=0)
    scraper.run()