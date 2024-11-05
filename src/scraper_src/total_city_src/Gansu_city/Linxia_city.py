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
        'city_code': 322,
        'city_name': '临夏回族自治州',
        'province_name': '甘肃省',
        'province': '甘肃省',

        'base_url': 'https://www.linxia.gov.cn/api-gateway/jpaas-jsearch-web-server/interface/search/info?websiteid=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pg=1&cateid=fd5c7d4e890a47838b6cf24cd5368d9f&serviceId=e57aebea1ed24558a9e6d925187bd897&p={page_num}',
        'total_news_num': 658,
        'each_page_news_num': 1,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Cookie":"user_sid=ca3cfaa27f3942a782484558b1dbd7aa; sessionId=2660f297bd7547af8b8c36e7e3bfb7a5; searchId=a8e8c9e21aba4e6b8046ef123d0384ba; _jsearchq=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60%3A%u8003%u5BDF%u5B66%u4E60%3A%u5B66%u4E60%u8003%u5BDF%3A","Host":"www.linxia.gov.cn","Referer":"https://www.linxia.gov.cn/api-gateway/jpaas-jsearch-web-server/search?serviceId=e57aebea1ed24558a9e6d925187bd897&webid=622900000000&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()