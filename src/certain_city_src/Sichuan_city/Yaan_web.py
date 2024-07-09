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
    URL获取方式：Drissionpage 通过xpath获取
    """

    # 爬虫基本信息
    city_info = {'name': 'Yaan',
                 'province': 'Sichuan_city',
                 'total_news_num': 10000,
                 'each_page_num': 100,
                 'targeted_year': 2019,
                 'base_url': 'https://www.yaan.gov.cn/search.html?q=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&content=1'
                             '&pageSize=100&st=2018-01-01&et=2018-12-31&ot=timedesc&content=1&page={page_num}'
                 }
    # 可选参数
    thread_num = 5

    """xpath信息"""
    frames_xpath = 'x:/html/body/div[1]/div[2]/div[2]/ul/li'
    title_xpath = 'x://h1/a'
    date_xpath = ['x://h2/span[2]']
    content_xpath = {'frames': frames_xpath,
                     'title': title_xpath,
                     'date': date_xpath}

    city_info = PageMother(city_info=city_info, is_headless=True, thread_num=thread_num, content_xpath=content_xpath)

    city_info.fetch_web_by_requests(request_type='get_xpath')
