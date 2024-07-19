import time

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
    if 'datas' in data:
        data_list = data['datas']
        # 遍历新闻列表
        for news_item in data_list:

            try:

                # 提取信息
                title = news_item['_doctitle']  # 提取标题
                news_url = news_item['chnldocurl']  # 提取新闻URL
                date = news_item['docreltime']  # 提取发布日期

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
    city_info = {'name': 'Fuzhou',
                 'province': 'Fujian',
                 'total_news_num': 151,
                 'each_page_num': 10,
                 'targeted_year': 2018,
                 'base_url': f'https://www.fuzhou.gov.cn/ssp/search/api/search?time={int(time.time() * 1000)}'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    # 将JSON字符串转换成字典
    data_dict = {'siteType': '1', 'mainSiteId': '402849946077df37016077eea95e002f',
                 'siteId': '402849946077df37016077eea95e002f', 'type': '0', 'page': '2',
                 'rows': '10', 'historyId': '48908a988f88afa2018f99659ecf48f7',
                 'sourceType': 'SSP_ZHSS', 'isChange': '0', 'fullKey': 'N',
                 'wbServiceType': '13', 'startDate': '2017-01-01', 'endDate': '2017-12-31',
                 'sortFiled': 'RELEVANCE', 'zhPubOrg': '1', 'keyWord': '学习考察 考察学习'}

    page_num_name = "page"
    # off_set = 10
    base_url = 'http://www.yingtan.gov.cn/jsearchfront/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'
    headers = {
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "Cookie": "Secure; _trs_uv=lv55rgqq_6103_2fcm; __jsluid_s=789de16e2b3e46ec7e7db71481da10cc; _trs_ua_s_1=lwfw4ecm_6103_7x4b; Hm_lvt_4=1716265429; Hm_lpvt_4=1716265429; Hm_lvt_f1010fcb400a1b17bc43a071742486bb=1716265429; Hm_lpvt_f1010fcb400a1b17bc43a071742486bb=1716265429; Secure",
  "Host": "www.fuzhou.gov.cn",
  "Origin": "https://www.fuzhou.gov.cn",
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
    content_xpath = {'frames': frames_xpath,
                     'title': title_xpath,
                     'date': date_xpath}

    city_info = PageMother(city_info=city_info, is_headless=True,
                           thread_num=thread_num)

    city_info.fetch_web_by_requests(request_type='post_session', data_dict=data_dict, page_num_name=page_num_name,
                                    headers=headers, data_type='data', cleaned_method=extract_news_info)
