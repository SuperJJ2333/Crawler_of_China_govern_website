from bs4 import BeautifulSoup

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
            # 创建 BeautifulSoup 对象来解析 HTML
            soup = BeautifulSoup(news_item, 'html.parser')

            # 寻找新闻标题和 URL
            title_tag = soup.find('a', target="_blank")
            title = title_tag.get_text(strip=True)

            news_url = title_tag['href']

            # 寻找发布日期
            date = soup.find('span', class_='jcse-news-date').get_text(strip=True)

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
        logger.info(f"第{page_num}页 - 符合年份为{year}的新闻有 {len(news_list)}/{len(data_list)} 条")
    else:
        # pass
        logger.warning(f"第{page_num}页 - Json格式设置得有问题，请重新设置")

    # 返回结果列表
    return news_list


if __name__ == '__main__':
    """
    URL获取方式：api post访问
    URL返回格式：HTMl字典
    """

    # 爬虫基本信息
    city_info = {'name': 'Weihai',
                 'province': 'Shandong_city',
                 'total_news_num': 267,
                 'each_page_num': 20,
                 'targeted_year': 2018,
                 'base_url': 'https://www.weihai.gov.cn/jsearchfront/interfaces/cateSearch.do'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    data_dict = {'websiteid': '371000000000000', 'q': '学习考察 考察学习', 'p': '2', 'pg': '20',
                 'cateid': '386', 'tpl': '1321', 'begin': '20170101', 'end': '20171231',
                 'checkError': '1', 'word': '学习考察 考察学习', 'timetype': '5'}
    page_num_name = 'p'
    # off_set = 5
    base_url = 'http://www.weihai.gov.cn/jsearchfront/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'

    city_info = PageMother(city_info=city_info, is_headless=True)

    # city_info.fetch_web_multiple()

    city_info.fetch_web_by_requests(request_type='post_session', data_dict=data_dict,
                                    page_num_name=page_num_name,
                                    cleaned_method=extract_news_info, base_url=base_url)
