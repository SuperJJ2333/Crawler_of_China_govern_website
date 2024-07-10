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
            date_search = re.search(r'class="jcse-news-date"[^>]*>\s*([^<]+)\s*</span>', news_item)
            date = date_search.group(1).strip() if date_search else "No date found"

            # 正则表达式查找标题
            title_search = re.search(r'&title=(.*?)\">', item)
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
        'city_name': '江苏省',
        'province_name': '江苏省',
        'province': 'province_web_data',
        'base_url': 'https://www.jiangsu.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 57,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"131","Content-Type":"application/x-www-form-urlencoded","Cookie":"user_sid=f633d8b2367d4c59aa8fbaf8d52ed1b4; sid=16c73bade5ee5ed9c54941a21a5edc66; searchsign=5f57293ebcb04b758b517f6b6305b107; __jsluid_s=e43577ce4ae108f7e71ad2007dc6528b; d7d579b9-386c-482a-b971-92cad6721901=WyI0MjIyMDUwNDUiXQ; zh_choose_1=s; arialoadData=true; ariawapChangeViewPort=false; CUSSESSIONID=15a9d531-76dc-4448-9940-42e5272419d5; _q=%u8003%u5BDF%u5B66%u4E60%3A%u5B66%u4E60%u8003%u5BDF%3A","Host":"www.jiangsu.gov.cn","Origin":"https://www.jiangsu.gov.cn","Referer":"https://www.jiangsu.gov.cn/jsearchfront/search.do?websiteid=320000000100000&searchid=12&pg=&p=2&tpl=38&serviceType=&cateid=20&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&pq=&oq=&eq=&pos=&sortType=0&begin=&end=","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'websiteid': '320000000100000', 'q': '学习考察', 'p': '2', 'pg': '20', 'cateid': '20', 'pos': '', 'pq': '', 'oq': '', 'eq': '', 'begin': '', 'sortType': '0', 'end': '', 'tpl': '38'}

    page_num_name = 'p'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name)
    scraper.run()