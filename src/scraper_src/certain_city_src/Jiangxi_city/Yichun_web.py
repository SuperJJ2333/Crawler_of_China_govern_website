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
    if 'searchTotal' in data:
        data_list = data['searchTotal']
        # 遍历新闻列表
        for news_item in data_list:

            try:

                # 提取信息
                title = news_item['title']  # 提取标题
                news_url = news_item['url']  # 提取新闻URL
                date = news_item['pubDate']  # 提取发布日期

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
    city_info = {'name': 'Yichun',
                 'province': 'Jiangxi',
                 'total_news_num': 207,
                 'each_page_num': 10,
                 'targeted_year': 2019,
                 'base_url': 'https://www.yichun.gov.cn/search4/commonAggs'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    # 将JSON字符串转换成字典
    data_dict = {'searchWord': '%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0', 'siteCode': '3609000002',
                 'column': '%E6%94%BF%E5%8A%A1%E5%85%AC%E5%BC%80', 'wordPlace': '0',
                 'orderBy': '2', 'startTime': '',
                 'endTime': '', 'pageSize': '10', 'pageNum': '0',
                 'timeStamp': '5', 'checkHandle': '1', 'areaSearchFlag': '0', 'countKey': '0',
                 'manualWord': '%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F'}

    page_num_name = "pageNum"
    # off_set = 10
    base_url = 'http://www.yingtan.gov.cn/jsearchfront/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'
    headers = {
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "Cookie": "proName=search4/; firstWord=%u5B66%u4E60%u8003%u5BDF; SECKEY_ABVK=TXuIX6p6HNd6ayGiHg9HgCSF8P+xpcuhWy/gD0VG/RQ%3D; HttpOnly; userSearch=siteCode-3609000002&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchTime-20240521112304&searchUseTime-189; SESSION_WEB_CACHE_KEY=b6848617c6a54144964694814298cd6f; Hm_lvt_72920cca32daf35e7e46dfa6ccc27328=1716213051; Hm_lpvt_72920cca32daf35e7e46dfa6ccc27328=1716213051; HttpOnly; arialoadData=true; ariawapChangeViewPort=true; HWWAFSESID=3d86079e31c832d46c; HWWAFSESTIME=1716261682443; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; 3609000002=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oCzlrabkuaDogIPlr58=; JSESSIONID=F75ED0593B58C0176818B55213CD5672",
  "Host": "www.yichun.gov.cn",
  "Origin": "https://www.yichun.gov.cn",
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
                                    headers=headers, data_type='data', cleaned_method=extract_news_info,
                                    base_url=base_url, is_begin_from_zero=True)
