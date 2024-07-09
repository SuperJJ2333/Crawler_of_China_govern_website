import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('pageData', {}).get('data', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('publishDate', '')
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
        'city_name': '陇南市',
        'province_name': '甘肃省',
        'province': 'Gansu',
        'base_url': 'https://www.longnan.gov.cn/s/so?allSite=false&correction=true&searchLabelType=ALL&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pageIndex={page_num}&pageSize=12&siteId=4448177&platformCode=&beginDate=&endDate=&sortField=&fuzzySearch=true&fromCode=title&orderType=0&sortOrder=&organName=&themeName=&catName=',

        'total_news_num': 374,
        'each_page_news_num': 12,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"SESSION=MjdhZmVmZjUtYWNmOC00ZTYwLTg2ODUtYTRiZWU4ZDg0YzJl; SHIROJSESSIONID=55308b3f-1b37-418b-b993-47745a4fe3c4; ln-szf_SHIROJSESSIONID=8f1b0a27-c0a0-42d4-9d7a-9de43f3be109; JSESSIONID=F900E409A956E9E8BF5478330CC2750E; searchHistory=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; wzaConfigTime=1719827726750","Host":"www.longnan.gov.cn","Ls-Language":"zh","Referer":"https://www.longnan.gov.cn/site/search/4448177?keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      page_num_start=0)

    scraper.run()
