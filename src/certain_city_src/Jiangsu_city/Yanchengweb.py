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

            try:
                soup = BeautifulSoup(news_item, 'html.parser')

                # 提取标题
                title = soup.find('div', class_='jcse-news-title').a.text

                # 提取发布日期
                date = soup.find('span', class_='jcse-news-date').text

                # 提取URL
                news_url = soup.find('div', class_='jcse-news-url').a['href']

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
    city_info = {'name': 'Yancheng',
                 'province': 'Jiangsu',
                 'total_news_num': 1267,
                 'each_page_num': 10,
                 'targeted_year': 2019,
                 'base_url': 'https://www.yancheng.gov.cn/jsearchfront/interfaces/cateSearch.do'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""

    # 将JSON字符串转换成字典
    data_dict = {'websiteid': '320901000000000', 'q': '学习考察 考察学习', 'p': '2', 'pg': '10',
                 'cateid': '310', 'pos': 'title,content,filenumber,keyword,_default_search',
                 'checkError': '0', 'tpl': '63', 'sortType': '1'}

    page_num_name = "p"
    # off_set = 10
    base_url = 'https://www.yancheng.gov.cn/jsearchfront/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "JSESSIONID=7AF057EF8EC999860DCA1EE39B51A0D3; user_sid=0c3b54e05a5946ad83dcf7dfbaf674b4; user_cid=b3c46972da1b40688568cf8394d4df4e; _city=%E5%B9%BF%E5%B7%9E%E5%B8%82; hq=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F; __jsluid_s=e62b0a8010b87fc5e4e8a80f47f7ba49",
        "Host": "www.yancheng.gov.cn",
        "Origin": "https://www.yancheng.gov.cn",
        "Referer": "https://www.yancheng.gov.cn/jsearchfront/search.do?websiteid=320901000000000&searchid=308&pg=&p=1&tpl=63&temporaryQ=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&standard=&checkError=0&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pq=&oq=&eq=&pos=title%2Ccontent%2Cfilenumber%2Ckeyword%2C_default_search&sortType=&begin=&end=",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }

    """get信息"""

    """xpath信息"""
    frames_xpath = 'x://*[@id="results"]/div'
    title_xpath = 'x://a'
    date_xpath = ['x://div/div[1]/font', 'x://div/div/div[2]/div[1]/font']
    content_xpath = {'frames': frames_xpath,
                     'title': title_xpath,
                     'date': date_xpath}

    city_info = PageMother(city_info=city_info, is_headless=True,
                           thread_num=thread_num)

    city_info.fetch_web_by_requests(request_type='post_session', data_dict=data_dict, page_num_name=page_num_name,
                                    headers=headers, data_type='data', cleaned_method=extract_news_info,
                                    base_url=base_url)
