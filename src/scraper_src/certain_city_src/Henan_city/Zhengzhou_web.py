from scraper.spider_mother import PageMother



if __name__ == '__main__':
    total_news_num = 6539
    each_page_num = 10
    frames_xpath = 'xpath://*[@id="full_text_search_form"]/div[2]/div/div[3]/div[2]'
    title_xpath = 'xpath://a'
    date_xpath = ['xpath://em[1]']
    time_limit = 2019

    name = 'Zhengzhou'
    url = 'https://www.zhengzhou.gov.cn/search_{page_num}.jspx?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&result_type=2&source=&place=&cid=&mid=&orderby=0'

    city_info = PageMother(name=name, url=url, targeted_year=time_limit, total_news_num=total_news_num,
                           each_page_num=each_page_num, is_headless=True)

    city_info.fetch_web_multiple(frames_xpath=frames_xpath, title_xpath=title_xpath, date_xpath=date_xpath)
