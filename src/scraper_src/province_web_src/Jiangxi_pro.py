import json
import re
from html import unescape
from urllib.parse import unquote

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('result', {})

    for item in data_dict:
        # 解码HTML实体
        news_item = unescape(item)
        try:
            # 正则表达式查找URL
            url_search = re.search(r'href="visit/link.do\?url=([^"&]+)', news_item)
            url = unquote(url_search.group(1)) if url_search else "No URL found"

            # 正则表达式查找日期
            date_search = re.search(r'class="jcse-news-date">\s*([\d-]+)\s*</span>', news_item)
            date = date_search.group(1) if date_search else "No date found"

            # 正则表达式查找标题
            title_search = re.search(r'title=([^"&]+)', news_item)
            topic = unquote(title_search.group(1)) if title_search else "No title found"

        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        if not url.startswith('http') and not url.startswith('https'):
            url = 'http://www.gswuwei.gov.cn' + url

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
    提取方法：JSON -- result -- 
            re：unquote：href="visit/link.do\?url=([^"&]+), 
            r'class="jcse-news-date">([\d-]+)</span>', 
            r'&title=(.*?)\">'
    """

    city_info = {
        'city_name': '江西省',
        'province_name': '江西省',
        'province': 'province_web_data',
        'base_url': 'https://sousuo.jiangxi.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 2000,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"176","Content-Type":"application/x-www-form-urlencoded","Cookie":"user_sid=bfce8cc663844a9c93d4fe0e49d07475; user_cid=9a203f8cdfc243409a10da9c2a86efa3; JSESSIONID=6F3206D17FF5DA6C6BACC3CA52908C43; hq=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F; arialoadData=true","Host":"sousuo.jiangxi.gov.cn","Origin":"https://sousuo.jiangxi.gov.cn","Referer":"https://sousuo.jiangxi.gov.cn/jsearchfront/search.do?websiteid=360000000000000&tpl=49&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pos=title&sortType=2","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'websiteid': '360000000000000', 'q': '学习考察考察学习', 'p': '1', 'pg': '20', 'cateid': '921', 'pos': 'title,content,_default_search', 'pq': '', 'oq': '', 'eq': '', 'begin': '', 'end': '', 'tpl': '49', 'sortType': '2'}

    page_num_name = 'p'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, proxies=fiddler_proxies,
                      verify=False)
    scraper.run()