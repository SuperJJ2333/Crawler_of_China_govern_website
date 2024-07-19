import json
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

            # 提取标题
            title_tag = soup.find('a', title=True)
            topic = title_tag['title'] if title_tag else None

            # 提取 URL
            url_tag = title_tag['href'] if title_tag else None
            url = url_tag.split('url=')[1].split('&')[0] if url_tag else None
            url = unquote(url)

            # 提取发布日期
            date_tag = soup.find('span', class_='jcse-news-date')
            date = date_tag.text.strip() if date_tag else None
            date = date.split()[-1] if date else None
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
        'city_name': '济南市',
        'province_name': '山东省',
        'province': 'Shandong',
        'base_url': 'http://www.jinan.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 14420,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Content-Length":"210","Content-Type":"application/x-www-form-urlencoded","Cookie":"JSESSIONID=4CCEA98785CAAC894D8CF8D792AF7558; user_sid=b4f6e92f16a24963846bbb234e262dfe; user_cid=fcf5128e26454a27b95186679bcfc06d; _city=%E5%B9%BF%E5%B7%9E%E5%B8%82; sid=b358ffd8828c1ccb33656797d951e539; hq=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; searchsign=8c8059c86d2b4c49be4e00179061b065; http_waf_cookie=3e68bc32-4f72-4dd1e8eda1bb6c02569c94a0ed33704e1c2c; zh_choose_1=s; wondersLog_sdywtb_sdk=%7B%22persistedTime%22%3A1720011769371%2C%22updatedTime%22%3A1720011770173%2C%22sessionStartTime%22%3A1720011770171%2C%22sessionReferrer%22%3A%22http%3A%2F%2Fwww.jinan.gov.cn%2Fjsearchfront%2Fsearch.do%3Fwebsiteid%3D370100000000000%26searchid%3D51%26pg%3D%26p%3D1%26tpl%3D1609%26serviceType%3D%26temporaryQ%3D%26standard%3D%26checkError%3D1%26word%3D%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0%26isConvertPinyin%3D1%26_cus_eq_filenumber%3D%26q%3D%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0%26jgq%3D%26begin%3D%26end%3D%26timetype%3D%26_cus_pq_ja_type%3D%26pos%3Dtitle%26sortType%3D1%26isAccurate%3D0%22%2C%22deviceId%22%3A%223cd4f5e5cd1607a161b575c6b0690bb2-8868%22%2C%22LASTEVENT%22%3A%7B%22eventId%22%3A%22wondersLog_pv%22%2C%22time%22%3A1720011770173%7D%2C%22sessionUuid%22%3A4253687596285717%2C%22costTime%22%3A%7B%7D%7D","Host":"www.jinan.gov.cn","Origin":"http://www.jinan.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.jinan.gov.cn/jsearchfront/search.do?websiteid=370100000000000&searchid=51&pg=&p=1&tpl=1609&serviceType=&temporaryQ=&standard=&checkError=1&word=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&isConvertPinyin=1&_cus_eq_filenumber=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&jgq=&begin=&end=&timetype=&_cus_pq_ja_type=&pos=title&sortType=1&isAccurate=0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest"}

    post_data = {'websiteid': '370100000000000', 'q': '学习考察 考察学习', 'p': '2', 'pg': '10', 'cateid': '1163', 'pos': 'title%2Ccontent', 'tpl': '1609', 'checkError': '1', 'word': '学习考察 考察学习'}

    page_num_name = 'p'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name)
    scraper.run()