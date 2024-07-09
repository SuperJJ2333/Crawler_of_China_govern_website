from common.form_utils import clean_news_data, is_in_year
from scraper.spider_mother import PageMother


def extract_news_info(json_data, year, page_num, logger, base_url=None):
    """
    从 JSON 数据中提取新闻标题、URL 和发布日期。

    参数:
    - json_data: 包含新闻信息的 JSON 字符串

    返回:
    - news_list: 包含每条新闻的标题、URL 和发布日期的字典列表
    """
    # 将 JSON 字符串解析为 Python 字典
    data = json_data

    # 初始化一个列表来存储新闻信息
    news_list = []

    # 检查 JSON 数据结构中是否存在所需的路径和数据
    if 'data' in data:
        data_list = data['data']['datas']
        # 遍历新闻列表
        for news_item in data_list:
            # 提取所需的信息
            title = news_item.get('title', '')  # 若无标题，默认值
            if base_url:
                news_url = base_url + news_item.get('selfUrl', '')  # 若无 URL，默认值
            else:
                news_url = news_item.get('selfUrl', '')
            publish_date = news_item.get('pubDate', '')  # 若无发布日期，默认值

            news_dict = {
                'topic': title,
                'url': news_url,
                'date': publish_date
            }
            # 清理URL字符串
            cleaned_dict = clean_news_data(news_dict)

            # 检查是否符合年份的要求
            if is_in_year(cleaned_dict['date'], year):
                # 将提取的信息存储在字典中，并添加到列表
                news_list.append(cleaned_dict)
                # logger.info(f"{cleaned_dict['topic']} 日期为：{cleaned_dict['date']} 年份属于 {year}")
            else:
                pass
                # logger.warning(f"{cleaned_dict['topic']} 日期为：{cleaned_dict['date']} 不属于 {year}")
        logger.info(f"第{page_num}页 - 符合年份为{year}的新闻有 {len(news_list)}/{len(data_list)} 条")
    else:
        logger.warning("Json格式设置得有问题，请重新设置")

    # 返回结果列表
    return news_list


if __name__ == '__main__':
    # 新闻目录参数
    total_news_num = 57
    each_page_num = 15
    time_limit = 2018

    # 爬虫信息
    name = 'Nanyang'
    province = 'Henan'
    url = 'https://t.nanyang.gov.cn/search-api/open/api/external?keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80' \
          '%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=4113000002&allKeyword=&anyKeyword=&noKeyword=&searchRange=-1000' \
          '&sortType=150&beginTime=2017-01-01&endTime=2017-12-31&pageNumber={page_num}&pageSize=15&fileType=0&docType=0'

    # 监听信息
    listen_path = 'search-api/open/api/'

    # xpath信息
    frames_xpath = 'x://*[@id="searchForm"]/div[2]/div[2]/div[1]/div[2]/div'
    title_xpath = 'x://p[1]/a'
    date_xpath = ['x://p[3]/span']
    content_xpath = {'frames': frames_xpath,
                     'title': title_xpath,
                     'date': date_xpath}

    # requests信息
    data_dict = {'q': '考察学习', 'forCatalogType': '0',
                 'token4': '6058461769fc4094a95e8bd4bfbf9485',
                 'siteId': 'efc127c860d248459e9b75bc458977d7',
                 'offset': '{page_num}', 'limit': '10'}
    off_set = 10
    page_num_name = 'offset'
    base_url = 'http://www.luohe.gov.cn'

    city_info = PageMother(name=name, url=url, targeted_year=time_limit, total_news_num=total_news_num,
                           each_page_num=each_page_num, province=province,
                           content_xpath=content_xpath, is_headless=True)

    city_info.fetch_web_multiple(is_by_listen=True, listen_target=listen_path, cleaned_method=extract_news_info)

    # city_info.get_web_by_requests(request_type='post', data_dict=data_dict, off_set=off_set,
    #                               page_num_name=page_num_name,
    #                               cleaned_method=extract_news_info,
    #                               base_url=base_url)
