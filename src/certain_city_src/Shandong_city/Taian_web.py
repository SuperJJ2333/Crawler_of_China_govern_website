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
    # 将 JSON 字符串解析为 Python 字典
    data = json_data

    # 初始化一个列表来存储新闻信息
    news_list = []

    # 检查 JSON 数据结构中是否存在所需的路径和数据
    if 'result' in data:
        data_list = data['result']
        # 遍历新闻列表
        for news_item in data_list:
            # 解析 HTML 内容
            parsed_html = html.fromstring(news_item)

            # 提取标题
            title = parsed_html.xpath('//div[@class="jcse-news-title"]/a/text()')[0]

            # 提取 URL
            url = parsed_html.xpath('//div[@class="jcse-news-title"]/a/@href')[0]

            # 提取日期
            date = parsed_html.xpath('//div[@class="jcse-news-other-info"]/span[@class="jcse-news-date"]/text()')[0]

            # 将提取的数据添加到列表中
            news_dict = {'topic': title,
                         'url': base_url + url,
                         'date': date
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
        pass
        # logger.warning(f"第{page_num}页 - Json格式设置得有问题，请重新设置")

    # 返回结果列表
    return news_list


if __name__ == '__main__':
    """
    需要IP代理，暂时搁置
    
    URL获取方式：api post访问
    URL返回格式：HTML
    """

    # 新闻目录参数
    total_news_num = 7728
    each_page_num = 6
    time_limit = 2021

    # 爬虫信息
    name = 'Taian'
    province = 'Shandong_city'
    url = 'http://www.heze.gov.cn/els-service/search/new/2/10'
    thread_num = 1

    """post信息"""
    data_dict = {"dq": "0530", "fwzt": 3, "highlight": "1", "isSearch": "1",
                 "type": [1, 2, 3], "tab": "qb",
                 "starttime": "2019-01-01", "endtime": "2019-12-31", "txtmemo": "考察学习"}
    off_set = 1
    page_num_name = 'p'
    base_url = 'http://www.taian.gov.cn/jsearchfront/'

    city_info = PageMother(name=name, url=url, targeted_year=time_limit, total_news_num=total_news_num,
                           each_page_num=each_page_num, province=province, is_headless=True, thread_num=thread_num)

    # city_info.fetch_web_multiple()

    city_info.fetch_web_by_requests(request_type='post_session', data_dict=data_dict,
                                    page_num_name=page_num_name,
                                    cleaned_method=extract_news_info)
