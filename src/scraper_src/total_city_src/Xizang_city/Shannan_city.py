import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('page', {}).get('content', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('trs_time', '')
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
    请求方法：GET
    获取数据：API
    提取方法：JSON -- data -- data -- title, createDate, url
    """

    city_info = {
        'city_name': '山南市',
        'province_name': '西藏省',
        'province': 'Xizang',

        'base_url': 'http://www.shannan.gov.cn/igs/front/search.jhtml?code=378290858d084b458f18c9f45f320b9f&pageNumber={page_num}&pageSize=10&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=5',

        'total_news_num': 3281,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=rBEABBroZohHRyMjHz1bSUAxj-mWIfoVmkgA; _gscu_971451729=20194917kdjdn012; _trs_uv=ly8vn5mv_2689_l2v4; uuid=c26904c8-cacb-46a1-836a-4d0f71a4b4a7; wzws_sessionid=gDIwMDE6MjUwOjMwMDc6ODAwMTpjOGQzOjUwOTU6MmU3NjoxYTM5gmI3NTc1OIE1ZjQ1OTGgZohHMA==; _gscbrs_971451729=1; _trs_ua_s_1=ly92xm42_2689_4xqh; token=7e95f5a7-2c75-40c7-82e5-cc24bf34ddf3; _gscs_971451729=20207168hmdepi17|pv:2","Host":"www.shannan.gov.cn","Referer":"http://www.shannan.gov.cn/shannan_site/search.html?siteId=5&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pageSize=10&pageNumber=3","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()
