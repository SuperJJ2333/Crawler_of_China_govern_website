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
            date = item.get('fwrq', '')
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
        'city_code': 301,
        'city_name': '喀什地区',
        'province_name': '新疆省',
        'province': '新疆省',

        'base_url': 'https://www.kashi.gov.cn/search5/search/s',

        'total_news_num': 12,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"383","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"yfx_c_g_u_id_10000066=_ck24110117285315114681273453713; yfx_f_l_v_t_10000066=f_t_1730453333507__r_t_1730453333507__v_t_1730453333507__r_c_0; JSESSIONID=394A6DE190E0B9564147E3CA23D3B73A; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; 6531000001=5a2m5Lmg6ICD5a+fLOiAg+Wvn+WtpuS5oCzlrabkuaDogIPlr58g6ICD5a+f5a2m5Lmg","Host":"www.kashi.gov.cn","Origin":"https://www.kashi.gov.cn","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = 'searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F&siteCode=6531000001&column=%25E5%2585%25A8%25E9%2583%25A8&pageSize=10&pageNum=1&sonSiteCode=&checkHandle=1&searchSource=0&areaSearchFlag=0&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index%3D=0&searchBoxSettingsIndex=&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=0'

    page_num_name = 'pageNum'
    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      verify=False, proxies=fiddler_proxies, page_num_start=0)
    scraper.run()