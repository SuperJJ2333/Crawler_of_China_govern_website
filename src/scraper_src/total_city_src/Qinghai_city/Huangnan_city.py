import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('value', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('adddate', '')
            url = item.get('linkurl', '')

            if not url.startswith('http'):
                url = 'http://www.huangnan.gov.cn' + url
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
    提取方法：JSON -- data -- datas -- title, pubDate, url
    """

    city_info = {
        'city_code': 327,
        'city_name': '黄南藏族自治州',
        'province_name': '青海省',
        'province': '青海省',

        'base_url': 'http://www.huangnan.gov.cn/api/SS.Huangnan/dynamics/search?&range=All&type=Title&word=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pagesize=10',
        'total_news_num': 2,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Host":"www.huangnan.gov.cn","Referer":"http://www.huangnan.gov.cn/utils/Search.html?type=Title&words=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      proxies=fiddler_proxies, verify=False,
                      )

    scraper.run()