import math

from scraper.spider_mother import PageMother


if __name__ == '__main__':
    page_num = math.ceil(1000 / 20)
    # page_num = math.ceil(39 / 10)
    frames_xpath = 'xpath://*[@class="u-conlist"]'
    title_xpath = 'xpath://h3/a'
    date_xpath = ['xpath://span[3]',
                  'xpath://li[2]/span[2]']

    name = 'Fuyan'
    url = 'https://www.fy.gov.cn/index.php?c=search&site_id=&type=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&field=&sort=&forceSearch=&wrongSearch=&from_date=2018-01-01&to_date=2018-12-31&page='
    city_info = PageMother(name, url, page_num, is_headless=True)

    city_info.fetch_web_multiple(frames_xpath=frames_xpath, title_xpath=title_xpath, date_xpath=date_xpath)

    'https://www.ahsz.gov.cn/site/search/11708048?orderType=1&colloquial=true&platformCode=&isAllSite=true&siteId=&columnId=&columnIds=&typeCode=all&beginDate=&endDate=&fromCode=title&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&oldKeywords=&subkeywords=&excColumns=&datecode=&sort=desc&type=&tableColumnId=&indexNum=&fuzzySearch=false&fileNum=&flag=false&pageIndex=2&pageSize=10'
