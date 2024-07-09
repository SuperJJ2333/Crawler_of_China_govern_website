import math

from common.form_utils import *
from scraper.spider_mother import PageMother


def get_data_from_dict(data_dict):
    data_list = []
    for data in data_dict['data']['data']:
        item = data

        # 使用get方法简化访问，如果'item'中的对应键不存在，则尝试从嵌套的字典中获取
        url = item.get('link', 'url')
        topic = item.get('title', 'name')
        date = item.get('date', 'createDate')

        if is_in_year(date, 2018):
            # 确保格式正常
            cleaned_dict = clean_news_data({'url': url, 'topic': topic, 'date': date})
            # 符合要求则加入
            data_list.append(cleaned_dict)
        else:
            continue

    return data_list


if __name__ == '__main__':
    # page_num = math.ceil(30 / 10)
    page_num = math.ceil(6345 / 10)

    name = 'Anqing'
    # &pageIndex=2
    url = 'https://www.anqing.gov.cn/site/label/8888?_=0.754174654089681&fuzzySearch=true&fromCode=title&showType=2&titleLength=35&contentLength=100&islight=true&isJson=true&pageSize=10&isForPage=true&datecode=&typeCode=all&siteId=&platformCode=&isAllSite=true&isForNum=true&sort=intelligent&orderType=0&beginDate=&endDate=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&subkeywords=&fileNum=&isInvalid=0&labelName=searchDataList'

    button_xpath = 'xpath://*[text()="下一页"]'
    # target_pack = 'front/search'

    city_info = PageMother(name, url, page_num, is_headless=True)

    city_info.fetch_web_multiple(cleaned_method=get_data_from_dict, is_by_json=True)

    "https://www.huangshan.gov.cn/site/label/8888?labelName=searchDataList&fuzzySearch=false&fromCode=&showType=2&titleLength=35&contentLength=100&islight=true&isJson=true&pageSize=10&pageIndex=2&isForPage=true&sort=desc&datecode=&typeCode=all&siteId=&columnId=&catIds=&platformCode=&isAllSite=true&isForNum=true&beginDate=2018-01-01&endDate=2018-12-31&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&subkeywords=&isAttach=1&colloquial=true&source_code=1001%2C2001%2C2003%2C201011%2C2004%2C2005&orderType=1"