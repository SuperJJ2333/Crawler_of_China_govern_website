import sys

from DrissionPage import ChromiumPage, ChromiumOptions
from concurrent.futures import as_completed

from src.common.content_utils import *

logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss} - <level>{level}</level> - {message}</green>",
    level="INFO",
)


def get_Hefei_web():
    name = "Anhui"

    base_url = 'https://www.hefei.gov.cn/site/search/6784331?typeCode=all&fuzzySearch=true&orderType=0&oldKeywords=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&dateKey=publishDate&beginDate=2016-01-01&endDate=2016-12-31&fromCode=&colloquial=true&sort=intelligent&isAllSite=true&platformCode=&siteId=&columnId=&subkeywords='

    co = ChromiumOptions().headless()
    page = ChromiumPage(co)
    # page = ChromiumPage()

    # 存储列表
    unique_news = []

    total_page = 600
    # total_page = 5

    # for page_num in range(1, total_page+1):
    #     # 新的目录页
    #     url = f"{base_url}&pageIndex={page_num}"
    #
    #     # 获取标题与日期
    #     news_data = get_news_data_from_page(url, page, page_num)
    #
    #     # 多线程遍历
    #     unique_news = process_news_data(news_data, page, visited, unique_news)


    # futures = []
    # with ThreadPoolExecutor(max_workers=10) as executor:
    #     for page_num in range(1, total_page + 1):
    #         url = f"{base_url}&pageIndex={page_num}"
    #         future = executor.submit(get_news_data_from_page, url, page, page_num)
    #         futures.append(future)
    #
    # for future in as_completed(futures):
    #     news_data = future.result()
    #     news_data = remove_duplicates(news_data)
    #     if news_data:
    #         unique_news, visited = process_news_data(news_data, page, visited, unique_news)

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {
            executor.submit(get_Hefei_news_data_from_page, f"{base_url}&pageIndex={page_num}",
                            page, page_num): page_num for page_num in range(1, total_page + 1)}
        for future in as_completed(future_to_url):
            news_data = future.result()
            news_data = remove_duplicates(news_data)
            if news_data:
                # 处理每页的新闻数据
                unique_news = process_news_content(news_data, page, unique_news)

    page.quit()
    save_to_excel(unique_news, name)


def get_Hefei_news_data_from_page(url, page, page_num):
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
    news_frames = tab.eles('xpath://*[@id="search_list"]/ul')
    titles = tab.eles('xpath://*[@id="search_list"]/ul/li[1]/a')
    dates = [frame.ele('xpath://li[3]/span[2]') or frame.ele('xpath://li/table/tbody/tr[3]/td[2]') for frame in news_frames]

    news_data = fetch_news_data(titles, dates)
    tab.close()
    return news_data


if __name__ == '__main__':
    get_Wuhu_web()
