import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('dataList', {})

    for item in data_dict:

        try:
            topic = item.get('xq_title', '')
            date = item.get('xq_pudate', '')
            url = item.get('xq_url', '')

            if url.startswith('http') is False:
                url = 'https://' + url

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
    请求方法：LISTEN
    获取数据：API
    提取方法：JSON -- data -- dataList -- xq_title, xq_pudate, xq_url
    """

    city_info = {
        'city_name': '成都市',
        'province_name': '四川省',
        'province': 'Sichuan',

        'base_url': 'https://www.chengdu.gov.cn/dist/index.html#/?query=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F',

        'total_news_num': 4,
        'each_page_news_num': 20,
    }

    content_xpath = {'frames': 'x://*[@id="jsearch-result-items"]/div',
                     'title': 'x://div[2]/a',
                     'date': ['x://div[3]/div[1]/span'],
                     'next_button': 'x://a[contains(text(),"下一页")]',
                     # 'url': 'x://a'
                     }

    headers = {"Host": "www.lanzhou.gov.cn", "Connection": "keep-alive",
               "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
               "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
               "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1",
               "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate, br, zstd",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
               "Cookie": "user_sid=cc33f3981cbe45a3a5444f2bc4397c84; JSESSIONID=AB6188B0FACC61299ADD71564429407D; rgHdgRP9MKUJO=5ENG936wNNatxBEvbiw936hYCVQAAeDvikAckbNa36NUO49wH8NIFav61vClBEW.Ebx8HjxXZ3DMtzYn3OEwH5A; _gscu_1846752234=19814477162igt90; _gscbrs_1846752234=1; _gscs_1846752234=19814477iu15si90|pv:1; rgHdgRP9MKUJP=5RLxEwDFc1U7qqqDAMH6WHGGoZd1M8koK8hk3YyifcqkVwtVz4Weh2fy4yYlojEJMa9RD3nO_uSxzbE7PTuM7SKftThxBbXjBWqu9h.J2jT5UeFn2pjegGz6JnWSzsRxZF5QTMd9CmA4nfdpMKwBYaaqACZvUl0Go9UXjfb2hoZ6k7u1pskr8DB4IM8.w_966TC56u942RFe68zVfF7Dwrl2uH.tZ64N3JKz_gN5rhk9gMrjW_p6dGcbIJtytD.BSCI3gxjQEf32_H4OGQcjYvbAiuFmq_CAUD0D4aoXLQ6_Y_GHlQnhdtwrbmqLK5Mv8XKtqtAJan5J.esIeKcM0eh"}

    listen_name = 'www.chengdu.gov.cn/v1/query'

    scraper = Scraper(city_info, method='listen', data_type='json',
                      content_xpath=content_xpath, headers=headers, is_headless=False, listen_name=listen_name,
                      extracted_method=extract_news_info)

    scraper.method_LISTEN()
    scraper.save_files()