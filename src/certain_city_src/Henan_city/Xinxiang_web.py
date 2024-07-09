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
    total_news_num = 14
    each_page_num = 10
    time_limit = 2018

    # 爬虫信息
    name = 'Xinxiang'
    province = 'Henan'
    url = 'http://www.xinxiang.gov.cn/search/SolrSearch/s'

    # 监听信息
    listen_path = 'searchapi.anyang.gov.cn/open/api/'

    # xpath信息
    frames_xpath = "//div[@class='media']/div[@class='media-body']"
    title_xpath = "./h4[@class='media-heading result-title']/a"
    date_xpath = ["./div[@class='result-inner']/i[@class='grey']"]
    content_xpath = {'frames': frames_xpath,
                     'title': title_xpath,
                     'date': date_xpath}

    # requests信息
    data_dict = {
        'token4': '1ec282ee4f5544d6aca40426826bea09',
        'q': '学习考察',
        'articlePublishTimeStart': '2017-01-01',
        'articlePublishTimeEnd': '2017-12-31',
        'siteId': '641a8f75d6d44ac09a68afc6aae73c23',
        'rows': '10',
        'page': '6',
        'catalogLevel': '',
        'type': ''
    }
    page_num_name = 'page'

    city_info = PageMother(name=name, url=url, targeted_year=time_limit, total_news_num=total_news_num,
                           each_page_num=each_page_num, content_xpath=content_xpath,
                           province=province, is_headless=True)

    city_info.fetch_web_by_requests(request_type='post_xpath', data_dict=data_dict,
                                    page_num_name=page_num_name)
