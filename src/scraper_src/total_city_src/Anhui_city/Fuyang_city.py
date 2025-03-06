import json

from scraper.scraper import Scraper

def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('response', {}).get('items', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('releaseDate', '')
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
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '阜阳市',
        'province_name': '安徽省',
        'province': '安徽省',
        'base_url': 'https://www.fy.gov.cn/SearchApi/data?siteName=%E6%9C%AC%E7%AB%99&siteId=1&keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&inResults=&page={page_num}&collection=all&sort=0&fullText=1&fromDays=0&days=0&fuzzy=1',
        # 新闻总数
        'total_news_num': 5000,
        'each_page_news_num': 16,
    }

    # content_xpath = {'frames': 'x://*[@id="search-result"]/div',
    #                  'title': 'x://h3/a',
    #                  'date': ['x://span[3]'],
    #                  'next_button': 'x://span[contains(text(),"下一页")]',
    #
    #                  # 'url': 'x://a'
    #                  }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"wzws_sessionid=gjViMTBhY4AyMjEuNC4zMi4yNKBmgADhgTVmNDU5MQ==; FYSESSID=l0pentiue2katu5igje36a9vs0; Hm_lvt_47f0853208dd4de1ee348e52899781d0=1717656926,1719664866; arialoadData=false; history=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0+%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; wzws_cid=bcb08a7dd60df3215266c3e31a97ef89d5e724c773537750922bf940f54fad881c7df84b81ec283cabd148b69d7875b606cb3f5e6acd87bbefef9c012e029a16b85c4edc1c2a4296f9dd96c3a4887f43; Hm_lpvt_47f0853208dd4de1ee348e52899781d0=1719664937","Host":"www.fy.gov.cn","Referer":"https://www.fy.gov.cn/index.php?c=search&site_id=543740479a05c26f4be2861a&type=&keywords=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&sort=&field=title&forceSearch=&wrongSearch=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()
