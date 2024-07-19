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
        'city_name': '鸡西市',
        'province_name': '黑龙江省',
        'province': 'HeiLongJiang',
        'base_url': 'https://www.jixi.gov.cn/search5/search/s',

        'total_news_num': 458,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"154","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"verid=false; Hm_lvt_3c451c24c7ed71a754f76f948e998416=1719860630; Hm_lpvt_3c451c24c7ed71a754f76f948e998416=1719860630; arialoadData=true; ariawapChangeViewPort=true; HWWAFSESID=7c205738f835401db7; HWWAFSESTIME=1719860638685; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; 2303000003=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oCzlrabkuaDogIPlr58=","Host":"www.jixi.gov.cn","Origin":"https://www.jixi.gov.cn","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'searchWord': '%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0', 'siteCode': '2303000003', 'column': '%E5%85%A8%E9%83%A8', 'pageSize': '10', 'pageNum': '2', 'sonSiteCode': '', 'checkHandle': '1', 'searchSource': '0', 'areaSearchFlag': '0', 'secondSearchWords': '', 'topical': '', 'docName': '', 'label': '', 'countKey': '0', 'uc': '0', 'left_right_index=': '0', 'searchBoxSettingsIndex': '', 'orderBy': '0', 'startTime': '', 'endTime': '', 'timeStamp': '0', 'strFileType': '', 'wordPlace': '1'}

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