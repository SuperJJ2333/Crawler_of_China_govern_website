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

        'base_url': 'https://www.tj.gov.cn/igs/front/search.jhtml?code=78778b9ded5140d4984030cf8f469303&pageNumber={page_num}&pageSize=10&position=TITLE&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=34&sortByFocus=true&type=21515',

        'total_news_num': 65,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"JSESSIONID=C01B490354616E6D2A338ABEC63E2880; _trs_uv=lx3lvfkj_5647_h4u; wzws_sessionid=gmY3MjFjYoAyMjEuNC4zMi4yNIE1ZjQ1OTGgZojuQg==; TjElderModelFlag=1; _trs_ua_s_1=ly9se31s_3499_9is1; _jc_ref.2022102501.6873=%5B%22%22%2C%22%22%2C1720249928%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DJIU1PqoHkByglyVUOLP1kfOzn9QAUIH8oz7PKiKCRdW%26wd%3D%26eqid%3Da934c375001f90e7000000046688ee3d%22%5D; _jc_id.2022102501.6873=d5188dd2f02fcb17.1720249928.; _jc_ses.2022102501.6873=1; token=86c03cfc-e73d-4215-87fd-618f6b6619a3; uuid=86c03cfc-e73d-4215-87fd-618f6b6619a3","Host":"www.tj.gov.cn","Referer":"https://www.tj.gov.cn/searchsite/tjzww/search.html?siteId=34&type=21515&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&sortByFocus&pageSize=10&position=TITLE&pageNumber=3","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      proxies=fiddler_proxies, verify=False,
                      )

    scraper.run()