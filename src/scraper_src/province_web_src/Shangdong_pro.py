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
        'city_name': '山东省',
        'province_name': '山东省',
        'province': 'province_web_data',
        'base_url': 'http://www.shandong.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 16536,
        'each_page_news_num': 12,
    }

    headers = {"Host":"www.shandong.gov.cn","Accept":"application/json, text/javascript, */*; q=0.01","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","Content-Type":"application/x-www-form-urlencoded","Origin":"http://www.shandong.gov.cn","Referer":"http://www.shandong.gov.cn/jsearchfront/search.do?websiteid=370000000088000&searchid=7001&pg=&p=4&tpl=2204&cateid=18021&total=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pq=&oq=&eq=&pos=&sortFields=%5B%7B%27name%27%3A%27top%27%2C%27clause%27%3A1%7D%2C%7B%27name%27%3A%27score%27%2C%27clause%27%3A1%7D%5D&begin=&end=","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"user_cid=28a35ebc52994c4286ecc76b06ae3d23; JSESSIONID=21A724ADF407786AFBF21F9CBA4E2A54; user_sid=e2dc15f0fc8d43c79f4ea0dc28c1af2f; hq=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; _city=%E6%B9%9B%E6%B1%9F%E5%B8%82; searchsign=4fda759909f243678e7d131e486e5303; sid=0e2ce3d580836594cd736545cc808906; flag0=Wed%20Jul%2003%202024%2020:57:52%20GMT+0800%20(%E9%A6%99%E6%B8%AF%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4); _q=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; zh_choose_410=s; wondersLog_sdywtb_sdk=%7B%22persistedTime%22%3A1720011431248%2C%22updatedTime%22%3A1721357342785%2C%22sessionStartTime%22%3A1721357342783%2C%22sessionReferrer%22%3A%22http%3A%2F%2Fwww.shandong.gov.cn%2F%22%2C%22deviceId%22%3A%223cd4f5e5cd1607a161b575c6b0690bb2-6935%22%2C%22LASTEVENT%22%3A%7B%22eventId%22%3A%22wondersLog_pv%22%2C%22time%22%3A1721357342785%7D%2C%22sessionUuid%22%3A6461948045386266%2C%22costTime%22%3A%7B%22wondersLog_unload%22%3A1721357342786%7D%7D; arialoadData=true; Hm_lvt_3147c565b4637bb1f8c07a562a3c6cb7=1720011433,1720067714,1720517439,1721357345; HMACCOUNT=A202F23FD4E0D795; zh_choose_undefined=s; Hm_lpvt_3147c565b4637bb1f8c07a562a3c6cb7=1721357546"}

    post_data = {'websiteid': '370000000088000', 'q': '学习考察考察学习', 'p': '3', 'pg': '12', 'cateid': '18021', 'pos': '', 'pq': '', 'oq': '', 'eq': '', 'begin': '', 'end': '', 'tpl': '2204', 'sortFields': "[{'name':'top','clause':1},{'name':'score','clause':1}]"}

    page_num_name = 'p'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      verify=False, thread_num=2, is_by_requests=True)
    scraper.run()