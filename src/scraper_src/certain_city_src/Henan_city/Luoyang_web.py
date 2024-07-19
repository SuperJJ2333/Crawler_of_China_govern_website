from common.form_utils import clean_news_data, is_in_year
from scraper.spider_mother import PageMother


def extract_news_info(json_data, year, page_num, logger):
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
            url = news_item.get('selfUrl', '')  # 若无 URL，默认值
            publish_date = news_item.get('pubDate', '')  # 若无发布日期，默认值

            news_dict = {
                'topic': title,
                'url': url,
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
    total_news_num = 15950
    each_page_num = 15
    time_limit = 2019

    name = 'Luoyang'
    province = 'Henan'
    url = 'https://t.ly.gov.cn/search-api/open/api/external?keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83' \
          '%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=4103000021&allKeyword=&anyKeyword=&noKeyword=&searchRange=-1000' \
          '&sortType=150&beginTime=&endTime=&pageNumber={page_num}&pageSize=15&fileType=0&docType=0'

    city_info = PageMother(name=name, url=url, targeted_year=time_limit, total_news_num=total_news_num,
                           each_page_num=each_page_num, province=province, is_headless=True)

    city_info.fetch_web_by_requests(cleaned_method=extract_news_info)
