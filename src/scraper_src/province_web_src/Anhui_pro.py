import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('data', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('createDate', '')
            url = item.get('link', '')
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
        'city_name': '安徽省',
        'province_name': '安徽省',
        'province': 'province_web_data',
        'base_url': 'https://www.ah.gov.cn/anhuisousuoserver/site/label/8888?labelName=searchDataList&isJson=true&isForPage=true&target=&pageSize=20&titleLength=35&contentLength=90&showType=2&ssqdDetailTpl=35931&islight=true&columnId=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&subkeywords=&typeCode=all&isAllSite=true&platformCode=&siteId=&fromCode=&fuzzySearch=true&attachmentType=&datecode=&sort=intelligent&colloquial=true&orderType=0&minScore=&fileNum=&publishDepartment=&pageIndex={page_num}',

        'total_news_num': 25150,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"wzws_sessionid=gDEyMC4yMzYuMTYzLjExMIE1ZjQ1OTGCYWM2NzJmoGaNXXQ=; SHIROJSESSIONID=7edc7aff-ce23-4a42-a7e2-a0ce37e9bbf0; _yfxkpy_ssid_10006888=%7B%22_yfxkpy_firsttime%22%3A%221719585020810%22%2C%22_yfxkpy_lasttime%22%3A%221720540550828%22%2C%22_yfxkpy_visittime%22%3A%221720540550828%22%2C%22_yfxkpy_domidgroup%22%3A%221719756403335%22%2C%22_yfxkpy_domallsize%22%3A%22100%22%2C%22_yfxkpy_cookie%22%3A%2220240628223020814477728376945947%22%2C%22_yfxkpy_returncount%22%3A%223%22%7D; wzaFirst=1; search_history=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%40%7C%40%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%40%7C%40%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; Hm_lvt_03d57a494739d01fa9c3ebedaa6e46bd=1719512291,1719579390,1719649293,1720549556; Hm_lpvt_03d57a494739d01fa9c3ebedaa6e46bd=1720549556; HMACCOUNT=A202F23FD4E0D795","Host":"www.ah.gov.cn","Ls-Language":"zh","Referer":"https://www.ah.gov.cn/site/search/6781961?keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()
