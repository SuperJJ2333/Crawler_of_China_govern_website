import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    for item in news_dict.get('data', []).get('data', []):
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
    提取方法：JSON -- data；data --title, createDate, link
    """

    city_info = {
        'city_name': '淮北市',
        'province_name': '安徽省',
        'province': 'Anhui',
        'base_url': 'https://fxsjcj.kaipuyun.cn/logcount.html?website=10007179&server=s1&datatype=click_click&sendid=1719669507777',
        # 新闻总数
        'total_news_num': 1276

        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="search_list"]/ul',
                     'title': 'x://li[1]/a',
                     'date': ['x://li[2]/table//tr[3]/td[2]', 'x://li[3]/span[2]']}

    headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br, zstd",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", "Connection": "keep-alive",
               "Cookie": "Secure; wzws_sessionid=gTVmNDU5MYIxNTdhNTegZn/EFIAyMjEuNC4zMi4yNA==; SHIROJSESSIONID=ffc95a8a-3595-430e-9674-838bdfa30b26; __51uvsct__Jg8io4yQIrMmA7WI=1; __51vcke__Jg8io4yQIrMmA7WI=d1fa0618-dc62-5cef-b521-ebc323e30f01; __51vuft__Jg8io4yQIrMmA7WI=1719649301928; search_history=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F; JSESSIONID=D7E9B94DC9257AA55A0CC93EA4CCB4A6; wzaConfigTime=1719649304182; Secure; __vtins__Jg8io4yQIrMmA7WI=%7B%22sid%22%3A%20%221d238b69-87a5-5c7a-8592-a9fb71ce7953%22%2C%20%22vd%22%3A%202%2C%20%22stt%22%3A%2027878%2C%20%22dr%22%3A%2027878%2C%20%22expires%22%3A%201719651129803%2C%20%22ct%22%3A%201719649329803%7D",
               "Host": "www.huaibei.gov.cn", "Ls-Language": "zh",
               "Referer": "https://www.huaibei.gov.cn/site/search/4697420?fuzzySearch=true&isAllSite=true&sort=intelligent&orderType=0&platformCode=&siteId=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F",
               "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
               "X-Requested-With": "XMLHttpRequest",
               "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
               "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\""}

    # proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}

    scraper = Scraper(city_info, method='get', data_type='json',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      extracted_method=extract_news_info)
    scraper.run()
