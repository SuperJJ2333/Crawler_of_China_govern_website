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
    if 'page' in data:
        data_list = data['page']['content']
        # 遍历新闻列表
        for news_item in data_list:

            title = news_item['title']
            news_url = news_item['url']
            date = news_item['docreltime']

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
    city_info = {'name': 'Nanjing',
                 'province': 'Sichuan',
                 'total_news_num': 233,
                 'each_page_num': 10,
                 'targeted_year': 2017,
                 'base_url': 'https://www.nanjing.gov.cn/igs/front/search.jhtml?code=c1c8a0a187b3404a9e7e1b048f90610c'
                             '&advancedQuery.root.keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5'
                             '%AD%A6%E4%B9%A0&pageSize=10&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83'
                             '%E5%AF%9F%E5%AD%A6%E4%B9%A0&searchWord2=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83'
                             '%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=10&time=2016-01-01,2016-12-31&type=&pageNumber={page_num}'
                 }
    # 可选参数
    thread_num = 5

    """xpath信息"""
    frames_xpath = 'x://*[@id="search_hasreslut"]/div[2]/div[2]/div[1]/div[2]/ul'
    title_xpath = 'x://li[1]/a'
    date_xpath = ['x://li[2]/span[2]',
                  'x://li[2]/span[3]']
    content_xpath = {'frames': frames_xpath,
                     'title': title_xpath,
                     'date': date_xpath}

    headers = {
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Cookie": "JSESSIONID=0509433EA440017CC799B5F7B70EDB22; __jsluid_s=51666b46aef071e6a7303462b44eead6; _gscu_1266880124=1627367332m2uz13; _gscbrs_1266880124=1; TrsAccessMonitor=TrsAccessMonitor-1716273675000-615480141; token=1955a216-a86c-4d93-90db-65eec74309a1; uuid=1955a216-a86c-4d93-90db-65eec74309a1; RANGERS_WEB_ID=7371318673476993280; RANGERS_SAMPLE=0.3066096990411733; _gscs_1266880124=t1627823224cs6n13|pv:3",
  "Host": "www.nanjing.gov.cn",
  "Referer": "https://www.nanjing.gov.cn/site/zgnj/search.html?searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=10&pageSize=10&searchWord2=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&type=&time=2016-01-01,2016-12-31&advancedQuery.root.keyword=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
  "sec-ch-ua": "\"Microsoft Edge\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\""
}

    city_info = PageMother(city_info=city_info, is_headless=True, thread_num=thread_num)

    city_info.fetch_web_by_requests(request_type='get', cleaned_method=extract_news_info)
