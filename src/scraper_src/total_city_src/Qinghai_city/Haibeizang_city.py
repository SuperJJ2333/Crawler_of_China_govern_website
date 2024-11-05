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
    提取方法：JSON -- data -- datas -- title, pubDate, url
    """

    city_info = {
        'city_code': 325,
        'city_name': '海北藏族自治州',
        'province_name': '青海省',
        'province': '青海省',

        'base_url': 'https://www.haibei.gov.cn/site/label/8888?labelName=searchDataList&fuzzySearch=false&fromCode=title&showType=2&titleLength=35&contentLength=100&islight=true&isJson=true&pageSize=10&pageIndex={page_num}&isForPage=true&sort=desc&datecode=&typeCode=all&siteId=6796541&columnId=&platformCode=haibei_sys1&isAllSite=true&isForNum=true&beginDate=&endDate=&keywords=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&subkeywords=&orderType=1',
        'total_news_num': 24,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"SHIROJSESSIONID=5b28e7ec-cbcc-4d5d-bd75-4191ad29b66f; JSESSIONID=6072B5DD54CE5494800BB2B811BFC68B; searchHistory=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%2B%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%2C%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Host":"www.haibei.gov.cn","Ls-Language":"zh","Referer":"https://www.haibei.gov.cn/site/search/6796541?siteId=6796541&platformCode=haibei_sys1&isAllSite=true&fuzzySearch=false&sort=intelligent&orderType=0&typeCode=all&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      proxies=fiddler_proxies, verify=False,
                      )

    scraper.run()