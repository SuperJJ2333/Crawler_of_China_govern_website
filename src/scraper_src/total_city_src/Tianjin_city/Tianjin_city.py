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
    提取方法：JSON -- data -- datas -- title, pubDate, url
    """

    city_info = {
        'city_name': '天津市',
        'province_name': '天津市',
        'province': 'Tianjin',

        'base_url': 'https://www.tj.gov.cn/igs/front/search.jhtml?code=78778b9ded5140d4984030cf8f469303&pageNumber={page_num}&pageSize=10&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=34&sortByFocus=true&type=35248',

        'total_news_num': 2445,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=DC39242A24A3EF8DFC734418420D5E36; TjElderModelFlag=1; _jc_id.2022102501.6873=01c34d467ac6f9f9.1740930663.; _jc_ses.2022102501.6873=1; _trs_uv=m7rt61ha_3499_demb; _trs_ua_s_1=m7rt61ha_3499_a70x; token=5814bc45-44e4-4342-a641-791e83dba070; uuid=5814bc45-44e4-4342-a641-791e83dba070; wzws_cid=a7ba1cd6a1254c665c99d0343333c12af828ed5269cc3bb2006eff423c1f2fad7ca1cd031970258f89ebd3c7921c455d750df13e498716975768d9b4a4fc932f821d32f42b0fd2e119d17646f2121c63","Host":"www.tj.gov.cn","Referer":"https://www.tj.gov.cn/searchsite/tjzww/search.html?siteId=34&type=35248&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&sortByFocus&pageSize=10&orderBy=&timeOrder=&advancedQuery.includesFull=&position=","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0","sec-ch-ua":"\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      proxies=fiddler_proxies, verify=False,
                      )

    scraper.run()