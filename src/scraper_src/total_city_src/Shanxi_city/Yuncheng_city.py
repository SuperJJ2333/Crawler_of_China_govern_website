import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('response', {})

    for item in data_dict:
        try:
            topic = item.get('TITLE', '')
            date = item.get('MOD_TIME', '')
            url = item.get('URL', '')
        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        news_info = {
            'topic': topic,
            'date': date,
            'url': url,
        }
        extracted_news_list.append(news_info)

    return extracted_news_list


if __name__ == '__main__':
    """
    请求方法：POST -- verify
    获取数据：API -- by_json
    提取方法：JSON -- response -- TITLE, MOD_TIME, URL
    """

    city_info = {
        'city_name': '运城市',
        'province_name': '山西省',
        'province': 'Shanxi',

        'base_url': 'https://www.yuncheng.gov.cn/search2/api/select',

        'total_news_num': 3440,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"742","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"zh_choose=n; __tins__21255789=%7B%22sid%22%3A%201720114072790%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201720115872790%7D; __51cke__=; __51laig__=1","Host":"www.yuncheng.gov.cn","Origin":"https://www.yuncheng.gov.cn","Referer":"https://www.yuncheng.gov.cn/newsearch/search.html?%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'q': 'TITLE:学习考察 考察学习  ', 'fq': 'STATUS:4 AND DEL_FLAG:false  AND SITE_ID:1 AND -CHANNEL_ROOT: "辅助栏目"', 'fl': 'TITLE,CONTENT,CHANNEL_ROOT,SITE_ID,CHANNEL_PATH,CHANNEL_ID_PATH,MOD_TIME,STATUS,WRITE_TIME,SITE_NAME,URL,PIC_URL,ID,DOC_ID,SUMMARY,KIND,CHAN_ID,DEL_FLAG,KIND,DEPT_NAME,DOMAIN,URL2', 'start': '0', '': '20', 'CHANNEL_ROOT': '', 'sort': 'score desc,SORT desc', 'facet': 'true', 'pageNum': '175', 'facet.mincount': '1', 'facet.limit': '10', 'facet.field': 'DEL_FLAG', 'hl': 'true', 'hl.fl': 'TITLE,CONTENT', 'hl.id': 'ID', 'hl.simple.pre': '<em>', 'hl.simple.post': '</em>', 'hl.maxAnalyzedChars': '-1', 'hl.fragsize': '120', 'hl.usePhraseHighlighter': 'true', 'hl.highlightMultiTerm': 'true'}

    page_num_name = 'start'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, proxies=fiddler_proxies, verify=False,
                      page_num_start=0, num_added_each_time=20)
    scraper.run()