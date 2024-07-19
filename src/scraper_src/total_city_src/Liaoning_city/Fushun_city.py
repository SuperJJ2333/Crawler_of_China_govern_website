import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('result', {}).get('records', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('infodate', '')
            url = item.get('linkurl', '')

        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        if url.startswith('http') is False:
            url = 'https://www.fushun.gov.cn' + url

        news_info = {
            'topic': topic,
            'date': date,
            'url': url,
        }
        extracted_news_list.append(news_info)

    return extracted_news_list


if __name__ == '__main__':
    """
    请求方法：POST -- 0
    获取数据：API -- offset
    提取方法：JSON -- resultDocs -- resultDocs -- titleO, docDate, url
    """

    city_info = {
        'city_name': '抚顺市',
        'province_name': '辽宁省',
        'province': 'Liaoning',

        'base_url': 'https://www.fushun.gov.cn/inteligentsearch/rest/inteligentSearch/getFullTextData',

        'total_news_num': 1006,
        'each_page_news_num': 12,
    }

    headers = {"Host":"www.fushun.gov.cn","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","Accept":"application/json, text/javascript, */*; q=0.01","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With":"XMLHttpRequest","sec-ch-ua-mobile":"?0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua-platform":"\"Windows\"","Origin":"https://www.fushun.gov.cn","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://www.fushun.gov.cn/search/fullsearch.html?search=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"userGuid=1047923792; fontZoomState=0; oauthClientId=demoClient; oauthPath=http://10.197.22.69:8080/EWB-FRONT; oauthLoginUrl=http://127.0.0.1:1112/membercenter/login.html?redirect_uri=; oauthLogoutUrl=; noOauthRefreshToken=57dc13cc364c93cde224fb04480e6e32; noOauthAccessToken=18be521d1e0d1c4454db087922def51b"}

    post_data = '{"token":"","pn":20,"rn":10,"sdt":"","edt":"","wd":"%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","inc_wd":"","exc_wd":"","fields":"title;content","cnum":"001;","sort":"","ssort":"title","cl":500,"terminal":"","condition":null,"time":null,"highlights":"title;content","statistics":null,"unionCondition":null,"accuracy":"","noParticiple":"0","searchRange":null}'

    post_data = json.loads(post_data)

    page_num_name = 'pn'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, is_post_by_json=False,
                      num_added_each_time=10, page_num_start=0, proxies=fiddler_proxies,
                      verify=False)
    scraper.run()
