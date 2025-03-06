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
            date = item.get('createDate', '')
            url = item.get('link', '')
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
        'city_name': '黄山市',
        'province_name': '安徽省',
        'province': '安徽省',
        'base_url': 'https://www.huangshan.gov.cn/site/label/8888?labelName=searchDataList&fuzzySearch=false&level=&fromCode=title&showType=2&titleLength=35&contentLength=100&islight=true&isJson=true&pageSize=10&pageIndex={page_num}&isForPage=true&sort=intelligent&datecode=&typeCode=all&siteId=&columnId=&catIds=&platformCode=&isAllSite=true&isForNum=true&beginDate=&endDate=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&subkeywords=&isAttach=1&colloquial=true&source_code=&orderType=0',
        'total_news_num': 386,
        'each_page_news_num': 10,
    }

    headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br, zstd",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", "Connection": "keep-alive",
               "Cookie": "__51vcke__JgGcfy96JTbhO1ey=0033f738-18da-57df-bbac-1321346626c3; __51vuft__JgGcfy96JTbhO1ey=1717589655157; wzws_sessionid=gDIyMS40LjMyLjI0oGaBiNaBNWY0NTkxgjI1MjhhMw==; huangshan_ex9_1_SHIROJSESSIONID=1af59864-75ec-4ba0-bec8-7dad2894dea0; __vtins__JgGcfy96JTbhO1ey=%7B%22sid%22%3A%20%227cd2b61b-9c49-508d-bcef-e792ac1861f3%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201719767008656%2C%20%22ct%22%3A%201719765208656%7D; __51uvsct__JgGcfy96JTbhO1ey=2; JSESSIONID=579993805B345C7FF10AD0EA693E3559; wzaConfigTime=1719765211289; searchHistory=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0",
               "Host": "www.huangshan.gov.cn", "Ls-Language": "zh",
               "Referer": "https://www.huangshan.gov.cn/site/search/6793336?isAllSite=true&siteId=&platformCode=&fuzzySearch=false&sort=desc&orderType=0&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F",
               "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
               "X-Requested-With": "XMLHttpRequest",
               "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
               "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()
