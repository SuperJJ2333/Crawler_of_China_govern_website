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
        'city_name': '马鞍山市',
        'province_name': '安徽省',
        'province': 'Anhui',
        'base_url': 'https://www.mas.gov.cn/site/label/8888',
        # 新闻总数
        'total_news_num': 227,
        'each_page_news_num': 10,
    }

    content_xpath = {'frames': 'x://*[@id="search_hasreslut"]/div[2]/div/div[2]/div[1]/div[2]/ul',
                     'title': 'x://li[1]/a',
                     'date': ['x://li[4]/span[2]', 'x://li[3]/span[2]'],
                     # 'url': 'x://a'，
                     'next_button': 'x://*/a[text()="下一页"]'
                     }

    listen_name = 'www.mas.gov.cn/site/label/8888'

    post_data = {'labelName': 'searchDataList', 'fromCode': 'title', 'showType': '2', 'titleLength': '35', 'contentLength': '100', 'islight': 'true', 'isJson': 'true', 'pageSize': '10', 'pageIndex': '2', 'isForPage': 'true', 'sort': 'intelligent', 'datecode': '', 'typeCode': 'articleNews,pictureNews,videoNews,policyDoc,explainDoc,dataOpen,bbs,public_content,messageBoard,interviewInfo,collectInfo,survey,knowledgeBase', 'siteId': '4697368', 'columnId': '', 'platformCode': '', 'isAllSite': 'false', 'isForNum': 'true', 'beginDate': '', 'endDate': '', 'keywords': '学习考察 考察学习', 'subkeywords': '', 'fuzzySearch': 'true', 'colloquial': 'true', 'excColumns': '4718732,4718799,4718800,4718801,4718802,4718803,4718804,4718805,4718809,4718812,4718818,4718824,4718806,4718810,4718813,4718819,4718825,4718807,4718811,4718814,4718820,4718826,4718808,4718815,4718821,4718827,4718864,4718816,4718822,4718817,4718823', 'isSkipConvert': 'false', 'privacyOpen': 'true'}

    page_num_name = 'pageIndex'

    # scraper = Scraper(city_info, method='Listen', data_type='json',
    #                   content_xpath=content_xpath, is_headless=True,
    #                   extracted_method=extract_news_info, listen_name=listen_name)

    # scraper.method_LISTEN()
    # scraper.save_files()

    scraper = Scraper(city_info, method='post', data_type='json', is_headless=True,
                      extracted_method=extract_news_info, post_data=post_data, page_num_name=page_num_name, verify=False,)

    scraper.run()
