import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('news', {}).get('list', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('pub_time', '')
            url = item.get('url', '')
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
        'city_name': '广州市',
        'province_name': '广东省',
        'province': 'Guangdong',
        'base_url': 'https://search.gd.gov.cn/api/search/all',

        'total_news_num': 5000,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Content-Type":"application/json","Cookie":"cmssearch_session=CiybehfW28IRa8dA8iO6eCBN6yBwiqTYw8KArFxE; SEARCH_LIST=%5B%22%5Cu5b66%5Cu4e60%5Cu8003%5Cu5bdf%22%2C%22%5Cu8003%5Cu5bdf%5Cu5b66%5Cu4e60%22%5D; XSRF-TOKEN=eyJpdiI6IkZNRFwvSjFkUlpibzVZYVl5ODJUbDZBPT0iLCJ2YWx1ZSI6IkpmazRVNkViWEE3clJmdlNBN1lNOFJmRHJtNnB0V0ptaDRPRlNRS2JPcXh1RVwvOHlwaXJtcVwvR1BuVEZVdlhrUSIsIm1hYyI6IjEyZGI1ZThlNzRkMTgxZWVhYWVkZTc0NzBhZmI2NWZhNjZjOGQ2MWYyZGQ1OGY0NjIyNDQ2YzNhM2VkMDcwM2YifQ%3D%3D","Host":"search.gd.gov.cn","Origin":"https://search.gd.gov.cn","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","X-XSRF-TOKEN":"eyJpdiI6IkZNRFwvSjFkUlpibzVZYVl5ODJUbDZBPT0iLCJ2YWx1ZSI6IkpmazRVNkViWEE3clJmdlNBN1lNOFJmRHJtNnB0V0ptaDRPRlNRS2JPcXh1RVwvOHlwaXJtcVwvR1BuVEZVdlhrUSIsIm1hYyI6IjEyZGI1ZThlNzRkMTgxZWVhYWVkZTc0NzBhZmI2NWZhNjZjOGQ2MWYyZGQ1OGY0NjIyNDQ2YzNhM2VkMDcwM2YifQ==","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"page":"2","keywords":"学习考察 考察学习","sort":"smart","site_id":"2","range":"city","position":"title","service_area":"200","recommand":1,"gdbsDivision":"440000"}'
    post_data = json.loads(post_data)

    page_num_name = 'page'

    province_code = {
        # '深圳': 755,  # 深圳
        # '广州': 200,  # 广州
        # '珠海': 756,  # 珠海
        # '汕头': 754,  # 汕头
        # '佛山': 757,  # 佛山
        '韶关': 751,  # 韶关
        # '湛江': 759,  # 湛江
        # '肇庆': 758,  # 肇庆
        # '江门': 750,  # 江门
        # '茂名': 668,  # 茂名
        # '惠州': 752,  # 惠州
        # '梅州': 753,  # 梅州
        # '汕尾': 660,  # 汕尾
        # '河源': 762,  # 河源
        # '阳江': 662,  # 阳江
        # '清远': 763,  # 清远
        # '东莞': 769,  # 东莞
        # '中山': 760,  # 中山
        # '潮州': 768,  # 潮州
        # '揭阳': 663,  # 揭阳
        # '云浮': 766  # 云浮
    }

    for city_name, city_code in province_code.items():
        post_data['service_area'] = city_code
        city_info['city_name'] = city_name + '市'

        scraper = Scraper(city_info, method='post', data_type='json',
                          headers=headers, extracted_method=extract_news_info, is_headless=False,
                          post_data=post_data, page_num_name=page_num_name, is_post_by_json=True)
        scraper.session.post(url=city_info['base_url'], headers=headers, json=post_data, proxies=scraper.proxies)
        scraper.total_news_num = scraper.session.json.get('data').get('news').get('total')
        scraper.total_page_num = scraper.count_page_num()
        print(f'{city_name}市共{scraper.total_news_num}条新闻，{scraper.total_page_num}页')

        scraper.run()
