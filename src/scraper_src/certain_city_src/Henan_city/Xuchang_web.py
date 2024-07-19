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
    if 'result' in data:
        data_list = data['result']['records']
        # 遍历新闻列表
        for news_item in data_list:
            # 提取所需的信息
            title = news_item.get('title', '')  # 若无标题，默认值
            if base_url:
                news_url = base_url + news_item.get('infoid', '')  # 若无 URL，默认值
            else:
                news_url = news_item.get('articleUri', '')
            publish_date = news_item.get('showdate', '')  # 若无发布日期，默认值

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
    total_news_num = 79
    each_page_num = 10
    time_limit = 2018

    # 爬虫信息
    name = 'Xuchang'
    province = 'Henan'
    url = 'http://www.xuchang.gov.cn/inteligentsearch/rest/esinteligentsearch/getFullTextDataNew'

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
    data_dict = {"token": "", "pn": '{page_num}', "rn": 10, "sdt": "2016-12-31T16:00:00.000Z", "edt": "2017-12-30T16:00:00.000Z",
                 "wd": "%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0", "inc_wd": "",
                 "exc_wd": "", "fields": "title;content", "cnum": "001;002;003;004;005;006;007;008;009;010", "sort": "",
                 "ssort": "title", "cl": 500, "terminal": "", "condition": None, "time": None,
                 "highlights": "title;content", "statistics": None, "unionCondition": None, "accuracy": "",
                 "noParticiple": "0", "searchRange": None}
    off_set = 10
    page_num_name = 'pn'
    base_url = 'http://www.xuchang.gov.cn/openDetailDynamic.html?infoid='

    city_info = PageMother(name=name, url=url, targeted_year=time_limit, total_news_num=total_news_num,
                           each_page_num=each_page_num, province=province, is_headless=True)

    city_info.fetch_web_by_requests(request_type='post', data_dict=data_dict, off_set=off_set,
                                    page_num_name=page_num_name,
                                    cleaned_method=extract_news_info,
                                    base_url=base_url)
