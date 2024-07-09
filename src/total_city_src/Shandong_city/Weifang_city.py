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
                url = f"http://www.qingzhou.gov.cn/21/21/{item.get('xxid', '')}.html"

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
        'city_name': '潍坊市',
        'province_name': '山东省',
        'province': 'Shandong',

        'base_url': 'http://www.weifang.gov.cn/xxgk/els-service/search/new/{page_num}/10',

        'total_news_num': 1323,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Content-Length":"91","Content-Type":"application/json;charset=UTF-8","Cookie":"wzws_sessionid=gDIyMS40LjMyLjI0gTVmNDU5MYIyODUwMGGgZoWIZA==; wondersLog_sdywtb_sdk=%7B%22persistedTime%22%3A1720027241839%2C%22updatedTime%22%3A1720027243412%2C%22sessionStartTime%22%3A1720027243410%2C%22sessionReferrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DwJZTQl4tAgYbb6OmfVwOnNKIcQSJi2UhngO55tH62WZcAP75T479IUpmyf2g9Nqa%26wd%3D%26eqid%3Dc1852cb8012bd50a0000000666858860%22%2C%22deviceId%22%3A%223cd4f5e5cd1607a161b575c6b0690bb2-6131%22%2C%22LASTEVENT%22%3A%7B%22eventId%22%3A%22wondersLog_pv%22%2C%22time%22%3A1720027243411%7D%2C%22sessionUuid%22%3A7367206363914831%2C%22costTime%22%3A%7B%22wondersLog_unload%22%3A1720027243412%7D%7D; Hm_lvt_5f74e9712bcef8f20555ab46f83261e2=1720027246; Hm_lpvt_5f74e9712bcef8f20555ab46f83261e2=1720027246; ppimssessionId=e74c4053-6c3a-4b3b-abdd-1fbf17472bf3-1720027396389","Host":"www.weifang.gov.cn","Origin":"http://www.weifang.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.weifang.gov.cn/xxgk/xbjs/index.html?keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = '{"fwzt":3,"highlight":"1","isSearch":"1","tab":"all","subject":"学习考察 考察学习"}'
    post_data = json.loads(post_data)

    scraper = Scraper(city_info, method='post_change', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, is_post_by_json=True)
    scraper.run()
