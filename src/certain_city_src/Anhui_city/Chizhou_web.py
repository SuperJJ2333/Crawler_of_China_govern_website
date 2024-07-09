from scraper.spider_mother import PageMother


if __name__ == '__main__':

    # 爬虫基本信息
    city_info = {'name': 'Chizhou',
                 'province': 'Anhui',
                 'total_news_num': 2318,
                 'each_page_num': 15,
                 'targeted_year': 2019,
                 'base_url': 'https://search.chizhou.gov.cn/searchData?collection=&Field=title&siteGroupId=1&keyword'
                             '=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&separate=false&sort=1&field=all&page={page_num}'
                 }
    # 可选参数
    thread_num = 5

    """xpath信息"""
    frames_xpath = 'xpath://*/div[3]/div[1]/div[1]/ul/li'
    title_xpath = 'xpath://a'
    date_xpath = ['xpath://div[2]/p[3]',
                  'xpath://li[2]/span[2]']
    content_xpath = {'frames': frames_xpath,
                     'title': title_xpath,
                     'date': date_xpath}

    city_info = PageMother(city_info=city_info, is_headless=True, thread_num=thread_num, content_xpath=content_xpath)

    city_info.fetch_web_by_requests(request_type='get_xpath')
