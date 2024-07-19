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
            url = url_tag.get_text(strip=True) if url_tag else None
            date = date_tag.get_text(strip=True) if date_tag else None

            if url.startswith('http') is False:
                url = 'https://www.weihai.gov.cn/jsearchfront/' + url
                url = unquote(url)

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
        'city_name': '滨州市',
        'province_name': '山东省',
        'province': 'Shandong',
        'base_url': 'http://www.binzhou.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 25,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"148","Content-Type":"application/x-www-form-urlencoded","Cookie":"user_sid=c6a009960b1e4a9fb1a61475ee2c68b9; JSESSIONID=9C002F2618C6229263457FB351499096; insert_cookie=36394243; readFlag=1; zh_choose_445=s","Host":"www.binzhou.gov.cn","Origin":"http://www.binzhou.gov.cn","Referer":"http://www.binzhou.gov.cn/zfxxgk/web/","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    post_data = {'websiteid': '371600000000000', 'q': '学习考察 考察学习', 'p': '3', 'pg': '10', 'begin': '', 'end': '', 'cateid': '15763', 'pos': 'title,content,_default_search'}

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
