import json
from datetime import datetime

import pandas as pd
from loguru import logger
from DrissionPage import ChromiumPage, ChromiumOptions
from bs4 import BeautifulSoup

from src.common.content_utils import save_to_excel, process_news_content, remove_duplicates


def get_Wuhu_web():
    name = "Wuhu_test"

    base_url = 'https://www.wuhu.gov.cn/whsearch/site/label/8888?_=0.8882243112451278&labelName=searchDataList&isJson=true&isForPage=true&target=&pageSize=20&titleLength=35&contentLength=80&showType=2&ssqdDetailTpl=35931&islight=true&columnId=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&subkeywords=&typeCode=all&isAllSite=true&platformCode=&siteId=&fromCode=&fuzzySearch=true&attachmentType=&datecode=&sort=intelligent&colloquial=true&orderType=0&minScore=&fileNum=&publishDepartment='
    co = ChromiumOptions().headless()
    page = ChromiumPage(co)
    # page = ChromiumPage()

    # 存储列表
    news_data = []

    total_page = 745
    # total_page = 5

    for page_num in range(1, total_page+1):
        # 新的目录页
        url = f"{base_url}&pageIndex={page_num}"

        # 获取标题与日期
        news_data = get_Wuhu_news_data_from_page(url, page, page_num, news_data)

        # 多线程遍历
        # unique_news = process_news_data(news_data, page, unique_news)

    page.quit()
    save_to_excel(news_data, name)


def get_Wuhu_news_data_from_page(url, page, page_num, articles):
    """
    从给定的URL加载新闻列表。
    参数:
    url -- 要访问的网址。
    page -- 用于访问URL的标签页对象。
    返回:
    news_data -- 从页面提取的新闻数据列表。
    """
    tab = page.new_tab()
    tab.get(url)
    logger.info(f"当前的页数：{page_num} - URL：{url}")
    html_content = tab.html

    # 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    if soup:
        # 获取无标签的文本
        json_str = soup.get_text()

        # 转换 JSON 字符串为 Python 字典
        data = json.loads(json_str)

        for article in data['data']['data']:
            title = article['title']
            link = article['link']
            date = article['createDate']
            try:
                # 解析日期字符串
                date_obj = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                continue
            # 只需要2018年的数据
            if date_obj.year != 2018:
                continue

            logger.info(f"{title}-{date}-获取成功")
            articles.append({
                'title': title,
                'link': link,
                'createDate': date
            })
    else:
        return logger.warning(f"没有响应-{url}")

    tab.close()
    return articles


def get_content():
    name = "Wuhu"

    co = ChromiumOptions().headless()
    page = ChromiumPage(co)

    df = pd.read_excel("../temp/Wuhu_test_news.xlsx")
    news_data = []
    unique_news = []

    for index, row in df.iterrows():
        news_data.append({
            'topic': row['title'],
            'url': row['link'],
            'date': row['createDate']
        })

    news_data = remove_duplicates(news_data)

    unique_news = process_news_content(news_data, page, unique_news)

    save_to_excel(unique_news, name)


if __name__ == '__main__':
    get_content()
