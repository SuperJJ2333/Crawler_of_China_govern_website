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
    if 'obj' in data:
        data_list = data['obj']['datas']
        # 遍历新闻列表
        for news_item in data_list:

            try:
                # 提取发布日期
                date = news_item['createDate']
                # 提取新闻标题
                title = news_item['title']
                # 提取新闻URL
                news_url = news_item['url']

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
    city_info = {'name': 'Baliaonier',
                 'province': 'Neimenggu',
                 'total_news_num': 1041,
                 'each_page_num': 10,
                 'targeted_year': 2021,
                 'base_url': 'https://www.bynr.gov.cn/webServices/search/5030?content=%E5%AD%A6%E4%B9%A0%E8%80%83%E5'
                             '%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&startDate=&endDate=2024-05-17%2015:20:57'
                             '&pager.offset={page_num}&channelid=&searchField=&sortFields=&orders='

                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    # 将JSON字符串转换成字典
    # data_dict = {'originalSearchUrl': '/search/pcRender?pageId=63493493b61047b8be9bc396fa236e60',
    #              'app': 'e0f5bd4c17f64784a4e8ea47a25bbb27,2d2145bfde734f20b3a746f5040a2752,b46547d5770e4c1794e9a337836ba34d,ab217b6d91d64085bd05924b218abbc8,4536d378b2a843d79ad0cbb2d5433ce1,fcff548c7a114dd3b3970d3866191820,57cddb86829c4d1e83ceed3c85dc4942',
    #              'sr': 'score desc', 'ext': 'siteId:1862', 'pNo': '2', 'q': '考察学习'}

    # page_num_name = "pNo"
    off_set = 10
    # base_url = 'https://www.wuxi.gov.cn/search/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "wzws_sessionid=gWVmNmMxOKBmRwB5gDIyMS40LjMyLjI0gjM1NDk1OQ==; AGILE_SID=66C9CDEECB49F6FEDD6C4804617AB829; USER_TOKEN=76f3b5f306c0484d978aaedf43105cec; AGILE_SID_SHIRO=3b126fac-74c7-4972-966a-0cf1e1f04688; _gscu_388273600=15929441oksuo116; _gscbrs_388273600=1; arialoadData=false; _gscs_388273600=159294416pcun316|pv:3",
        "Host": "www.bynr.gov.cn",
        "Referer": "https://www.bynr.gov.cn/web/search/5030?searchField=title&content=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0",
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
    frames_xpath = 'x://*[@id="panel-page"]/div/div[2]/div[2]/div/div'
    title_xpath = 'x://h3/a'
    date_xpath = ['x://div/p[2]/span']
    content_xpath = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "wzws_sessionid=gWVmNmMxOKBmRwB5gDIyMS40LjMyLjI0gjM1NDk1OQ==; AGILE_SID=66C9CDEECB49F6FEDD6C4804617AB829; USER_TOKEN=76f3b5f306c0484d978aaedf43105cec; AGILE_SID_SHIRO=3b126fac-74c7-4972-966a-0cf1e1f04688; _gscu_388273600=15929441oksuo116; _gscbrs_388273600=1; arialoadData=false; _gscs_388273600=159294416pcun316|pv:3",
        "Host": "www.bynr.gov.cn",
        "Referer": "https://www.bynr.gov.cn/web/search/5030?searchField=title&content=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }

    city_info = PageMother(city_info=city_info, is_headless=True,
                           thread_num=thread_num)

    city_info.fetch_web_by_requests(request_type='get',  off_set=off_set,
                                    headers=headers, is_begin_from_zero=True, cleaned_method=extract_news_info)