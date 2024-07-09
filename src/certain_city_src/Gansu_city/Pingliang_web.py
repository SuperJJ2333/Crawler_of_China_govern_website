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
    if 'data' in data:
        data_list = data['data']['searchResult']['result']
        # 遍历新闻列表
        for news_item in data_list:

            try:

                soup = BeautifulSoup(news_item, 'html.parser')

                # 提取标题
                title = soup.find('a', class_='textTitle').text

                # 提取新闻URL
                news_url = soup.find('a', class_='textTitle')['href']

                # 提取发布日期
                date = soup.find('div', class_='sourceTime').find_all('span')[1].text.replace('时间:', '')
            except Exception as e:
                logger.warning(f"部分数据不存在：{e}")
                continue

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
    URL获取方式：Session 获取post数据
    URL返回格式：json
    """

    # 爬虫基本信息
    city_info = {'name': 'Pingliang',
                 'province': 'Gansu',
                 'total_news_num': 323,
                 'each_page_num': 15,
                 'targeted_year': 2022,
                 'base_url': 'http://www.pingliang.gov.cn/api-gateway/jpaas-jsearch-web-server/interface/search/info?websiteid=&q=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pg=&cateid=faf661dbe7e94a839ac6f7a652de7af4&serviceId=7112f33f9410490396c03839bf99647f&p={page_num}&pos=title,content,filenumber&begin=2021-01-01&end=2021-12-31'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""

    """get信息"""

    city_info = PageMother(city_info=city_info, is_headless=True)

    city_info.fetch_web_by_requests(request_type='get', cleaned_method=extract_news_info)
