import json
import urllib
from urllib.parse import unquote

from bs4 import BeautifulSoup

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('result', {})

    for item in data_dict:

        try:
            soup = BeautifulSoup(item, 'html.parser')

            title_tag = soup.select_one('.jcse-news-title > a')
            url_tag = soup.select_one('.jcse-news-url > a')
            date_tag = soup.select_one('.jcse-news-date')

            topic = title_tag.get_text(strip=True) if title_tag else None
            url = url_tag['href'] if url_tag else None
            date = date_tag.get_text(strip=True) if date_tag else None

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
        'city_name': '烟台市',
        'province_name': '山东省',
        'province': 'Shandong',
        'base_url': 'https://www.yantai.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 3116,
        'each_page_news_num': 15,
    }

    headers = {"Host": "www.yantai.gov.cn",
           "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
           "Accept": "application/json, text/javascript, */*; q=0.01",
           "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest",
           "sec-ch-ua-mobile": "?0",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
           "sec-ch-ua-platform": "\"Windows\"", "Origin": "https://www.yantai.gov.cn", "Sec-Fetch-Site": "same-origin",
           "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty",
           "Referer": "https://www.yantai.gov.cn/jsearchfront/search.do?websiteid=370600000000000&tpl=82&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&p=1&pg=&pos=title&searchid=5&oq=&eq=&begin=&end=",
           "Accept-Encoding": "gzip, deflate, br, zstd",
           "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
           }

    post_data = {'websiteid': '370600000000000', 'q': '学习考察 考察学习', 'p': '3', 'pg': '15', 'cateid': '5', 'pos': 'title', 'pq': '', 'oq': '', 'eq': '', 'begin': '', 'end': '', 'tpl': '82', 'sortFields': ''}

    page_num_name = 'p'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      verify=False, proxies=fiddler_proxies)
    scraper.run()
