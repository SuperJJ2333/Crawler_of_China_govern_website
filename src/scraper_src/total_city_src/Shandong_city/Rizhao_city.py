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
                url = 'http://www.rizhao.gov.cn/jsearchfront/' + url
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
        'city_name': '日照市',
        'province_name': '山东省',
        'province': 'Shandong',
        'base_url': 'http://www.rizhao.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 10222,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"163","Content-Type":"application/x-www-form-urlencoded","Cookie":"user_cid=c1905a6db60a4a269e1e195e0ce77359; hq=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; user_sid=7f1a910b33fa482195827f11ab0e35b6; _city=%E5%B9%BF%E5%B7%9E%E5%B8%82; sid=6afb0b57cb414d17c50a434250e45221; JSESSIONID=A42A0B2048BF1F2CE72DDD1468CA75A0; searchsign=dfc1aaa895c74c8d87ececbe269cf52a; zh_choose_147=s; wzaFirst=1; _q=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60%3A; zh_choose_undefined=s","Host":"www.rizhao.gov.cn","Origin":"http://www.rizhao.gov.cn","Referer":"http://www.rizhao.gov.cn/jsearchfront/search.do?websiteid=371100000000000&searchid=6269&pg=&p=1&tpl=1541&serviceType=&sortFields=null&pos=title%2Ccontent%2C_default_search&temporaryQ=&standard=&checkError=1&word=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pq=&oq=&eq=&_cus_pq_USELEVEL=&_cus_pq_TYPE=&_cus_pq_SERVICE_OBJECT=&begin=&end=&timeall=","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest"}

    post_data = {'websiteid': '371100000000000', 'q': '学习考察 考察学习', 'p': '1', 'pg': '10', 'cateid': '19481', 'pos': 'title,content,_default_search', 'pq': '', 'oq': '', 'eq': '', 'begin': '', 'end': '', 'tpl': '1541', 'sortFields': 'null'}

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
