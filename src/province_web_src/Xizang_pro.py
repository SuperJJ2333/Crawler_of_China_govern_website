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
    请求方法：GET
    获取数据：API
    提取方法：JSON -- data -- data -- title, createDate, url
    """

    city_info = {
        'city_name': '西藏藏族自治区',
        'province_name': '西藏藏族自治区',
        'province': 'province_web_data',
        'base_url': 'https://www.xizang.gov.cn/igs/front/search.jhtml?code=30e4960928e74a14a2c05439d100cfc0&pageNumber={page_num}&pageSize=10&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=2',

        'total_news_num': 2367,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"HttpOnly; csrf_cookie=8e1f1513b29f6f47cd3bddcd4408fd92; JSESSIONID=81DE5FFE784B49703D378DB8313ECE30; HttpOnly; csrf_cookie=0de8aea2d2f412fe712b21dc992d8188; HttpOnly; _trs_uv=lyelg189_845_5kpk; Hm_lvt_65b61173ac2f8f060a0a5ead8ba2d472=1720540593; Hm_lpvt_65b61173ac2f8f060a0a5ead8ba2d472=1720540593; HMACCOUNT=A202F23FD4E0D795; arialoadData=false; _trs_ua_s_1=lyer6iud_845_gnu9; token=8282cdf2-d69f-4889-80d9-e16e9fa3e42e; uuid=8282cdf2-d69f-4889-80d9-e16e9fa3e42e; csrf_cookie=5be7c84d31bf0b830fd7cea73f317691; security_session_verify=1b89f151990c731a168e883d51b40be4","Host":"www.xizang.gov.cn","Referer":"https://www.xizang.gov.cn/site/xzzzqrmzf/search.html?searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=2&pageSize=10&pageNumber=3","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()
