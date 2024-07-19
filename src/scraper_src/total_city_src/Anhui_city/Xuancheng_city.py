import json

from scraper.scraper import Scraper

def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('items', {})

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
    提取方法：XPATH - verify；fiddler_proxies
    """

    city_info = {
        'city_name': '宣城市',
        'province_name': '安徽省',
        'province': 'Anhui',
        'base_url': 'https://search.xuancheng.gov.cn/search?keyword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&field=all&inResult=&page={page_num}&siteId=0&fromDays=0',

        'total_news_num': 3649,

        'each_page_news_num': 15,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"SearchHistory=+%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0+'+%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f+%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0+'+%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f+; SearchLog=%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0%2f04052e98dba04244aed59ac01fac3324'%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f+%e8%80%83%e5%af%9f%e5%ad%a6%e4%b9%a0%2f600b6f95bc364829b512f0be5e261059'%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f%2fbce2b6c77353460ab7863151df462c70; Hm_lvt_96da6bb9c6240d1fcc3e26827fb60319=1719756414,1720786711,1720791701; Hm_lpvt_96da6bb9c6240d1fcc3e26827fb60319=1720791701; HMACCOUNT=A202F23FD4E0D795","Host":"search.xuancheng.gov.cn","Referer":"https://search.xuancheng.gov.cn/searchData?keyword=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&field=title","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      proxies=fiddler_proxies, verify=False)

    scraper.run()
