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
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '宿州市',
        'province_name': '安徽省',
        'province': '安徽省',
        'base_url': 'https://www.ahsz.gov.cn/searchFront/search/doSearch?_=0.6272443798444927&pageSize=20&contentLength=80&isHighlight=1&columnId=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E4%BA%A4%E6%B5%81%E5%AD%A6%E4%B9%A0&subkeywords=&typeCode=all&isAllSite=true&platformCode=&siteId=&fromCode=&fuzzySearch=false&sortOrder=desc&datecode=&startDate=&endDate=&orderType=1&doColloquialConvert=true&fileNums=&publishDepartment=&isCollapse=0&minScore=0&newZwfwInfo=false&pageIndex={page_num}',
        'total_news_num': 4356,

        'each_page_news_num': 20,
    }

    content_xpath = {'frames': 'x://*[@id="search_list"]/ul',
                     'title': 'x://li[1]/a',
                     'date': ['x://li[3]/span[2]', 'x://li[2]/span[2]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"wzws_sessionid=oGZ/8PaAMjIxLjQuMzIuMjSCNzg1Y2M5gTVmNDU5MQ==; SHIROJSESSIONID=e22d7e5a-3328-428e-bf50-ce40a300e305; Hm_lvt_44a621db3972c11cb1cfdf26b27a9261=1719660793; wzaConfigTime=1719660794195; search_history=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; Hm_lpvt_44a621db3972c11cb1cfdf26b27a9261=1719660815","Host":"www.ahsz.gov.cn","Referer":"https://www.ahsz.gov.cn/site/search/11708048?typeCode=all&oldKeywords=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&beginDate=&endDate=&fromCode=title&sort=desc&fuzzySearch=false&colloquial=true&orderType=1&models=news%2CworkGuide%2Cpublic_content%2CmessageBoard&isAllSite=true&platformCode=&siteId=&columnId=&subkeywords=","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()