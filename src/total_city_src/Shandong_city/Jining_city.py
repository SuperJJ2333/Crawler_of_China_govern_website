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

            # 提取标题
            title_tag = soup.find('a')
            topic = title_tag.text.strip() if title_tag else None

            # 提取 URL
            # 提取 URL
            url_tag = title_tag['href'] if title_tag else None
            if url_tag:
                parsed_url = urllib.parse.urlparse(url_tag)
                query_params = urllib.parse.parse_qs(parsed_url.query)
                url = query_params.get('url', [None])[0]
                if url:
                    url = urllib.parse.unquote(url)
            else:
                url = None

            # 提取发布日期
            date_tag = soup.find('span', class_='jcse-news-date')
            date = date_tag.text.strip() if date_tag else None
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
        'city_name': '济宁市',
        'province_name': '山东省',
        'province': 'Shandong',
        'base_url': 'https://www.jining.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 1853,
        'each_page_news_num': 12,
    }

    headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br, zstd",
           "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
           "Content-Type": "application/x-www-form-urlencoded",
           "Host": "www.jining.gov.cn", "Origin": "https://www.jining.gov.cn",
           "Referer": "https://www.jining.gov.cn/jsearchfront/search.do?websiteid=370800000000000&searchid=2&pg=&p=3&tpl=101&cateid=297&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pq=&oq=&eq=&pos=title%2Ccontent&begin=&end=",
           "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
           "X-Requested-With": "XMLHttpRequest",
           "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
           "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\""}
    post_data = {'websiteid': '370800000000000', 'q': '学习考察 考察学习', 'p': '2', 'pg': '12', 'cateid': '297', 'pos': 'title,content', 'pq': '', 'oq': '', 'eq': '', 'begin': '', 'end': '', 'tpl': '101'}

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
