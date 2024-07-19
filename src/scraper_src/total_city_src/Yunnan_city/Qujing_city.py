import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('datas', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('inputdate', '')
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
    提取方法：JSON -- data -- data -- title, createDate, url
    """

    city_info = {
        'city_name': '曲靖市',
        'province_name': '云南省',
        'province': 'Yunnan',

        'base_url': 'https://www.qj.gov.cn/html/ss/search.html?doctitle=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0',

        'total_news_num': 49,
        'each_page_news_num': 15,
    }

    content_xpath = {'frames': 'x://*[@id="jsearch-result-items"]/div',
                     'title': 'x://div[2]/a',
                     'date': ['x://div[3]/div[1]/span'],
                     'next_button': 'x://a[contains(text(),"下一页")]',
                     # 'url': 'x://a'
                     }

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    listen_name = 'www.qj.gov.cn/s/searchall.php'

    scraper = Scraper(city_info, method='listen', data_type='json',
                      content_xpath=content_xpath, is_headless=False, listen_name=listen_name,
                      extracted_method=extract_news_info)

    scraper.method_LISTEN()
    scraper.save_files()