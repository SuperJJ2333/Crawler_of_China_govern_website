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
        'city_name': '淄博市',
        'province_name': '山东省',
        'province': 'Shandong',
        'base_url': 'https://www.zibo.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 1125,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"174","Content-Type":"application/x-www-form-urlencoded","Cookie":"JSESSIONID=F3ADDB267A44A6DC47776BDA96CA77CD; user_sid=06bb5166f2124e0598deb85938b8eb7e; user_cid=2b2a9adc1d0d47da9aadaf225397fbf0; hq=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; _city=; sid=a1657b8cb4ea2cd187734e6f64ca2bb9; searchsign=e246e62e411c45ac87dc2124e5b331cf; zh_choose_1=s; zh_choose_undefined=s; _q=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60","Host":"www.zibo.gov.cn","Origin":"https://www.zibo.gov.cn","Referer":"https://www.zibo.gov.cn/jsearchfront/search.do?websiteid=370300000000000&searchid=1&pg=&p=2&tpl=174&cateid=2&serviceType=&sortFields=&pos=title&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&zcwj-timing=on&zcwj-sort-way=on&zcwj-query-scope=on&pq=&oq=&eq=&mattertype=&begin=&end=&timeall=","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'websiteid': '370300000000000', 'q': '学习考察 考察学习', 'p': '2', 'pg': '', 'cateid': '2', 'pos': 'title', 'pq': '', 'oq': '', 'eq': '', 'begin': '', 'end': '', 'tpl': '174', 'sortFields': ''}

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