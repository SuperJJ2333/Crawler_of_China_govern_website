from common.form_utils import clean_news_data, is_in_year
from scraper.spider_mother import PageMother


def extract_news_info(json_data, year, logger):
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
    if 'searchResultAll' in data and 'searchTotal' in data['searchResultAll']:
        # 遍历新闻列表
        for news_item in data['searchResultAll']['searchTotal']:
            # 提取所需的信息
            title = news_item.get('title', '')  # 若无标题，默认值
            url = news_item.get('url', '')  # 若无 URL，默认值
            publish_date = news_item.get('pubDate', '')  # 若无发布日期，默认值

            news_dict = {
                'topic': title,
                'url': url,
                'date': publish_date
            }
            # 清理URL字符串
            cleaned_dict = clean_news_data(news_dict)

            if is_in_year(cleaned_dict['date'], year):
                # 将提取的信息存储在字典中，并添加到列表
                news_list.append(cleaned_dict)
                logger.info(
                    f"{cleaned_dict['topic']} 日期为：{cleaned_dict['date']} 年份属于 {year}")
            else:
                pass
                logger.warning(f"{cleaned_dict['topic']} 日期为：{cleaned_dict['date']} 不属于 {year}")

    # 返回结果列表
    return news_list


if __name__ == '__main__':
    total_news_num = 27
    each_page_num = 10
    frames_xpath = 'xpath://*[@id="full_text_search_form"]/div[2]/div/div[3]/div[2]'
    title_xpath = 'xpath://a'
    date_xpath = ['xpath://em[1]']
    listen_name = 'search5/search/s'
    time_limit = 2019

    name = 'Kaifeng'
    province = 'Henan'
    url = 'https://www.kaifeng.gov.cn/search5/search/s'
    data_dict = {
        'searchWord': '%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F',
        'siteCode': '4102000008',
        'column': '%E5%85%A8%E9%83%A8',
        'pageSize': '10',
        'pageNum': '{page_num}',
        'sonSiteCode': '',
        'checkHandle': '1',
        'searchSource': '0',
        'areaSearchFlag': '0',
        'secondSearchWords': '',
        'topical': '',
        'docName': '',
        'label': '',
        'countKey': '0',
        'uc': '0',
        'left_right_index=': '0',
        'searchBoxSettingsIndex': '',
        'orderBy': '0',
        'startTime': '',
        'endTime': '',
        'timeStamp': '0',
        'strFileType': '',
        'wordPlace': '1'
    }
    page_num_name = 'pageNum'

    city_info = PageMother(name=name, url=url, targeted_year=time_limit, total_news_num=total_news_num,
                           each_page_num=each_page_num, province=province, is_headless=True)

    city_info.get_web_by_post(data_dict=data_dict, page_num_name=page_num_name, cleaned_method=extract_news_info)
