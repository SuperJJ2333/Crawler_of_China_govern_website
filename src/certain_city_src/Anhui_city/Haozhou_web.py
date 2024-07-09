import math

from scraper.spider_mother import PageMother


if __name__ == '__main__':
    page_num = math.ceil(29 / 14)
    # page_num = math.ceil(39 / 10)
    frames_xpath = 'xpath://*[@class="f-mb15 f-md-mb10"]'
    title_xpath = 'xpath://a'
    date_xpath = ['xpath://div[2]/p[2]',
                  'xpath://li[2]/span[2]']

    name = 'Haozhou'
    url = 'https://search.bozhou.gov.cn/searchData?keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&siteId=1&field=all&fromDate=2018-01-01&endDate=2018-12-31&separate=false&sort=-1&page='

    city_info = PageMother(name, url, page_num, is_headless=True)

    city_info.fetch_web_multiple(frames_xpath=frames_xpath, title_xpath=title_xpath, date_xpath=date_xpath)
