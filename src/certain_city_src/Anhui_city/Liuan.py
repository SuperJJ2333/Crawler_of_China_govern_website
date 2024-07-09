import math

from scraper.spider_mother import PageMother


if __name__ == '__main__':
    page_num = math.ceil(177 / 10)
    # page_num = math.ceil(39 / 10)
    frames_xpath = 'xpath://*[@id="search_list"]/ul'
    title_xpath = 'xpath://li[1]/a'
    date_xpath = ['xpath://li[4]/span[2]',
                  'xpath://li[3]/span[2]',
                  'xpath://li[2]/table/tbody/tr[3]/td[2]/text()']

    name = 'liuan'
    url = 'https://www.luan.gov.cn/site/search/6789941?platformCode=&isAllSite=true&siteId=&columnId=&columnIds=&typeCode=&beginDate=2018-1-1&endDate=2018-12-31&fromCode=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&oldKeywords=&subkeywords=&filterKeyWords=&excColumns=&datecode=&sort=intelligent&orderType=1&fuzzySearch=true&type=&tableColumnId=&indexNum=&fileNum=&flag=false&pageSize=10&pid=&leaderTypeId=&liId=&pageIndex='

    city_info = PageMother(name, url, page_num, is_headless=True)

    city_info.fetch_web_multiple(frames_xpath=frames_xpath, title_xpath=title_xpath, date_xpath=date_xpath)
