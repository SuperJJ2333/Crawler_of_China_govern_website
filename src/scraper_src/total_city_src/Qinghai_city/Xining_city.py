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
            date = item.get('PUBDATEformat', '')
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
        'city_name': '西宁市',
        'province_name': '青海省',
        'province': 'Qinghai',
        'base_url': 'https://www.xining.gov.cn/igs/front/search.jhtml?code=76fc023bff5b4e65bcf48c8b08da897d&timeOrder=&siteId=2&WCMSITEID=3&orderBy=&position=TITLE&orderDirection=&orderProperty=&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pageNumber={page_num}&pageSize=10&type=65,68,66,70',

        'total_news_num': 42,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=DCAD95FE659810F5C020BE996AE88BC0; _gscu_1996694622=20239009b15jn317; _gscbrs_1996694622=1; JSESSIONID=6AF22ECEEB26163E5287F3C7BF38E1AB; TrsAccessMonitor=TrsAccessMonitor-1720239015000-1788984554; _gscs_1996694622=t20243159wpws4p17|pv:2; token=31aaf3d3-c23d-4444-99e6-a2b4eebb7adb; uuid=31aaf3d3-c23d-4444-99e6-a2b4eebb7adb","Host":"www.xining.gov.cn","Referer":"https://www.xining.gov.cn/","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()
