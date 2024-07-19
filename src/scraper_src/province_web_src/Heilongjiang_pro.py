import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('searchResultAll', {}).get('searchTotal', [])

    for item in data_dict:
        try:
            topic = item.get('title', '')
            date = item.get('pubDate', '')
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
    提取方法：JSON -- searchResultAll -- searchTotal -- data：title, fwrq, url
    """

    city_info = {
        'city_name': '黑龙江省',
        'province_name': '黑龙江省',
        'province': 'province_web_data',
        'base_url': 'https://www.hlj.gov.cn/search5/search/s',

        'total_news_num': 930,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"371","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"yfx_c_g_u_id_10000001=_ck24070203030416963145628475696; yfx_sv_c_g_u_id=_ck24070203030416963145628475696; yfx_f_l_v_t_10000001=f_t_1719860584659__r_t_1720533945595__v_t_1720533945595__r_c_1; yfx_mr_10000001=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_mr_f_10000001=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_key_10000001=; JSESSIONID=1E0D8F38DF77E38664A82233F4F188EB; arialoadData=true; route=bea1247a7b00595e282a28e54893eb3b; 2300000061=5a2m5Lmg6ICD5a+fLOiAg+Wvn+WtpuS5oCzlrabkuaDogIPlr58g6ICD5a+f5a2m5Lmg","Host":"www.hlj.gov.cn","Origin":"https://www.hlj.gov.cn","Referer":"https://www.hlj.gov.cn/search5/html/searchResult_heilongjiang.html?siteCode=2300000061&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&column=%2525E5%252585%2525A8%2525E9%252583%2525A8%26&left_right_index=0&searchSource=1","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'searchWord': '%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0', 'siteCode': '2300000061', 'column': '%E5%85%A8%E9%83%A8', 'pageSize': '10', 'pageNum': '2', 'checkHandle': '1', 'searchSource': '0', 'areaSearchFlag': '-1', 'secondSearchWords': '', 'topical': '', 'docName': '', 'label': '', 'countKey': '0', 'uc': '0', 'left_right_index=': '0', 'searchBoxSettingsIndex': '0', 'orderBy': '2', 'startTime': '', 'endTime': '', 'timeStamp': '0', 'strFileType': '', 'wordPlace': '0'}

    page_num_name = 'pageNum'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      verify=False, page_num_start=0)
    scraper.run()