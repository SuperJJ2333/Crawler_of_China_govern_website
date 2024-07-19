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

        if url.startswith('http') is False:
            url = 'http://www.dongying.gov.cn/jsearchfront' + url

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
        'city_name': '东营市',
        'province_name': '山东省',
        'province': 'Shandong',
        'base_url': 'http://www.dongying.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 2897,
        'each_page_news_num': 10,
    }

    headers = {"Host":"www.dongying.gov.cn","Connection":"keep-alive","Content-Length":"217","Accept":"application/json, text/javascript, */*; q=0.01","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","Content-Type":"application/x-www-form-urlencoded","Origin":"http://www.dongying.gov.cn","Referer":"http://www.dongying.gov.cn/jsearchfront/search.do?websiteid=370500000000000&searchid=4954&pg=&p=3&tpl=2142&cateid=14400&total=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pq=&oq=&eq=&dimension_filenumber=&dimension_fbjg=&pos=title%2Ccontent&begin=&end=","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"user_cid=7039879a656c4a9db5830cb3363c06e3; hq=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; user_sid=b61c0ac3254b4ce3bfb584145c5113af; sid=b1012adc335a3d46c797a0224dccd4e0; JSESSIONID=9F2C765E0575840935236BF31DFD9FF9; _city=%E5%B9%BF%E5%B7%9E%E5%B8%82; searchsign=cc03d09c7cc945b6b54f280c485d7e9d; zh_choose_207=s"}

    post_data = {'websiteid': '370500000000000', 'q': '学习考察 考察学习', 'p': '3', 'pg': '10', 'cateid': '14400', 'pos': 'title,content', 'pq': '', 'oq': '', 'eq': '', 'begin': '', 'end': '', 'tpl': '2142', 'dimension_filenumber': '', 'dimension_fbjg': ''}

    page_num_name = 'p'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      verify=False, proxies=fiddler_proxies, thread_num=1)
    scraper.run()