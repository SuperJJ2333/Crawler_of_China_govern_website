import math

from scraper.spider_mother import PageMother


if __name__ == '__main__':
    page_num = math.ceil(398 / 10)
    # page_num = math.ceil(39 / 10)
    frames_xpath = 'xpath://*[@id="search_data_list"]/ul'
    title_xpath = 'xpath://li[1]/a'
    date_xpath = ['xpath://li[2]/table/tbody/tr[3]/td[2]',
                  'xpath://li[2]/span[2]']

    name = 'Maanshan'
    url = 'https://www.mas.gov.cn/site/search/4697368?fuzzySearch=true&sort=intelligent&orderType=0&isAllSite=false&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F'
    city_info = PageMother(name, url, is_headless=False)

    city_info.fetch_web_by_click(page_num, frames_xpath, title_xpath, date_xpath)

