import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('searchResultAll', {}).get('searchTotal', [])

    for item in data_dict:
        try:
            topic = item.get('title', '')
            date = item.get('pubDate', '')
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
    请求方法：POST -- verify
    获取数据：API
    提取方法：JSON -- searchResultAll -- searchTotal -- data：title, fwrq, url
    """

    city_info = {
        'city_name': '牡丹江市',
        'province_name': '黑龙江省',
        'province': 'HeiLongJiang',
        'base_url': 'https://www.mdj.gov.cn/search5/search/s',

        'total_news_num': 37,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"411","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"Path=/; Path=/; slb-route=067c760b8b32afeb8cf88f8177435e84; SESSION_WEB_CACHE_KEY=6bd07b9ac4804eb59c68dc7d9ab0797a; JSESSIONID=E5A3758F9C0D6FEEEF3CDC56021EC985; arialoadData=false; 2310000002=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oA==; firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60","Host":"www.mdj.gov.cn","Origin":"https://www.mdj.gov.cn","Referer":"https://www.mdj.gov.cn/search5/html/searchResult_mudanjiang.html?siteCode=2310000002&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'searchWord': '%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0', 'siteCode': '2310000002', 'column': '%E5%85%A8%E9%83%A8', 'pageSize': '10', 'pageNum': '2', 'checkHandle': '1', 'searchSource': '0', 'areaSearchFlag': '0', 'secondSearchWords': '', 'topical': '', 'docName': '', 'label': '', 'countKey': '0', 'uc': '0', 'left_right_index=': '0', 'orderBy': '1', 'startTime': '', 'endTime': '', 'timeStamp': '0', 'strFileType': '', 'wordPlace': '1'}

    page_num_name = 'pageNum'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      verify=False, proxies=fiddler_proxies, page_num_start=0)
    scraper.run()