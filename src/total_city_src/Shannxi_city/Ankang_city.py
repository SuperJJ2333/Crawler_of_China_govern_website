import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    data_list = data_list.replace('jQuery171016135784735420122_1720118188747(', '').replace(')', '')

    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('list', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('publicTime', '')
            url = item.get('urlText', '')
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
    提取方法：JSON -- data -- datas -- title, pubDate, url
    """

    city_info = {
        'city_name': '安康市',
        'province_name': '陕西省',
        'province': 'Shannxi',

        'base_url': 'https://so.ankang.gov.cn/Views/searchkjsonp.cshtml?callback=jQuery171016135784735420122_1720118188747&m=&t=0&sid=0&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pageIndex={page_num}&pageSize=20&fullTextType=1&day=&date=&cycle=0&beginDate=&endDate=&year=0&articleNumber=&theme=0&service=0&valid=&weight=1',
        'total_news_num': 100,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"Hm_lvt_f79ed174397504cdc42cb2199a06fa8e=1720118181; Hm_lpvt_f79ed174397504cdc42cb2199a06fa8e=1720118181; HMACCOUNT=A202F23FD4E0D795; ASP.NET_SessionId=1os1ijhv3bz3ejpypgaxhnbo; arialoadData=false","Host":"so.ankang.gov.cn","Referer":"https://so.ankang.gov.cn/s?q=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      proxies=fiddler_proxies, verify=False,
                      )

    scraper.run()