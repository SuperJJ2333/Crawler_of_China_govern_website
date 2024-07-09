from datetime import datetime

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
    if 'match' in data:
        data_list = data['match']['hits']['hits']
        # 遍历新闻列表
        for news_item in data_list:

            try:
                news_item = news_item['_source']
                # 提取发布日期
                date = datetime.fromtimestamp(news_item['releasetime'] / 1000).strftime('%Y-%m-%d')
                # 提取新闻标题
                title = news_item['msg_title']
                # 提取新闻URL
                news_url = news_item['htmlpath']

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
    city_info = {'name': 'Wuhai',
                 'province': 'Neimenggu',
                 'total_news_num': 797,
                 'each_page_num': 10,
                 'targeted_year': 2021,
                 'base_url': 'http://www.wuhai.gov.cn/search/pcRender?pageId=63493493b61047b8be9bc396fa236e60'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    # 将JSON字符串转换成字典
    data_dict = {'originalSearchUrl': '/search/pcRender?pageId=63493493b61047b8be9bc396fa236e60',
                 'app': 'e0f5bd4c17f64784a4e8ea47a25bbb27,2d2145bfde734f20b3a746f5040a2752,b46547d5770e4c1794e9a337836ba34d,ab217b6d91d64085bd05924b218abbc8,4536d378b2a843d79ad0cbb2d5433ce1,fcff548c7a114dd3b3970d3866191820,57cddb86829c4d1e83ceed3c85dc4942',
                 'sr': 'score desc', 'ext': 'siteId:1862', 'pNo': '2', 'q': '考察学习'}

    page_num_name = "pNo"
    # off_set = 10
    base_url = 'https://www.wuxi.gov.cn/search/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'
    headers = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Cache-Control": "max-age=0",
  "Content-Type": "application/x-www-form-urlencoded",
  "Cookie": "AMJ-VISIT=\"4FF135B5E8E648DCAAB751FD5D9CDCAA,390CAA50D9D181EAB1C42A424195C9AF,1715929360000\"; JSESSIONID=390CAA50D9D181EAB1C42A424195C9AF; _gscu_1831468369=15928690u0bnpg14; _gscbrs_1831468369=1; _gscs_1831468369=159286903727ig14|pv:6",
  "Host": "www.wuhai.gov.cn",
  "Origin": "http://www.wuhai.gov.cn",
  "Referer": "http://www.wuhai.gov.cn/search/pcRender?pageId=63493493b61047b8be9bc396fa236e60",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}

    """get信息"""

    """xpath信息"""
    frames_xpath = 'x://*[@id="panel-page"]/div/div[2]/div[2]/div/div'
    title_xpath = 'x://h3/a'
    date_xpath = ['x://div/p[2]/span']
    content_xpath = {'frames': frames_xpath,
                     'title': title_xpath,
                     'date': date_xpath}

    city_info = PageMother(city_info=city_info, is_headless=True, content_xpath=content_xpath,
                           thread_num=thread_num)

    city_info.fetch_web_by_requests(request_type='post_xpath', data_dict=data_dict, page_num_name=page_num_name,
                                    headers=headers, data_type='data',
                                    is_versify=False)
