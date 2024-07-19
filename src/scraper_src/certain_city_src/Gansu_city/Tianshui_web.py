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

                title = news_item['title']

                news_url = news_item['url']

                # 寻找发布日期
                date = news_item['createDate']
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
    URL获取方式：Drissionpage 模拟访问 Listen获取post数据
    URL返回格式：json
    """

    # 爬虫基本信息
    city_info = {'name': 'Tianshui',
                 'province': 'Gansu',
                 'total_news_num': 2348,
                 'each_page_num': 10,
                 'targeted_year': 2022,
                 'base_url': 'https://www.tianshui.gov.cn/aop_component//webber/search/search/search/queryPage'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    headers = {
        "Host": "www.tianshui.gov.cn",
        "sec-ch-ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "owner": "1912126876",
        "sec-ch-ua-mobile": "?0",
        "Authorization": "tourist",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "sec-ch-ua-platform": "\"Windows\"",
        "Origin": "https://www.tianshui.gov.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.tianshui.gov.cn/views/search/modules/resultpc/soso.html?query=eyJhbGlhc05hbWUiOiJhcnRpY2xlX2RhdGEsb3Blbl9kYXRhLG1haWxib3hfZGF0YSxhcnRpY2xlX2ZpbGUiLCJrZXlXb3JkIjoi5a2m5Lmg6ICD5a+fIiwibGFzdGtleVdvcmQiOiLogIPlr5/lrabkuaAiLCJzZWFyY2hLZXlXb3JkIjpmYWxzZSwib3JkZXJUeXBlIjoic2NvcmUiLCJzZWFyY2hUeXBlIjoidGV4dCIsInNlYXJjaFNjb3BlIjozLCJzZWFyY2hPcGVyYXRvciI6MCwic2VhcmNoRGF0ZVR5cGUiOiIiLCJzZWFyY2hEYXRlTmFtZSI6InRpbWUuYW55X3RpbWUiLCJiZWdpbkRhdGUiOiIiLCJlbmREYXRlIjoiMjAyNC0wNS0wOCIsInNob3dJZCI6ImMyZWUxMzA2NWFhZTg1ZDdhOTk4YjhhM2NkNjQ1OTYxIiwiYXVkaXRpbmciOlsiMSJdLCJvd25lciI6IjE5MTIxMjY4NzYiLCJ0b2tlbiI6InRvdXJpc3QiLCJ1cmxQcmVmaXgiOiIvYW9wX2NvbXBvbmVudC8iLCJwYWdlIjp7ImN1cnJlbnQiOjAsInNpemUiOjEwLCJwYWdlU2l6ZXMiOlsyLDUsMTAsMjAsNTAsMTAwXSwidG90YWwiOjE2MzQ4LCJ0b3RhbFBhZ2UiOjE2MzUsImluZGV4cyI6WzEsMiwzLDQsNSw2LDcsOCw5LDEwXX0sImFkdmFuY2UiOmZhbHNlLCJhZHZhbmNlS2V5V29yZCI6IiIsImxhbmciOiJpMThuX3poX0NOIn0=",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "coverlanguage_bb=0; JSESSIONID=A3DAEB6717DC8E58DC4051803C9B0F0E; appsearch_sessionid=8435F3371F41E0CEADFC48C72302A4DD"
    }

    json_str = '{"aliasName":"article_data,open_data,mailbox_data,article_file","keyWord":"学习考察","lastkeyWord":"学习考察","searchKeyWord":false,"orderType":"score","searchType":"text","searchScope":"3","searchOperator":0,"searchDateType":"custom","searchDateName":"2021-01-01-2021-12-31","beginDate":"2021-01-01","endDate":"2021-12-31","showId":"c2ee13065aae85d7a998b8a3cd645961","auditing":["1"],"owner":"1912126876","token":"tourist","urlPrefix":"/aop_component/","page":{"current":9,"size":10,"pageSizes":[2,5,10,20,50,100],"total":2348,"totalPage":235,"indexs":[1,2,3,4,5,6,7,8,9,10]},"advance":false,"advanceKeyWord":"","lang":"i18n_zh_CN"}'
    data_dict = json.loads(json_str)
    page_num_name = "page.current"
    # off_set = 5
    base_url = 'https:'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'
    """get信息"""

    city_info = PageMother(city_info=city_info, is_headless=True)

    city_info.fetch_web_by_requests(request_type='post_session', cleaned_method=extract_news_info,
                                    data_dict=data_dict,
                                    page_num_name=page_num_name, headers=headers, base_url=base_url)
