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
            topic = item.get('title_no_tag', '')
            date = item.get('time', '')
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
    获取数据：API
    提取方法：JSON -- resultDocs -- resultDocs -- titleO, docDate, url
    """

    city_info = {
        'city_name': '海口市',
        'province_name': '海南省',
        'province': 'Hainan',
        'base_url': 'https://www.haikou.gov.cn/irs/front/search',

        'total_news_num': 1607,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"373","Content-Type":"application/json","Cookie":"_trs_uv=ly2yvyo6_1012_j0hw; _trs_ua_s_1=ly2yvyo6_1012_5yi4; arialoadData=false; Hm_lvt_bcf3ba6c604ce01f324388684b34b7e9=1719837577; Hm_lpvt_bcf3ba6c604ce01f324388684b34b7e9=1719837577; membercenterjsessionid=OGZkZjE4NTAtNjE3Ni00NTgzLTg3NTItMDdiZGNhOTQ3NDU1; JSESSIONID=DE2D0C2F4B48EE389E1895D870C46CCE","Host":"www.haikou.gov.cn","Origin":"https://www.haikou.gov.cn","Referer":"https://www.haikou.gov.cn/irs-c-web/search.shtml?code=17d1d69fedf&codes=&configCode=&searchWord=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%20%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&dataTypeId=259&sign=7161b1de-c94e-434e-c1b5-6e5dd509f3c1","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"code":"17d1d69fedf","configCode":"","codes":"","searchWord":"考察学习 学习考察","historySearchWords":["考察学习 学习考察","考察学习","学习考察 考察学习"],"dataTypeId":"259","orderBy":"related","searchBy":"all","appendixType":"","granularity":"ALL","beginDateTime":"","endDateTime":"","isSearchForced":0,"filters":[],"pageNo":2,"pageSize":10}'

    post_data = json.loads(post_data)

    page_num_name = 'pageNo'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, is_post_by_json=True,
                      verify=False, proxies=fiddler_proxies)
    scraper.run()