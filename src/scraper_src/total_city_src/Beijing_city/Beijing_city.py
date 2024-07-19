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
        item = item.get('data', {})
        try:
            topic = item.get('titleO', '')
            date = item.get('docDate', '')
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
    提取方法：JSON -- resultDocs -- data：titleO, docDate, url
    """

    city_info = {
        'city_name': '北京市',
        'province_name': '北京市',
        'province': 'Beijing',
        'base_url': 'https://www.beijing.gov.cn/so/ss/query/s',

        'total_news_num': 18749,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"215","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"Path=/; Path=/; __jsluid_s=45a0f96898675f64b491e82661794084; Path=/; JSESSIONID=ZDRmNGZiNjktZDEwYy00YjA5LTkxMDMtOGUyMzIxZWJmZGM5; _va_ref=%5B%22%22%2C%22%22%2C1720249919%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DAn7CU_0ayjEu76wSrBPPVXYl6G9709FjArg70y5_ufooFkPSQ37JOD9JpeBnyFt3%26wd%3D%26eqid%3D8426a2fa000f2a5e000000046688ee36%22%5D; _va_ses=*; arialoadData=false; CPS_SESSION=4D048DC4083B8C474B3DC1E1B0A7A6BB; JSESSIONID=1B90799EBBD6EC91D7A2C478C7572ADB; _va_id=4b30b7418dec575a.1720249919.1.1720249933.1720249919.","Host":"www.beijing.gov.cn","Origin":"https://www.beijing.gov.cn","Referer":"https://www.beijing.gov.cn/so/s?tab=all&siteCode=1100000088&qt=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'tab': 'all', 'siteCode': '1100000088', 'qt': '学习考察 考察学习', 'sort': 'relevance', 'keyPlace': '0', 'locationCode': '110000000000', 'page': '2', 'pageSize': '20', 'ie': '99a53197-6060-45a0-935a-d9ab73662ca3'}

    page_num_name = 'page'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      verify=False, proxies=fiddler_proxies)
    scraper.run()