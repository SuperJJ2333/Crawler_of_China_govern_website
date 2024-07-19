import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('searchTotal', {})

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
    请求方法：POST
    获取数据：API
    提取方法：JSON -- resultDocs -- resultDocs -- titleO, docDate, url
    """

    city_info = {
        'city_name': '宜春市',
        'province_name': '江西省',
        'province': 'Jiangxi',

        'base_url': 'https://www.yichun.gov.cn/search4/commonAggs',

        'total_news_num': 546,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"495","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"proName=search4/; firstWord=%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60; SECKEY_ABVK=ronpiFc8YLl9QEEwQ/xDFOKkjlI+T4u9aYq6hZ8VNw/9Isy70jmK98bwEJvKmcGyMt6hWTDFtfPwvcCBWGPPVg%3D%3D; HttpOnly; userSearch=siteCode-3609000002&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord-%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240703190605&searchUseTime-162; SESSION_WEB_CACHE_KEY=8ef0cfd77f064570b47023e52a8096ce; Hm_lvt_72920cca32daf35e7e46dfa6ccc27328=1718965996,1720000058; Hm_lpvt_72920cca32daf35e7e46dfa6ccc27328=1720000058; HttpOnly; arialoadData=true; ariawapChangeViewPort=true; HWWAFSESID=54b3076b20eaaad62b; HWWAFSESTIME=1720004556427; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; 3609000002=6ICD5a+f5a2m5LmgLOWtpuS5oOiAg+WvnyzlrabkuaDogIPlr58g6ICD5a+f5a2m5Lmg","Host":"www.yichun.gov.cn","Origin":"https://www.yichun.gov.cn","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'searchWord': '%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0', 'siteCode': '3609000002', 'column': '%E6%94%BF%E5%8A%A1%E5%85%AC%E5%BC%80', 'wordPlace': '0', 'orderBy': '0', 'startTime': '', 'endTime': '', 'pageSize': '10', 'pageNum': '0', 'timeStamp': '0', 'checkHandle': '1', 'strFileType': '', 'areaSearchFlag': '0', 'secondSearchWords': '', 'topical': '', 'docName': '', 'label': '', 'countKey': '0', 'searchBoxSettingsIndex': '', 'manualWord': '%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0'}

    page_num_name = 'pageNum'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, page_num_start=0)
    scraper.run()