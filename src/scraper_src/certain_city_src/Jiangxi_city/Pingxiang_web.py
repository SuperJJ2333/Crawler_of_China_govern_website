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

            try:

                # 解析HTML内容
                doc = html.fromstring(news_item)

                # 使用XPath提取信息
                title = doc.xpath('//div[contains(@class, "jcse-news-title")]/a/text()')[0].strip()
                news_url = doc.xpath('//div[contains(@class, "jcse-news-url")]/a/@href')[0]
                date = doc.xpath('//span[contains(@class, "jcse-news-date")]/text()')[0]

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
    city_info = {'name': 'Pingxiang',
                 'province': 'Jiangxi',
                 'total_news_num': 2275,
                 'each_page_num': 5,
                 'targeted_year': 2021,
                 'base_url': 'https://www.pingxiang.gov.cn/jsearchfront/interfaces/cateSearch.do'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    # 将JSON字符串转换成字典
    data_dict = {'websiteid': '360300000000000', 'q': '学习考察', 'p': '2', 'pg': '5',
                 'cateid': '118', 'begin': '0', 'end': '0', 'tpl': '8'}

    page_num_name = "p"
    # off_set = 10
    base_url = 'https://www.pingxiang.gov.cn/jsearchfront/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'
    headers = {
        "Host": "www.pingxiang.gov.cn",
        "sec-ch-ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Origin": "https://www.pingxiang.gov.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.pingxiang.gov.cn/jsearchfront/search.do?websiteid=360300000000000&searchid=126&pg=&p=1&tpl=8&serviceType=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&pq=&oq=&eq=&pos=&begin=20200101&end=20201231",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "JSESSIONID=5B6B19B3D68BE73BF3DF7BDC5CEB04E6; user_sid=eaadb97a2e9a4d50867ac6ca2fd9692f; user_cid=81785146f9034c5eb06ed8e48878112a; searchsign=b86ef2fbe1134e9688d7c1f61774b386; FW9uCWqlVzC22m1KfCMCjfvFHpRMsgt=14faf0a8-26d1-42de-ae13-b151b136719d; dGg2aCfMMK97Ro270mqBFu5qjC8TQbL2opnHvbEpM=Tifz8hd5p4O3AB%2BivrbJpIrUmQqXoggwP2UtfkDHghk%3D; dGg2aCfMMK97Ro270mqBFu5qjC8TQbL2opnHvbEpM=Tifz8hd5p4O3AB%2BivrbJpIrUmQqXoggwP2UtfkDHghk%3D; FW9uCWqlVzC22m1KfCMCjfvFHpRMsgt=14faf0a8-26d1-42de-ae13-b151b136719d"
    }

    """get信息"""

    """xpath信息"""
    frames_xpath = 'x://*[@id="panel-page"]/div/div[2]/div[2]/div/div'
    title_xpath = 'x://h3/a'
    date_xpath = ['x://div/p[2]/span']
    content_xpath = {'frames': frames_xpath,
                     'title': title_xpath,
                     'date': date_xpath}

    city_info = PageMother(city_info=city_info, is_headless=True,
                           thread_num=thread_num)

    city_info.fetch_web_by_requests(request_type='post_session', data_dict=data_dict, page_num_name=page_num_name,
                                    headers=headers, data_type='data', cleaned_method=extract_news_info,
                                    base_url=base_url)
