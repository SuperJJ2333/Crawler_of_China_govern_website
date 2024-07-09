from lxml import html

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

    """xpath信息"""
    frames_xpath = '//*[@id="results"]/div'
    title_xpath = './/a'
    date_xpath = ['.//div/div/div/div[1]/font']

    # 将 JSON 字符串解析为 Python 字典
    data = json_data

    # 初始化一个列表来存储新闻信息
    news_list = []

    # 假设 data 是你的 HTML 数据，这里用 json_data 表示可能是一个JSON字符串
    tree = html.fromstring(data)

    # 使用 XPath
    frames = tree.xpath(frames_xpath)

    for frame in frames:
        a_tag = frame.xpath(title_xpath)[0] if frame.xpath(title_xpath) else None
        if a_tag is not None:
            title = a_tag.text_content().strip()
            news_url = a_tag.get('href')
        else:
            continue  # 如果没有找到标题，则继续下一个 frame

        date = None
        for date_path in date_xpath:
            date_element = frame.xpath(date_path)
            if date_element:
                date = date_element[0].text_content().strip()
                break

        # 将提取的数据添加到列表中
        news_dict = {'topic': title,
                     'url': news_url if news_url.startswith(('http://', 'https://')) else base_url + news_url,
                     'date': date,
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
    logger.info(f"第{page_num}页 - 符合年份为{year}的新闻有 {len(news_list)}/{len(frames)} 条")

    # 返回结果列表
    return news_list


if __name__ == '__main__':
    """
    URL获取方式：Drissionpage 通过xpath获取
    """

    # 爬虫基本信息
    city_info = {'name': 'Panzihua',
                 'province': 'Sichuan_city',
                 'total_news_num': 26429,
                 'each_page_num': 20,
                 'targeted_year': 2019,
                 'base_url': 'http://bot.panzhihua.gov.cn/search/index.html?keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&isLocalWebSite=false&sortType=timeSort&siteId=14'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    data_dict = {'searchType': 'fullSearch', 'keyword': '学习考察 考察学习', 'isLocalWebSite': 'false',
                 'siteId': '14', 'channel': 'all', 'timeCondition': 'setTime',
                 'dateRange': '2018-01-01T00:00:00Z|2018-12-31T23:59:59Z',
                 'sortType': 'timeSort', 'page': '4'}

    page_num_name = "page"
    # off_set = 5
    # base_url = 'http://www.zg.gov.cn/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'

    """初始化爬虫"""
    city_info = PageMother(city_info=city_info, is_headless=True)

    # city_info.fetch_web_multiple(is_begin_from_zero=True)

    city_info.fetch_web_by_requests(request_type='post_session', cleaned_method=extract_news_info,
                                    data_dict=data_dict, page_num_name=page_num_name,
                                    data_type='data')
