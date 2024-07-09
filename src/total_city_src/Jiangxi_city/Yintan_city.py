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
                url = 'http://www.yingtan.gov.cn/jsearchfront/' + url

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
        'city_name': '鹰潭市',
        'province_name': '江西省',
        'province': 'Jiangxi',
        'base_url': 'http://www.yingtan.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 2000,

        'each_page_news_num': 15,
    }

    headers = {
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Content-Length": "175",
  "Content-Type": "application/x-www-form-urlencoded",
  "Cookie": "JSESSIONID=CB041C786E5227CD296157429B3B420F; user_sid=22b1d170dee04da39b5d4c692427abf4; user_cid=672a99f6e93347d8be002379abc60845; _city=%E5%B9%BF%E5%B7%9E%E5%B8%82; sid=a52a2e6cd9830c23ff21a76010aa31ab; hq=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F; searchsign=5afe10977b504deaa9c5b80744440443; zh_choose_1=s",
  "Host": "www.yingtan.gov.cn",
  "Origin": "http://www.yingtan.gov.cn",
  "Proxy-Connection": "keep-alive",
  "Referer": "http://www.yingtan.gov.cn/jsearchfront/search.do?websiteid=360600000000000&searchid=8&pg=&p=1&tpl=144&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pq=&oq=&eq=&pos=&begin=20200101&end=20201231",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
  "X-Requested-With": "XMLHttpRequest"
}
    post_data = {'websiteid': '360600000000000', 'q': '学习考察 考察学习', 'p': '2', 'pg': '15', 'cateid': '2', 'pos': '', 'pq': '', 'oq': '', 'eq': '', 'begin': '', 'end': '', 'tpl': '144'}

    page_num_name = 'p'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name)
    scraper.run()
