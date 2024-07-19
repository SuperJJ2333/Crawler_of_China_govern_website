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
            topic = item.get('DOCTITLE', '')
            date = item.get('PUBDATE', '')
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
    提取方法：JSON -- page -- content -- title, trs_time, url
    """

    city_info = {
        'city_name': '十堰市',
        'province_name': '湖北省',
        'province': 'Hubei',
        'base_url': 'https://www.shiyan.gov.cn/igs/front/search.jhtml?code=e54c0c0426f7456a86327603ba10c77e&pageNumber={page_num}&pageSize=20&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=71',

        'total_news_num': 38909,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=B7EB4D91DE831EE8BCE2D2F045A3909D; uuid=4d2fbc24-09dc-42de-a066-ebe9580595fb; SESSION=MjlkY2YxZDEtMzk2ZC00ODRkLTk0ODQtNTYyNGI2ODE2YzIx; Hm_lvt_d49d789d7155624a5a39290671927f96=1720895805,1720961608; Hm_lpvt_d49d789d7155624a5a39290671927f96=1720961608; HMACCOUNT=A202F23FD4E0D795; token=f8448fa9-ace0-4e22-baa2-bd6a15eeac0f","Host":"www.shiyan.gov.cn","Referer":"https://www.shiyan.gov.cn/site/qsjs/search.html?siteId=71&pageSize=20&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pageNumber=3","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}
    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()