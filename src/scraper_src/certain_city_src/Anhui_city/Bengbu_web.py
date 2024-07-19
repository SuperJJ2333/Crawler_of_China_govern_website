import sys

from DrissionPage import ChromiumPage
from concurrent.futures import as_completed

from src.common.content_utils import *

logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss} - <level>{level}</level> - {message}</green>",
    level="INFO",
)


def get_bengbu_web():
    name = "bengbu"

    base_url = 'https://www.bengbu.gov.cn/site/search/6795621?isAllSite=true&platformCode=bengbu_gova,bengbu_govb,bengbu_govc,bengbu_govd,bengbu_govf&siteCode=&siteId=&columnIds=&typeCode=all&beginDate=2018-01-01&endDate=2018-12-12&fromCode=title&fuzzySearch=true&subkeywords=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&sort=intelligent&fileNum=&catIds=&orderType=0&flag=false&datecode=&pageSize=10'

    # co = ChromiumOptions().headless()
    # co = ChromiumOptions().auto_port()
    # page = ChromiumPage(co)
    # page = ChromiumPage(addr_or_opts=co)
    page = ChromiumPage()

    # 存储列表
    unique_news = []

    total_page = 18
    # total_page = 5

    # for page_num in range(1, total_page+1):
    #     # 新的目录页
    #     url = f"{base_url}&pageIndex={page_num}"
    #
    #     # 获取标题与日期
    #     news_data = get_bengbu_news_data_from_page(url, page, page_num)
    #
    #     # 多线程遍历
    #     unique_news = process_news_data(news_data, page, unique_news)

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {
            executor.submit(get_bengbu_news_data_from_page, f"{base_url}&pageIndex={page_num}",
                            page, page_num): page_num for page_num in range(1, total_page + 1)}
        for future in as_completed(future_to_url):
            news_data = future.result()
            news_data = remove_duplicates(news_data)
            if news_data:
                # 处理每页的新闻数据
                unique_news = process_news_content(news_data, page, unique_news)

    page.quit()
    save_to_excel(unique_news, name)


def get_bengbu_news_data_from_page(url, page, page_num):
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
    news_frames = tab.eles('xpath://*[@class="searchlistw"][2]/ul')
    titles = [frame.ele('xpath://li[1]/a') for frame in news_frames]
    dates = []
    for frame in news_frames:
        dates.append(frame.ele('xpath://li[3]/span[3]') or frame.ele('xpath://li[3]/span[2]'))

    news_data = fetch_news_data(titles, dates, url)
    tab.close()
    return news_data


if __name__ == '__main__':
    get_bengbu_web()
