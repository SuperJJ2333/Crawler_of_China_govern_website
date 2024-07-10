import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('news', []).get('list', [])

    for item in data_dict:
        try:
            topic = item.get('title', '')
            date = item.get('pub_time', '')
            url = item.get('post_url', '')
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
    请求方法：POST -- verify
    获取数据：API
    提取方法：JSON -- searchResultAll -- searchTotal -- data：title, fwrq, url
    """

    city_info = {
        'city_name': '广东省',
        'province_name': '广东省',
        'province': 'province_web_data',
        'base_url': 'https://search.gd.gov.cn/api/search/all',

        'total_news_num': 600,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Content-Type":"application/json","Cookie":"cmssearch_session=CiybehfW28IRa8dA8iO6eCBN6yBwiqTYw8KArFxE; SEARCH_LIST=%5B%22%5Cu5b66%5Cu4e60%5Cu8003%5Cu5bdf%22%2C%22%5Cu8003%5Cu5bdf%5Cu5b66%5Cu4e60%22%5D; XSRF-TOKEN=eyJpdiI6IkZNRFwvSjFkUlpibzVZYVl5ODJUbDZBPT0iLCJ2YWx1ZSI6IkpmazRVNkViWEE3clJmdlNBN1lNOFJmRHJtNnB0V0ptaDRPRlNRS2JPcXh1RVwvOHlwaXJtcVwvR1BuVEZVdlhrUSIsIm1hYyI6IjEyZGI1ZThlNzRkMTgxZWVhYWVkZTc0NzBhZmI2NWZhNjZjOGQ2MWYyZGQ1OGY0NjIyNDQ2YzNhM2VkMDcwM2YifQ%3D%3D","Host":"search.gd.gov.cn","Origin":"https://search.gd.gov.cn","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","X-XSRF-TOKEN":"eyJpdiI6IkZNRFwvSjFkUlpibzVZYVl5ODJUbDZBPT0iLCJ2YWx1ZSI6IkpmazRVNkViWEE3clJmdlNBN1lNOFJmRHJtNnB0V0ptaDRPRlNRS2JPcXh1RVwvOHlwaXJtcVwvR1BuVEZVdlhrUSIsIm1hYyI6IjEyZGI1ZThlNzRkMTgxZWVhYWVkZTc0NzBhZmI2NWZhNjZjOGQ2MWYyZGQ1OGY0NjIyNDQ2YzNhM2VkMDcwM2YifQ==","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"page":"4","keywords":"学习考察 考察学习","sort":"smart","site_id":"2","range":"site","position":"title","recommand":1,"gdbsDivision":"440000","service_area":1}'

    post_data = json.loads(post_data)

    page_num_name = 'page'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, is_post_by_json=True)
    scraper.run()