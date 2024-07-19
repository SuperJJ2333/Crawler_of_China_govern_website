from lxml import html

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
            # 创建 BeautifulSoup 对象来解析 HTML
            doc = html.fromstring(news_item)

            try:
                # 提取数据
                title = doc.xpath('//div[@class="jcse-news-title"]/a/text()')[0] if doc.xpath(
                    '//div[@class="jcse-news-title"]/a/text()') else "Title not found"
                news_url = doc.xpath('//div[@class="jcse-news-title"]/a/@href')[0] if doc.xpath(
                    '//div[@class="jcse-news-title"]/a/@href') else "URL not found"
                date = doc.xpath('//div[@class="jcse-news-other-info"]/span[@class="jcse-news-date"]/text()')[
                    0] if doc.xpath(
                    '//div[@class="jcse-news-other-info"]/span[@class="jcse-news-date"]/text()') else "Date not found"

            except Exception as e:
                # 提取标题和链接
                title = soup.find('a').text
                news_url = soup.find('a')['href']

                # 提取发布日期
                date = soup.find('span', class_='szf_rq').text.strip()
                # logger.warning(f"部分数据不存在：{e}")
                # continue

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
    URL获取方式：api post访问
    URL返回格式：HTMl字典
    """

    # 爬虫基本信息
    city_info = {'name': 'Jining',
                 'province': 'Shandong',
                 'total_news_num': 91,
                 'each_page_num': 12,
                 'targeted_year': 2019,
                 'base_url': 'https://www.jining.gov.cn/jsearchfront/interfaces/cateSearch.do'
                 }
    # 可选参数
    thread_num = 5

    """post信息"""
    data_dict = {'websiteid': '370800000000000', 'q': '学习考察 考察学习', 'p': '2', 'pg': '12',
                 'cateid': '297', 'pos': 'title,content', 'begin': '20180101', 'end': '20181231',
                 'tpl': '101'}

    page_num_name = 'p'
    # off_set = 5
    base_url = 'https://www.jining.gov.cn/jsearchfront/'
    # change_url = 'http://www.heze.gov.cn/els-service/search/new/'

    headers = {
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Content-Type": "application/x-www-form-urlencoded",
  "Cookie": "JSESSIONID=9f0e09f12c330fa2488e70c5d06c; user_sid=d20e98bb57e445919313f495daf757fa; user_cid=7f625a5d718549848d259ac76020499d; hq=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%2C%E4%B9%9D%E8%80%81%E5%8C%BA%2C%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F; searchsign=26f81bf464b0433ca3f14b0be574ac87; sid=978203121de9a52c12a4c7eed57f8bb6; zh_choose_1=s; _q=å­¦ä¹ è€ƒå¯Ÿ è€ƒå¯Ÿå­¦ä¹",
  "Host": "www.jining.gov.cn",
  "Origin": "https://www.jining.gov.cn",
  "Referer": "https://www.jining.gov.cn/jsearchfront/search.do?websiteid=370800000000000&searchid=2&pg=&p=2&tpl=101&cateid=297&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pq=&oq=&eq=&pos=title%2Ccontent&begin=20180101&end=20181231",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
  "X-Requested-With": "XMLHttpRequest",
  "sec-ch-ua": "\"Microsoft Edge\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\""
}

    city_info = PageMother(city_info=city_info, is_headless=True)

    city_info.fetch_web_by_requests(request_type='post_session', data_dict=data_dict,
                                    page_num_name=page_num_name, data_type='data',
                                    cleaned_method=extract_news_info, base_url=base_url)
