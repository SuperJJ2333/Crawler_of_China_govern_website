import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('pageData', {}).get('data', [])

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('updateDate', '')
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
    提取方法：JSON -- page -- content -- title, trs_time, url
    """

    city_info = {
        'city_name': '黄冈市',
        'province_name': '湖北省',
        'province': 'Hubei',
        'base_url': 'https://www.hg.gov.cn/s/so?allSite=true&correction=true&searchLabelType=ALL&keywords=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pageIndex={page_num}&pageSize=15&siteId=6799394&platformCode=hg-szf&beginDate=&endDate=&sortField=&fuzzySearch=false&fromCode=&orderType=0&sortOrder=&organName=&themeName=&catName=&columnId=',

        'total_news_num': 472,
        'each_page_news_num': 15,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"SESSION=MTk2NGRkODYtZjUwNy00YTg1LTk1NmItMDhkMDVhMjUyNjQ3; hg-xxgk_SHIROJSESSIONID=b68db913-d3a9-474b-9b6e-f2ca23b29604; SESSION=MGVkMjdiZWEtNzdkOC00ZWM5LWE0NWYtOTExYTlkNTE5OTcy; hg-szf_SHIROJSESSIONID=aa36f8fc-ff31-457a-b6e3-fce5c1bf71db; JSESSIONID=344F5E9258FB0A10119E632EC906F93B; wzaConfigTime=1720969273176; searchHistory=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%2C%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Host":"www.hg.gov.cn","Ls-Language":"zh","Referer":"https://www.hg.gov.cn/site/search/6799394?allSite=true&isAllSite=true&correction=true&searchLabelType=ALL&fuzzySearch=false&fromCode=content&orderType=0&siteId=6799394&platformCode=hg-szf&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()