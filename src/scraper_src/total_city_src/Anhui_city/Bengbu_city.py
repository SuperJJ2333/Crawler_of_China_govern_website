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
        'city_name': '蚌埠市',
        'province_name': '安徽省',
        'province': '安徽省',

        'base_url': 'https://www.bengbu.gov.cn/site/label/8888?labelName=searchDataList&isJson=true&isForPage=true&target=&pageSize=20&titleLength=35&contentLength=90&showType=2&ssqdDetailTpl=35931&islight=true&columnId=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E4%BA%A4%E6%B5%81%E5%AD%A6%E4%B9%A0&subkeywords=&typeCode=all&isAllSite=true&platformCode=bengbu_gova%2Cbengbu_govb%2Cbengbu_govc%2Cbengbu_govd%2Cbengbu_govf&siteId=&fromCode=&fuzzySearch=false&attachmentType=&datecode=&sort=intelligent&colloquial=true&orderType=0&minScore=&excColumns=6805996%2C6806002&beginDate=&endDate=&pageIndex={page_num}',
        # 新闻总数
        'total_news_num': 3476,
        'each_page_news_num': 20,
        'city_code': 95
    }

    # content_xpath = {'frames': 'x://*[@id="search_hasreslut"]/div[2]/div/div[2]/div[1]/div[2]/ul',
    #                  'title': 'x://li[1]/a',
    #                  'date': ['x://li[4]/span[2]', 'x://li[3]/span[2]']
    #                  # 'url': 'x://a'
    #                  }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"__jsluid_s=6eb95ce8144130e3c25f9904bdc3307e; bengbu_gova_SHIROJSESSIONID=e0201a79-5e06-449a-9c03-d203aa81b065; Hm_lvt_acd9cc04b6e1fdb4fb70c7816a9056f8=1717504785,1719661162; JSESSIONID=FEB428FCDC7D87A7148BC4A5DCFA5965; wzaConfigTime=1719661162660; search_history=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; Hm_lpvt_acd9cc04b6e1fdb4fb70c7816a9056f8=1719661243","Host":"www.bengbu.gov.cn","Referer":"https://www.bengbu.gov.cn/site/search/6795621?beginDate=&endDate=&fromCode=title&fuzzySearch=true&subkeywords=&platformCode=bengbu_gova%2Cbengbu_govb%2Cbengbu_govc%2Cbengbu_govd%2Cbengbu_govf&siteId=&typeCode=all&isAllSite=true&sort=intelligent&orderType=0&siteCode=&sort=intelligent&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    scraper = Scraper(city_info, method='get', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True)

    scraper.run()
