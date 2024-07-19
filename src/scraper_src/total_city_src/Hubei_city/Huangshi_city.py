import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('page', {}).get('content', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('trs_time', '')
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
    请求方法：GET
    获取数据：API
    提取方法：JSON -- page -- content -- title, trs_time, url
    """

    city_info = {
        'city_name': '黄石市',
        'province_name': '湖北省',
        'province': 'Hubei',
        'base_url': 'https://www.shiyan.gov.cn/igs/front/search.jhtml?code=e54c0c0426f7456a86327603ba10c77e&pageNumber=3&pageSize=20&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=71',
        'total_news_num': 32582,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"JSESSIONID=AFEA8F358D28D873983C13D411A5E0FA; _trs_uv=lylk3x29_3027_9ssd; _trs_ua_s_1=lylk3x29_3027_90cn; token=4a8188e5-1b62-4638-982b-e2282051aad9; uuid=4a8188e5-1b62-4638-982b-e2282051aad9","Host":"www.huangshi.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.huangshi.gov.cn/SITE/zghs/","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()