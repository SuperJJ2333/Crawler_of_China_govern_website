import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('data', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('docpubtime', '')
            url = item.get('docpuburl', '')
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
    提取方法：JSON -- data -- data -- title, createDate, url
    """

    city_info = {
        'city_name': '吕梁市',
        'province_name': '山西省',
        'province': 'Shanxi',

        'base_url': 'http://www.lvliang.gov.cn/trs-search/trssearch/v2/searchAll.do?siteId=5&searchTag=all&allKeywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&fullKeywords=&orKeywords=&notKeywords=&sort=&position=0&organization=&pageNum={page_num}&pageSize=10&zcYear=&isAlways=1&fileTag=',

        'total_news_num': 1434,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"_gscu_1275628695=201131543nvgkc38; _gscbrs_1275628695=1; _gscs_1275628695=20113154p1ldsi38|pv:1; _trs_uv=ly7iykh7_1490_1rl7; _trs_ua_s_1=ly7iykh7_1490_7gqk","Host":"www.lvliang.gov.cn","Referer":"http://www.lvliang.gov.cn/search-web/","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()