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
    提取方法：JSON -- resultDocs -- data：titleO, docDate, url
    """

    city_info = {
        'city_name': '哈密市',
        'province_name': '新疆省',
        'province': 'Xinjiang',

        'base_url': 'https://www.hami.gov.cn/index_zhsearch.jsp?wbtreeid=1001&keyword=5a2m5Lmg6ICD5a%2Bf&ot=1&rg=2&tg=5&clid=0&currentnum={page_num}',

        'total_news_num': 36,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@class="xwd"]',
                     'title': 'x://div/a',
                     'date': ['x://div[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cache-Control":"max-age=0","Connection":"keep-alive","Content-Length":"78","Content-Type":"application/x-www-form-urlencoded","Cookie":"CTC_SCI=5D60910D7ED65269D2025462262EBF8D0F0D856F8BF0D444E105CFDAA128606FBF6F8B0A9FC1DDD8DA972BCB6448DF55FC3B5560F6F306AC991TZRQ2Uw==; CTC_CAL=119B57F7E93299C185E0E924D799A52AFD492A452A11D6EE09FC7C2D8E1AD05EA9B282350A87334E740TZRQ2Ow==; arialoadData=false; JSESSIONID=6FCC5A93193BC0431194FFA86D0681B5; CTC_JMC=207D78505530E4D0C434F0CFF76DBF21BC6BE9353B0ACD74FB52FD76BC065A1961ATZRQ2Xw==","Host":"www.hami.gov.cn","Origin":"https://www.hami.gov.cn","Referer":"https://www.hami.gov.cn/index_zhsearch.jsp?wbtreeid=1001","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'ot': '1', 'rg': '1', 'tg': '5', 'clid': '0', 'kw': '6ICD5a+f5a2m5Lmg', 'columnCode': '', '_lucenen_search_mixed': ''}

    page_num_name = 'pageNum'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      verify=False, proxies=fiddler_proxies, post_data=post_data,
                      )
    scraper.run()