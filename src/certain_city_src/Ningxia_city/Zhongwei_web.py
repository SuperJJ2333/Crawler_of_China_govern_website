import json

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
        data_list = data['data']['middle']['list']
        # 遍历新闻列表
        for news_item in data_list:

            try:

                # 提取信息
                title = news_item['title']  # 提取标题
                news_url = news_item['url']  # 提取新闻URL
                date = news_item['time']  # 提取发布日期

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
    city_info = {'name': 'Zhongwei',
                 'province': 'Ningxia',
                 'total_news_num': 21,
                 'each_page_num': 10,
                 'targeted_year': 2019,
                 'base_url': 'https://www.nxzw.gov.cn/irs/front/search'
                 }
    # 可选参数
    thread_num = 5

    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888"
    }

    """post信息"""
    # 将JSON字符串转换成字典
    data_dict = '{"tenantIds":"167","tenantId":"167","searchWord":"学习考察 考察学习","dataTypeId":4,"historySearchWords":[],"orderBy":"related","searchBy":"all","pageNo":2,"pageSize":10,"endDateTime":1546271999000,"beginDateTime":1514736000000,"filters":[],"configTenantId":"19","customFilter":{"operator":"and","properties":[],"filters":[]},"sign":"d5752637-83bd-4026-cbb5-045f71bb72b1"}'
    data_dict = json.loads(data_dict)
    page_num_name = "pageNo"
    # off_set = 10
    base_url = 'http://www.yingtan.gov.cn/jsearchfront/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'
    headers = {
  "POST /irs/front/search HTTP/1.1": "",
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Content-Type": "application/json",
  "Cookie": "SESSION=MmU2YmFjMzYtYzY4OS00OWIxLThjZGYtZTYzZjZmMWI4MTQ4; TS01dbc741=0138b8b1602162d164559d4c8d113065174324ff94eb37b41f7355ae698bedb4137fd79c3bc044985d972acc71936f73eedbfa8cf1; _trs_uv=lwfvng0u_1697_2qmz; _trs_ua_s_1=lwfvng0u_1697_1y1z; TS01d5e988=0138b8b1602162d164559d4c8d113065174324ff94eb37b41f7355ae698bedb4137fd79c3bc044985d972acc71936f73eedbfa8cf1",
  "Host": "www.nxzw.gov.cn",
  "Origin": "https://www.nxzw.gov.cn",
  "Referer": "https://www.nxzw.gov.cn/nxsearch/search.html?code=17ccab70a79&tenantId=167&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
  "sec-ch-ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\""
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
                           thread_num=thread_num, proxies=proxies)

    city_info.fetch_web_by_requests(request_type='post_session', data_dict=data_dict, page_num_name=page_num_name,
                                    headers=headers, data_type='json', cleaned_method=extract_news_info,
                                    is_versify=False,)
