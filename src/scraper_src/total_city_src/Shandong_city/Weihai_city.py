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
        'city_name': '威海市',
        'province_name': '山东省',
        'province': 'Shandong',
        'base_url': 'https://www.weihai.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 6833,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"185","Content-Type":"application/x-www-form-urlencoded","Cookie":"JSESSIONID=CDA7FA12189279CC041920EB339A51CB; user_sid=077a0f6e7a6b42a2a0367f395bc63042; user_cid=396a4abda34742d6a1481388def2f8a3; hq=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; _searchtools=close; searchsign=aeca814fede344cd804cc2ba762945ce; sid=039a198845680ddf8854f97236150389; zh_choose_78=s; zh_choose_undefined=s","Host":"www.weihai.gov.cn","Origin":"https://www.weihai.gov.cn","Referer":"https://www.weihai.gov.cn/jsearchfront/search.do?websiteid=371000000000000&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&p=3&pg=20&cateid=386&pos=title&tpl=1321&checkError=1&word=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}\

    post_data = {'websiteid': '371000000000000', 'q': '学习考察 考察学习', 'p': '3', 'pg': '20', 'cateid': '386', 'tpl': '1321', 'checkError': '1', 'word': '学习考察 考察学习'}

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
