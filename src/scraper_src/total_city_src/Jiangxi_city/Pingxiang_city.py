from lxml import html

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
            # 解析HTML内容
            doc = html.fromstring(item)

            # 使用XPath提取信息
            topic = doc.xpath('//div[contains(@class, "jcse-news-title")]/a/text()')[0].strip()
            url = doc.xpath('//div[contains(@class, "jcse-news-url")]/a/@href')[0]
            date = doc.xpath('//span[contains(@class, "jcse-news-date")]/text()')[0]

            if url.startswith('http') is False:
                url = 'https://www.pingxiang.gov.cn/jsearchfront/' + url

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
    提取方法：JSON -- result -- html.fromstring：jcse-news-title， jcse-news-url， jcse-news-date
    """

    city_info = {
        'city_name': '萍乡市',
        'province_name': '江西省',
        'province': 'Jiangxi',
        'base_url': 'https://www.pingxiang.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 329,

        'each_page_news_num': 5,
    }

    headers = {
        "Host": "www.pingxiang.gov.cn",
        "sec-ch-ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Origin": "https://www.pingxiang.gov.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.pingxiang.gov.cn/jsearchfront/search.do?websiteid=360300000000000&searchid=126&pg=&p=1&tpl=8&serviceType=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&pq=&oq=&eq=&pos=&begin=20200101&end=20201231",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "JSESSIONID=5B6B19B3D68BE73BF3DF7BDC5CEB04E6; user_sid=eaadb97a2e9a4d50867ac6ca2fd9692f; user_cid=81785146f9034c5eb06ed8e48878112a; searchsign=b86ef2fbe1134e9688d7c1f61774b386; FW9uCWqlVzC22m1KfCMCjfvFHpRMsgt=14faf0a8-26d1-42de-ae13-b151b136719d; dGg2aCfMMK97Ro270mqBFu5qjC8TQbL2opnHvbEpM=Tifz8hd5p4O3AB%2BivrbJpIrUmQqXoggwP2UtfkDHghk%3D; dGg2aCfMMK97Ro270mqBFu5qjC8TQbL2opnHvbEpM=Tifz8hd5p4O3AB%2BivrbJpIrUmQqXoggwP2UtfkDHghk%3D; FW9uCWqlVzC22m1KfCMCjfvFHpRMsgt=14faf0a8-26d1-42de-ae13-b151b136719d"
    }
    post_data = {'websiteid': '360300000000000', 'q': '学习考察', 'p': '2', 'pg': '5',
                 'cateid': '118', 'begin': '0', 'end': '0', 'tpl': '8'}

    page_num_name = 'p'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name)
    scraper.run()
