import json
import re

from bs4 import BeautifulSoup

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('content', {})

    soup = BeautifulSoup(data_dict, 'html.parser')

    soup2 = BeautifulSoup(soup.contents[0], 'html.parser')

    # 查找所有新闻条目
    news_items = soup2.find_all('li')

    for item in news_items:

        try:
            # 提取标题
            title_tag = item.find('div', class_='titlep').find('a')
            topic = title_tag.text.strip()

            # 提取发布日期
            date_tag = re.search(r'发布时间：(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', item.text)
            date = date_tag.group(1) if date_tag else ''

            # 提取URL
            url = title_tag['href'].strip()
            if not url.startswith('http'):
                url = 'http://www.zg.gov.cn/' + url

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
    提取方法：JSON -- B -- resultDocs -- titleO, docDate, url
    """

    city_info = {
        'city_name': '自贡市',
        'province_name': '四川省',
        'province': 'Sichuan',

        'base_url': 'http://www.zg.gov.cn/search',

        'total_news_num': 277,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"63","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"COOKIE_SUPPORT=true; GUEST_LANGUAGE_ID=zh_CN; Hm_lvt_42d6b817f4e93bdfaee0513e1b272405=1720154426; Hm_lpvt_42d6b817f4e93bdfaee0513e1b272405=1720154426; HMACCOUNT=A202F23FD4E0D795; JSESSIONID=3A528004A4A946838A7CB12ADD0BEC30; Secure","Host":"www.zg.gov.cn","Origin":"http://www.zg.gov.cn","Referer":"http://www.zg.gov.cn/Search?fromAnother=true&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest"}

    post_data = {'Page': '3', 'keywords': '考察学习', 'location': '1'}

    page_num_name = 'Page'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name)
    scraper.run()