import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('data', {}).get('list', {})

    if len(data_dict) == 0:
        return []

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('pubtime', '')
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
    请求方法：POST
    获取数据：API
    提取方法：JSON -- resultDocs -- resultDocs -- titleO, docDate, url
    """

    city_info = {
        'city_name': '吉林省',
        'province_name': '吉林省',
        'province': 'province_web_data',
        'base_url': 'https://intellsearch.jl.gov.cn/search/index.html?q=101101101100110O100111001100000O1000000000000011O101101111011111O100000O1000000000000011O101101111011111O101101101100110O100111001100000&sttype=',

        'total_news_num': 325,
        'each_page_news_num': 20,
    }

    content_xpath = {'frames': 'x://*[@id="jsearch-result-items"]/div',
                     'title': 'x://div[2]/a',
                     'date': ['x://div[3]/div[1]/span'],
                     'next_button': 'x://a[contains(text(),"下一页")]',
                     # 'url': 'x://a'
                     }

    listen_name = 'intellsearch.jl.gov.cn/api/data/list'

    scraper = Scraper(city_info, method='listen', data_type='json',
                      content_xpath=content_xpath, is_headless=True, listen_name=listen_name,
                      extracted_method=extract_news_info)

    scraper.method_LISTEN()
    scraper.save_files()