import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('data', {})

    for item in data_dict:

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
    提取方法：JSON -- resultDocs -- resultDocs -- titleO, docDate, url
    """

    city_info = {
        'city_name': '芜湖市',
        'province_name': '安徽省',
        'province': 'Anhui',
        'base_url': 'https://www.wuhu.gov.cn/whsearch/site/label/8888?_=0.431810624427174&labelName=searchDataList&isJson=true&isForPage=true&target=&pageSize=20&titleLength=35&contentLength=80&showType=2&ssqdDetailTpl=35931&islight=true&columnId=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&subkeywords=&typeCode=all&isAllSite=true&platformCode=&siteId=&fromCode=title&fuzzySearch=true&attachmentType=&datecode=&sort=intelligent&colloquial=true&orderType=0&minScore=&fileNum=&publishDepartment=&pageIndex={page_num}',

        'total_news_num': 2067,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"wh_gova_SHIROJSESSIONID=5c917c7c-5bd2-46fe-ae72-6f54609768e1; wzaConfigTime=1719752261373; search_history=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%40%7C%40%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%40%7C%40%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F","Host":"www.wuhu.gov.cn","Ls-Language":"zh","Referer":"https://www.wuhu.gov.cn/site/search/6787231?keywords=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=&platformCode=&isAllSite=true","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      verify=False, proxies=fiddler_proxies)
    scraper.run()
