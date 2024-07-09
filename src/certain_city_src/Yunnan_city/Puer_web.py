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
        data_list = data['data']['page']['records']
        # 遍历新闻列表
        for news_item in data_list:

            try:

                # 提取信息
                title = news_item['title']  # 提取标题
                news_url = news_item['columnurl']  # 提取新闻URL
                date = news_item['createDate']  # 提取发布日期

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
    city_info = {'name': 'Puer',
                 'province': 'Yunnan_city',
                 'total_news_num': 1000,
                 'each_page_num': 10,
                 'targeted_year': 2019,
                 'base_url': 'https://www.pes.gov.cn/aop_component//webber/search/search/search/queryPage'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    # 将JSON字符串转换成字典
    data_dict = '{"aliasName":"article_data,open_data,mailbox_data,guest_book","keyWord":"学习考察 考察学习","lastkeyWord":"学习考察 考察学习","searchKeyWord":false,"orderType":"score","searchType":"text","searchScope":3,"searchOperator":0,"searchDateType":"","searchDateName":"time.any_time","beginDate":"","endDate":"2024-05-21","language":"chinese","showId":"35ede40151f31c8873ed450acc7a93b3","auditing":["1","5"],"owner":"1948729862","token":"tourist","urlPrefix":"/aop_component/","page":{"current":0,"size":10,"pageSizes":[2,5,10,20,50,100],"total":0,"totalPage":0,"indexs":[]},"advance":false,"advanceKeyWord":"","lang":"i18n_zh_CN"}'

    data_dict = json.loads(data_dict)

    page_num_name = "page.current"
    # off_set = 10
    base_url = 'https:'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'
    headers = {
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Authorization": "tourist",
  "Content-Type": "application/json;charset=UTF-8",
  "Cookie": "JSESSIONID=FB26D7A0FC7A0089FD16D15B14CD84D5; appsearch_sessionid=CCEF72CBF72D3E50095A24B003761BD9",
  "Host": "www.pes.gov.cn",
  "Origin": "https://www.pes.gov.cn",
  "Referer": "https://www.pes.gov.cn/views/search/modules/resultpc/soso.html?query=eyJhbGlhc05hbWUiOiJhcnRpY2xlX2RhdGEsb3Blbl9kYXRhLG1haWxib3hfZGF0YSxndWVzdF9ib29rIiwia2V5V29yZCI6IuWtpuS5oOiAg+WvnyDogIPlr5/lrabkuaAiLCJsYXN0a2V5V29yZCI6IuWtpuS5oOiAg+WvnyIsInNlYXJjaEtleVdvcmQiOmZhbHNlLCJvcmRlclR5cGUiOiJzY29yZSIsInNlYXJjaFR5cGUiOiJ0ZXh0Iiwic2VhcmNoU2NvcGUiOjMsInNlYXJjaE9wZXJhdG9yIjowLCJzZWFyY2hEYXRlVHlwZSI6IiIsInNlYXJjaERhdGVOYW1lIjoidGltZS5hbnlfdGltZSIsImJlZ2luRGF0ZSI6IiIsImVuZERhdGUiOiIyMDI0LTA1LTIxIiwibGFuZ3VhZ2UiOiJjaGluZXNlIiwic2hvd0lkIjoiMzVlZGU0MDE1MWYzMWM4ODczZWQ0NTBhY2M3YTkzYjMiLCJhdWRpdGluZyI6WyIxIiwiNSJdLCJvd25lciI6IjE5NDg3Mjk4NjIiLCJ0b2tlbiI6InRvdXJpc3QiLCJ1cmxQcmVmaXgiOiIvYW9wX2NvbXBvbmVudC8iLCJwYWdlIjp7ImN1cnJlbnQiOjAsInNpemUiOjEwLCJwYWdlU2l6ZXMiOlsyLDUsMTAsMjAsNTAsMTAwXSwidG90YWwiOjY0LCJ0b3RhbFBhZ2UiOjcsImluZGV4cyI6WzEsMiwzLDQsNSw2LDddfSwiYWR2YW5jZSI6ZmFsc2UsImFkdmFuY2VLZXlXb3JkIjoiIiwibGFuZyI6ImkxOG5femhfQ04ifQ==",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
  "owner": "1948729862",
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
                                    headers=headers, data_type='json', cleaned_method=extract_news_info,
                                    base_url=base_url, is_begin_from_zero=True)
