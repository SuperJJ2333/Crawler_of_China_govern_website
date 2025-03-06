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
            date = item.get('publishDate', '')
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
    获取数据：HTML
    提取方法：XPATH
    """

    city_info = {
        'city_name': '滁州市',
        'province_name': '安徽省',
        'province': '安徽省',
        'base_url': 'https://www.chuzhou.gov.cn/searchFront/search/doSearch?pageSize=20&contentLength=80&isHighlight=1&columnId=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E4%BA%A4%E6%B5%81%E5%AD%A6%E4%B9%A0&subkeywords=&typeCode=all&isAllSite=true&platformCode=&siteId=&fromCode=&fuzzySearch=true&datecode=&orderType=0&doColloquialConvert=true&minScore=&fileNums=&publishDepartment=&labelName=searchDataList&isJson=true&isForPage=true&pageIndex={page_num}',
        # 新闻总数
        'total_news_num': 2583,
        'each_page_news_num': 20,
    }

    # content_xpath = {'frames': 'x://*[@class="ls-search-list-container"]/div',
    #                  'title': 'x://ul/li[1]/a',
    #                  'date': ['x://ul/li[3]/span[3]']
    #                  # 'url': 'x://a'
    #                  }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"__jsluid_s=e06d671413fb8b08cf989d36e53ab3a0; search_history=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%2C%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; SHIROJSESSIONID=73c73559-5cb8-47fc-98fa-9030b3f8d9d3; JSESSIONID=CEFFFE85A6445549190F3AFB73ADC57F; __jsl_clearance_s=1720785972.726|0|vklvJS%2FYzA18Y78oFWthkrgfNV0%3D; wzaConfigTime=1720785978162","Host":"www.chuzhou.gov.cn","Referer":"https://www.chuzhou.gov.cn/site/search/2653861?isAllSite=true&platformCode=&siteId=&columnId=&columnIds=&typeCode=&beginDate=&endDate=&fromCode=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&excColumns=&datecode=&sort=intelligent&type=&tableColumnId=&subkeywords=&orderType=0&indexNum=&fileNum=&pid=&language=&oldKeywords=&flag=false&searchType=&searchTplId=&fuzzySearch=true&internalCall=false&pageIndex=6&pageSize=10","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()
