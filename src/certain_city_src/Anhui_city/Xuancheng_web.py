import math

from scraper.spider_mother import PageMother


if __name__ == '__main__':
    page_num = math.ceil(376 / 15)
    # page_num = math.ceil(39 / 10)
    frames_xpath = 'xpath://*[@id="ui-view"]/div/ul/li'
    title_xpath = 'xpath://h1/a'
    date_xpath = ['xpath://p[2]/span[2]',
                  'xpath://li[2]/span[2]']

    name = 'Xuancheng'
    url = 'https://search.xuancheng.gov.cn/searchData?keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&fromDate=2018-01-01&endDate=2018-12-31&field=all&separate=false&sort=-1&page='

    city_info = PageMother(name, url, page_num, is_headless=True)

    city_info.fetch_web_multiple(frames_xpath=frames_xpath, title_xpath=title_xpath, date_xpath=date_xpath)
