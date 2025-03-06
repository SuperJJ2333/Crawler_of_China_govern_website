import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('resultDocs', {})

    for item in data_dict:
        try:
            topic = item.get('data', {}).get('titleO', '')
            date = item.get('data', {}).get('docDate', '')
            url = item.get('data', {}).get('url', '')
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
    获取数据：API 
    提取方法：JSON -- datas -- _doctitle, docreltime, docpuburl
    """

    city_info = {
        'city_name': '龙岩市',
        'province_name': '福建省',
        'province': 'Fujian',
        'base_url': 'https://api.so-gov.cn/query/s',

        'total_news_num': 3370,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"718","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"Secure; _gscu_1267028586=19767212hsc8mw25; BFreeTip=1; BFreeDialect=0","Host":"www.fujian.gov.cn","Origin":"https://www.fujian.gov.cn","Referer":"https://www.fujian.gov.cn/ssp/main/index.html?key=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&siteId=ff808081624641aa0162476c0e0e0055&isMain=","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = 'siteCode=3500000049&tab=sxq&qt=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E4%BA%A4%E6%B5%81%E5%AD%A6%E4%B9%A0&SHI=%E9%BE%99%E5%B2%A9%E5%B8%82&keyPlace=0&sort=relevance&fileType=&timeOption=0&locationCode=350000&page=1&pageSize=20&ie=9d003b5b-43c7-4fa2-91bb-29e4d0f6ec79'
    page_num_name = 'page'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name)
    scraper.run()