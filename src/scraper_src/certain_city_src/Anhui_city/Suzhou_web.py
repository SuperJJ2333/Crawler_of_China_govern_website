import math

from scraper.spider_mother import PageMother


if __name__ == '__main__':
    page_num = math.ceil(177 / 10)
    # page_num = math.ceil(39 / 10)
    frames_xpath = 'xpath://*[@id="search_list"]/ul'
    title_xpath = 'xpath://li[1]/a'
    date_xpath = ['xpath://li[3]/span[2]',
                  'xpath://li[2]/span[3]',
                  'xpath://li[2]/span[2]']

    name = 'Suzhou'
    url = 'https://www.ahsz.gov.cn/site/search/11708048?orderType=&colloquial=true&platformCode=&isAllSite=true&siteId=&columnId=&columnIds=&typeCode=all&beginDate=2018-1-1&endDate=2018-12-31&fromCode=title&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&oldKeywords=&subkeywords=&excColumns=&datecode=&sort=&type=&tableColumnId=&indexNum=&fuzzySearch=true&fileNum=&flag=false&pageSize=10&pageIndex='
    city_info = PageMother(name, url, page_num, is_headless=True)

    city_info.fetch_web_multiple(frames_xpath=frames_xpath, title_xpath=title_xpath, date_xpath=date_xpath)
