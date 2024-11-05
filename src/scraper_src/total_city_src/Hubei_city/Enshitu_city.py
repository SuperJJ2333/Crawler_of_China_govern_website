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
    请求方法：POST
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_code': 306,
        'city_name': '恩施土家族苗族自治州',
        'province_name': '湖北省',
        'province': '湖北省',

        'base_url': 'http://www.enshi.gov.cn/igs/front/search.jhtml?code=65bc81e2d67646ed9474dc3df1f150d7&pageNumber={page_num}&pageSize=10&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=2',

        'total_news_num': 1168,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=821D98DBBA4D81055B74AA97A270EE04; SESSION=OTU5ZTljNGUtMTdkYy00YWYwLTk4Y2ItMDM4MzFiODczYzEz; _trs_uv=m2yoprk9_4336_h25i; _trs_ua_s_1=m2yoprk9_4336_hd; Hm_lvt_a55a65eb4b198566d798228ff0d897fc=1730462538; Hm_lpvt_a55a65eb4b198566d798228ff0d897fc=1730462538; HMACCOUNT=3DE9BC176CD975E6; token=8369da01-491a-4d1e-9965-3a07cfb3ae59; uuid=8369da01-491a-4d1e-9965-3a07cfb3ae59","Host":"www.enshi.gov.cn","Referer":"http://www.enshi.gov.cn/site/esz/search.html?searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=2&pageSize=10&pageNumber=2","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      proxies=fiddler_proxies, verify=False,
                      )

    scraper.run()