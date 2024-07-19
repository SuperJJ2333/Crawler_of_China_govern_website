import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = json.loads(news_dict.get('news', '')).get('result', [])

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('inserttime', '')
            url = 'http://www.qhd.gov.cn/front_pcthi.do?uuid=' + item.get('uuid', '')
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
        'city_name': '秦皇岛市',
        'province_name': '河北省',
        'province': 'Hebei',
        'base_url': 'http://www.qhd.gov.cn/front_searchall.do?state=news&pn={page_num}&pageSize=10&query=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F',

        'total_news_num': 226,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"JSESSIONID=54436438BEB9BBDD8ED11FBDC67F21F3; Hm_lvt_8599c84c1638be9987f632573758c412=1719122636,1720871895; HMACCOUNT=A202F23FD4E0D795; qhdnew=039C6834359A84EC96431ABAE052DC36; Hm_lpvt_8599c84c1638be9987f632573758c412=1720871981","Host":"www.qhd.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.qhd.gov.cn/front_searchnews.do?keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&pn=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest"}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()
