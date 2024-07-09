import json
import re
from html import unescape

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('searchResult', {}).get('result', {})

    for item in data_dict:
        # 解码HTML实体
        news_item = unescape(item)
        try:
            title_search = re.search(r'data-title="([^"]+)"', news_item)
            topic = title_search.group(1) if title_search else "No title found"

            # 正则表达式查找日期
            date_search = re.search(r'时间:(\d{4}-\d{2}-\d{2})', news_item)
            date = date_search.group(1) if date_search else "No date found"

            url_search = re.search(r'href="([^"]+)"', news_item)
            url = url_search.group(1) if url_search else "No URL found"
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
        'city_name': '平凉市',
        'province_name': '甘肃省',
        'province': 'Gansu',
        'base_url': 'http://www.pingliang.gov.cn/api-gateway/jpaas-jsearch-web-server/interface/search/info?websiteid=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pg=&cateid=faf661dbe7e94a839ac6f7a652de7af4&serviceId=7112f33f9410490396c03839bf99647f&p={page_num}&pos=title&sortType=1',

        'total_news_num': 1172,
        'each_page_news_num': 15,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Content-Type":"application/x-www-form-urlencoded","Cookie":"user_sid=9fa74c8760bf4aa190f1304bbbcd63bb; sessionId=f306ab46beaf4bfc88104847aae1cb3b; searchId=0e98ee1f71124caeaaada2e6bdbb2c9a; zh_choose_undefined=s; _jsearchq=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60%3A%u5B66%u4E60%u8003%u5BDF%3A","Host":"www.pingliang.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.pingliang.gov.cn/api-gateway/jpaas-jsearch-web-server/search?serviceId=7112f33f9410490396c03839bf99647f&cateid=faf661dbe7e94a839ac6f7a652de7af4&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pos=title&sortType=1&p=3","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest"}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()
