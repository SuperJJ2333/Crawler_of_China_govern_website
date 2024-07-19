import math

from common.content_utils import save_to_excel
from scraper.spider_mother import PageMother


if __name__ == '__main__':
    page_num = math.ceil(3947 / 10)
    # page_num = math.ceil(20 / 10)

    name = 'Huaibei'
    url = 'https://www.huaibei.gov.cn/site/label/8888?_=0.6011192822980198&labelName=searchDataList&isJson=true&isForPage=true&excSites=4697629%2C4699146%2C4697634%2C4697584%2C4697632%2C4697650%2C4698945%2C4697636&target=&pageSize=10&titleLength=35&contentLength=100&showType=2&ssqdDetailTpl=35931&islight=true&columnId=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&subkeywords=&typeCode=all&isAllSite=true&fromCode=title&fuzzySearch=true&attachmentType=&datecode=&sort=intelligent&colloquial=true&orderType=0&platformCode=&siteId='

    city_info = PageMother(name, url, is_headless=True)

    data_list = city_info.fetch_web_by_json(page_num)

    info_list = []

    for data in data_list:
        for item in data['data']['data']:
            year_part = item['createDate'].split('-')[0]

            if int(year_part) == 2018:
                info_list.append({
                    'url': item['link'],
                    'topic': item['title'],
                    'date': item['createDate'],
                    'content': item['content'],
                })

    save_to_excel(info_list, name)
