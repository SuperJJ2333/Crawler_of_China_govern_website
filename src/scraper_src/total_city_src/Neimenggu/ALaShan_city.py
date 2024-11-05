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
            date_search = re.search(r'class="jcse-news-date">([\d-]+)</span>', news_item)
            date = date_search.group(1) if date_search else "No date found"

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
        'city_code': 337,
        'city_name': '阿拉善盟',
        'province_name': '内蒙古省',
        'province': '内蒙古省',

        'base_url': 'https://www.als.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 15,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"119","Content-Type":"application/x-www-form-urlencoded","Cookie":"JSESSIONID=571C67DF1BA35E3B1AE3A37091B2CE79; user_sid=1a830f6c85084517a629fadc875b99fa; user_cid=0abd7744ee5249cdb155f1edfb7e6dd5; _city=%E5%B9%BF%E5%B7%9E%E5%B8%82; hq=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; searchsign=7de32632817c420d9d9ea49ab8d40547; sid=6008ce0308cc193c452c5fe7e64e6033; zh_choose_1=s","Host":"www.als.gov.cn","Origin":"https://www.als.gov.cn","Referer":"https://www.als.gov.cn/jsearchfront/search.do?websiteid=152900000000000&searchid=1&pg=&p=1&tpl=23&cateid=1&total=&q=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pq=&oq=&eq=&pos=&begin=&end=","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = 'websiteid=152900000000000&q=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&p=1&pg=20&cateid=1&pos=&pq=&oq=&eq=&begin=&end=&tpl=23'

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