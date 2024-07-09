import math

from scraper.spider_mother import PageMother


if __name__ == '__main__':
    page_num = math.ceil(472 / 10)
    frames_xpath = 'xpath://*[@id="search_list"]/ul'
    title_xpath = 'xpath://li[1]/a'
    date_xpath = ['xpath://li[3]/span[2]',
                  'xpath://li[2]/span[3]',
                  'xpath://li[2]/span[2]']

    name = 'Huainan'
    url = 'https://www.huainan.gov.cn/site/search/4964522?platformCode=&fuzzySearch=true&orderType=0&isAllSite=true&siteId=&columnId=&columnIds=&typeCode=all&beginDate=2018-1-1&endDate=2018-12-31&fromCode=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&oldKeywords=&subkeywords=&excColumns=&datecode=&sort=desc&type=&tableColumnId=&indexNum=&catIds=&fileNum=&flag=false&colloquial=&pageSize=10'
    city_info = PageMother(name, url, is_headless=True)

    # city_info.get_web(page_num, frames_xpath, title_xpath, date_xpath)
    city_info.fetch_web_multiple(page_num, frames_xpath, title_xpath, date_xpath)

