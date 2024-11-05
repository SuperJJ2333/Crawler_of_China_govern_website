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
        'city_code': 333,
        'city_name': '巴音郭楞蒙古自治州',
        'province_name': '新疆省',
        'province': '新疆省',
        'base_url': 'http://xjbz.gov.cn/search5/search/s',

        'total_news_num': 31,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Content-Length":"383","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"yfx_c_g_u_id_10000089=_ck24110122402012515154755138524; _gscu_915820984=304720208lig2c16; _gscbrs_915820984=1; _gscs_915820984=30713232zsw0oz16|pv:1; yfx_f_l_v_t_10000089=f_t_1730472020251__r_t_1730713234934__v_t_1730713234934__r_c_1; JSESSIONID=2E7D88FAA0B53999DD063E4348E042ED; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; 6528000001=6ICD5a+f5a2m5LmgLOWtpuS5oOiAg+Wvnw==","Host":"xjbz.gov.cn","Origin":"http://xjbz.gov.cn","Proxy-Connection":"keep-alive","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","X-Requested-With":"XMLHttpRequest"}

    post_data = 'searchWord=%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&siteCode=6528000001&column=%25E5%2585%25A8%25E9%2583%25A8&pageSize=10&pageNum=1&sonSiteCode=&checkHandle=1&searchSource=0&areaSearchFlag=0&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index%3D=0&searchBoxSettingsIndex=&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=0'

    post_data = json.dumps(post_data)

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