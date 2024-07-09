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
            date = item.get('showdate', '')
            url = item.get('linkurl', '')
        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        if url.startswith('http') is False:
            url = 'http://www.jiaozuo.gov.cn' + url

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
        'city_name': '许昌市',
        'province_name': '河南省',
        'province': 'Henan',

        'base_url': 'https://www.xuchang.gov.cn/inteligentsearch/rest/esinteligentsearch/getFullTextDataNew',

        'total_news_num': 2188,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"408","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"sid=5011DDF89F31413BA297CFFBE4269EED; Hm_lvt_a76142de94f0387585b8544497ad6ccb=1719851715; fontZoomState=0; Hm_lpvt_a76142de94f0387585b8544497ad6ccb=1719853832","Host":"www.xuchang.gov.cn","Origin":"https://www.xuchang.gov.cn","Referer":"https://www.xuchang.gov.cn/search/fullsearch.html?wd=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"token":"","pn":20,"rn":10,"wd":"%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","inc_wd":"","exc_wd":"","fields":"title;content","cnum":"001;002;003;004;005;006;007;008;009;010","sort":"","ssort":"title","cl":500,"terminal":"","condition":null,"time":null,"highlights":"title;content","statistics":null,"unionCondition":null,"accuracy":"","noParticiple":"0","searchRange":null}'
    post_data = json.loads(post_data)

    page_num_name = 'pn'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name,
                      num_added_each_time=10, page_num_start=0)
    scraper.run()

