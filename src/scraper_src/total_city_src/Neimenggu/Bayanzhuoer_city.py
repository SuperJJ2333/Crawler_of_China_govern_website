import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('obj', {}).get('datas', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('createDate', '')
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
        'city_name': '巴彦淖尔市',
        'province_name': '内蒙古省',
        'province': 'Neimenggu',
        'base_url': 'https://www.bynr.gov.cn/webServices/search/5030?content=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&startDate=&endDate=2024-07-15%2019:50:08&pager.offset={page_num}&channelid=&searchField=&sortFields=&orders=',

        'total_news_num': 997,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"wzws_sessionid=gTVmNDU5MYAyMDAxOjI1MDozMDA3OjgwMDE6YTRjODpkNjIyOmFjM2M6YzU0M6Bmh+oJgjM1NDk1OQ==; Hm_lvt_90475ab6bf9eae9dfbf09d9b720c5c3e=1720183302; HMACCOUNT=A202F23FD4E0D795; arialoadData=false; AGILE_SID=EE4C35A3BC39BC68F40DB78219CCF51E; USER_TOKEN=67ffa59a358b4699ac44bf73480178e1; AGILE_SID_SHIRO=4955f688-3fa4-4d25-9026-4896d57b29fc; Hm_lpvt_90475ab6bf9eae9dfbf09d9b720c5c3e=1720183338","Host":"www.bynr.gov.cn","Referer":"https://www.bynr.gov.cn/web/search/5030?content=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}
    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      page_num_start=0, num_added_each_time=10)

    scraper.run()
