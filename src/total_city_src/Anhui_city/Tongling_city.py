import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('middle', {}).get('listAndBox', {})

    for item in data_dict:
        item = item.get('data', {})
        try:
            topic = item.get('title', '')
            date = item.get('table-7', '')
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
    获取数据：API -- by_json
    提取方法：JSON -- data -- middle -- listAndBox -- title, table-7, url
    """

    city_info = {
        'city_name': '铜陵市',
        'province_name': '安徽省',
        'province': 'Anhui',
        'base_url': 'https://www.tl.gov.cn/irs/front/search',

        'total_news_num': 669,
        'each_page_news_num': 16,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"332","Content-Type":"application/json","Cookie":"__jsluid_s=bfef4eec1ccc0872cf51459dd2368caa; arialoadData=true; ariawapChangeViewPort=true; __jsl_clearance_s=1719763775.991|0|HfJs7pl0Sm9yr38TGDkxOioR06w%3D","Host":"www.tl.gov.cn","Origin":"https://www.tl.gov.cn","Referer":"https://www.tl.gov.cn/home?searchWord=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteid=1678666940295417856&isall=all&isxmt=","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"appendixType":"","beginDateTime":"","codes":"","dataTypeId":8,"configCode":"","endDateTime":"","granularity":"ALL","historySearchWords":[],"isSearchForced":0,"orderBy":"related","enableExactSearch":false,"pageNo":2,"pageSize":16,"searchBy":"title","searchWord":"考察学习","code":"189485830c1","customFilter":{"operator":"or","properties":[]},"filters":[]}'

    post_data = json.loads(post_data)

    page_num_name = 'pageNo'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, proxies=fiddler_proxies, verify=False,
                      is_post_by_json=True)
    scraper.run()
