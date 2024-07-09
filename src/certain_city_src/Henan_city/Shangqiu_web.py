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
    if 'rows' in data:
        data_list = data['rows']
        # 遍历新闻列表
        for news_item in data_list:
            # 提取所需的信息
            title = news_item.get('articleTitle', '')  # 若无标题，默认值
            if base_url:
                news_url = base_url + news_item.get('articleUri', '')  # 若无 URL，默认值
            else:
                news_url = news_item.get('articleUri', '')
            publish_date = news_item.get('articlePublishTime', '')  # 若无发布日期，默认值

            news_dict = {
                'topic': title,
                'url': news_url,
                'date': publish_date
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
        logger.warning("Json格式设置得有问题，请重新设置")

    # 返回结果列表
    return news_list


if __name__ == '__main__':
    # 隧道域名:端口号
    tunnel = "o268.kdltps.com:15818"

    # 用户名密码方式
    username = "t11473268717266"
    password = "t060njhi"
    proxies = "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},

    # 新闻目录参数
    total_news_num = 1420
    each_page_num = 15
    time_limit = 2018

    # 爬虫信息
    name = 'Shangqiu'
    province = 'Henan'
    url = 'https://www.shangqiu.gov.cn/s?as=true&qal=&qad=%e5%ad%a6%e4%b9%a0%e8%80%83%e5%af%9f&qo=&qn=&bt=2017%2f01' \
          '%2f01&et=2017%2f12%2f31&kp=0&ps=10&sids=1%2c55%2c49%2c29%2c37%2c56%2c60%2c40%2c33%2c38%2c58%2c46%2c50%2c23' \
          '%2c59%2c22%2c27%2c21%2c32%2c28%2c66%2c20%2c43%2c24%2c30%2c35%2c31%2c39%2c48%2c47%2c41%2c34%2c25%2c26%2c36' \
          '%2c45%2c68%2c44%2c69%2c70%2c71%2c73%2c74%2c75&siids=2%2c3%2c4%2c5%2c39%2c40%2c517&p={page_num}&vc='
    thread_num = 1

    # 监听信息
    listen_path = 'searchapi.anyang.gov.cn/open/api/'

    # xpath信息
    frames_xpath = 'x://body/div[5]/div[2]/div[2]/ul/li'
    title_xpath = 'x://h4/a'
    date_xpath = ['x://div/text()']
    content_xpath = {'frames': frames_xpath,
                     'title': title_xpath,
                     'date': date_xpath}

    # requests信息
    data_dict = {'q': '考察学习', 'forCatalogType': '0',
                 'token4': '6058461769fc4094a95e8bd4bfbf9485',
                 'siteId': 'efc127c860d248459e9b75bc458977d7',
                 'offset': '{page_num}', 'limit': '10'}
    off_set = 10
    page_num_name = 'offset'
    base_url = 'http://www.luohe.gov.cn'

    city_info = PageMother(name=name, url=url, targeted_year=time_limit, total_news_num=total_news_num,
                           each_page_num=each_page_num, province=province, thread_num=thread_num,
                           content_xpath=content_xpath, is_headless=True)

    city_info.fetch_web_multiple()

    # city_info.get_web_by_requests(request_type='post', data_dict=data_dict, off_set=off_set,
    #                               page_num_name=page_num_name,
    #                               cleaned_method=extract_news_info,
    #                               base_url=base_url)
