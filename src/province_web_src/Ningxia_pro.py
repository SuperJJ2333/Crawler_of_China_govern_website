import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('middle', {}).get('list', {})

    for item in data_dict:
        try:
            topic = item.get('title', '')
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
    请求方法：POST -- verify
    获取数据：API -- by_json
    提取方法：JSON -- data -- middle -- listAndBox -- titleO, docDate, url
    """

    city_info = {
        'city_name': '宁夏回族自治区',
        'province_name': '宁夏回族自治区',
        'province': 'province_web_data',
        'base_url': 'https://www.nx.gov.cn/irs/front/search',

        'total_news_num': 283,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Content-Type":"application/json","Cookie":"Path=/; TS01adeb59=014e462434f0186f75324b6de4ad18ed9cd040677a036eb2d112547b56858e4f82bb8f914ee4d33a4d6f98cfa1b1c546aafe71571c; SESSION=ZWE5MjNjYTktMjA0MC00YWU0LWE3YzctZWYyZWMzMGY2ZjQ0; _trs_uv=lyeriqvs_1248_kpnr; TS01a3c590=014e462434f0186f75324b6de4ad18ed9cd040677a036eb2d112547b56858e4f82bb8f914ee4d33a4d6f98cfa1b1c546aafe71571c; _trs_ua_s_1=lyfexskf_1248_8s3e","Host":"www.nx.gov.cn","Origin":"https://www.nx.gov.cn","Referer":"https://www.nx.gov.cn/","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"tenantIds":"19","tenantId":"19","searchWord":"学习考察 考察学习","dataTypeId":4,"historySearchWords":[" 建党100周年","乡村振兴","疫情防控","十四五规划"],"orderBy":"related","searchBy":"all","pageNo":3,"pageSize":10,"endDateTime":"","beginDateTime":"","filters":[],"configTenantId":"19","customFilter":{"operator":"and","properties":[],"filters":[]},"sign":"251374e2-c18f-432c-daa7-5fcbb5d2dff2"}'

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