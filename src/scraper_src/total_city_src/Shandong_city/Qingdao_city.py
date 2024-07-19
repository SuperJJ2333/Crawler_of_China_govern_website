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
            date = item.get('fwTime', '')
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
    提取方法：JSON -- data -- data -- title, createDate, url
    """

    city_info = {
        'city_name': '青岛市',
        'province_name': '山东省',
        'province': 'Shandong',

        'base_url': 'http://www.qingdao.gov.cn/igs/front/search.jhtml?code=0060ed3eefe4449c93734b28fab5622a&siteId=5&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pageSize=10&pageNumber={page_num}&type=&zc=&publishTime=&advancedQuery.notIncludes=&advancedQuery.includesAny=&advancedQuery.includesFull=&pubRange=2021-07-17&department=&year=&region=&stillSearching=false&area=+&modal=1',

        'total_news_num': 12434,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"SESSION=b9c88fa9-a5ba-40f0-b098-9fe8cc053b76; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219078bad21766c-0aee4d1db5698f8-4c657b58-1327104-19078bad218a0a%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22%24device_id%22%3A%2219078bad21766c-0aee4d1db5698f8-4c657b58-1327104-19078bad218a0a%22%7D; clientCookie=78e8e0c3af874b97b3622ced9c1bf58a; token=cc6433aa-9593-4b5a-a106-5c84d46f7321; uuid=cc6433aa-9593-4b5a-a106-5c84d46f7321; FanJianChange=jian; _trs_uv=ly5uzovu_4357_djxn; clientIp=45.12.82.199; _trs_ua_s_1=ly63d0s0_4357_1w13; searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Host":"www.qingdao.gov.cn","Proxy-Connection":"keep-alive","Referer":"http://www.qingdao.gov.cn/unionsearch/index.shtml?searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&sitetype=only","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest"}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()
