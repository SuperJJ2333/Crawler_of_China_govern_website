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
        'city_name': '荆门市',
        'province_name': '湖北省',
        'province': 'Hubei',
        'base_url': 'https://www.jingmen.gov.cn/JSEARCHFRONT/interfaces/cateSearch.do',

        'total_news_num': 1500,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"206","Content-Type":"application/x-www-form-urlencoded","Cookie":"JSESSIONID=6E5BE36F211D10891B432CDE7EEF558D; user_sid=af3bb6214f7b4043a915e13deb79cb65; user_cid=4a3aa197a6524a4096d016c2d4cbb09d; searchsign=b543a1e7fe5743c985f1b80bd333edff; hq=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6; _CLTJ_6fef=zk7g5cTIfI; Hm_lvt_d921f686cee12cfb5ec38ea5b128d6ae=1718374028,1720965382; Hm_lpvt_d921f686cee12cfb5ec38ea5b128d6ae=1720965382; HMACCOUNT=A202F23FD4E0D795","Host":"www.jingmen.gov.cn","Origin":"https://www.jingmen.gov.cn","Referer":"https://www.jingmen.gov.cn/JSEARCHFRONT/search.do?websiteid=420800000000000&searchid=2&pg=&p=1&tpl=56&serviceType=&temporaryQ=&standard=&checkError=1&word=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&jgq=&pos=title%2Ccontent%2Cfilenumber","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'websiteid': '420800000000000', 'q': '学习考察 考察学习', 'p': '3', 'pg': '10', 'cateid': '2', 'pos': 'title,content,filenumber', 'tpl': '56', 'checkError': '1', 'word': '学习考察 考察学习'}

    page_num_name = 'p'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name)
    scraper.run()