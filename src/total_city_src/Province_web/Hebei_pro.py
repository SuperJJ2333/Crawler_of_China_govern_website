import json
import re
from html import unescape

from bs4 import BeautifulSoup

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    soup = BeautifulSoup(news_dict, 'html.parser')

    for item in soup.find_all('li', style="display:block"):
        try:

            title_tag = item.find('a')
            topic = title_tag['title']

            url = title_tag['href']

            date = item.find('span', class_='date').text.strip()
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
    请求方法：GET
    获取数据：API
    提取方法：JSON -- data -- searchResult -- result -- re： data-title=, 时间, href
    """

    city_info = {
        'city_name': '河北省',
        'province_name': '河北省',
        'province': 'Province_web',
        'base_url': 'https://www.hebei.gov.cn/columns/0/templates/b5a0012b-09bd-4038-95df-37c8fd97f2ac/blocks/7054057f-8913-4ee5-8030-a77aeb6be68d?page=2&keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&fix=1',

        'total_news_num': 31,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"Hm_lvt_b95d55e7652e7ba1eca22797968c4a2f=1719840677,1720335005; Hm_lpvt_b95d55e7652e7ba1eca22797968c4a2f=1720335005; HMACCOUNT=A202F23FD4E0D795; arialoadData=[object Object]; q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Host":"www.hebei.gov.cn","Referer":"https://www.hebei.gov.cn/s?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&fix=1","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()