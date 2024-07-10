import json
import re
from html import unescape
from urllib.parse import unquote

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('result', {})

    for item in data_dict:
        # 解码HTML实体
        news_item = unescape(item)
        try:
            # 正则表达式查找URL
            url_search = re.search(r"href='visit/link.do\?url=([^'&]+)", news_item)
            url = unquote(url_search.group(1)) if url_search else "No URL found"

            # 正则表达式查找日期
            date_search = re.search(r'时间:(\d{4}-\d{2}-\d{2})', news_item)
            date = date_search.group(1) if date_search else "No date found"

            # 正则表达式查找标题
            title_search = re.search(r'&title=([^&]+)', news_item)
            topic = unquote(title_search.group(1)) if title_search else "No title found"
        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        if not url.startswith('http') and not url.startswith('https'):
            url = 'http://www.gswuwei.gov.cn' + url

        news_info = {
            'topic': topic,
            'date': date,
            'url': url,
        }
        extracted_news_list.append(news_info)

    return extracted_news_list


if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：API
    提取方法：JSON -- result -- 
            re：unquote：href="visit/link.do\?url=([^"&]+), 
            r'class="jcse-news-date">([\d-]+)</span>', 
            r'&title=(.*?)\">'
    """

    city_info = {
        'city_name': '浙江省',
        'province_name': '浙江省',
        'province': 'province_web_data',
        'base_url': 'https://search.zj.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 12978,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"298","Content-Type":"application/x-www-form-urlencoded","Cookie":"user_sid=0f7a705ae4af4305ac4ca8bc9652d0f5; _q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; sid=00d1ae4d6eafe9cb939fa2e8e8d21aa6; JSESSIONID=3C1351F5FF8E9E772E30AB395C0A2BE7; searchsign=ba3a96ab118a48adb55d2f332c836437; searchid=aa212d845a9741438862d992d3b5e479; cna=PW7UHlaEJGICAf/////co69V; cssstyle=1; _ud_=07f0ac6395394b759a85340c9d28ac3e; zh_choose_undefined=s; arialoadData=false; zwlogBaseinfo=eyJsbF91c2VyaWQiOiIiLCJsb2dfc3RhdHVzIjoi5pyq55m75b2VIiwidXNlclR5cGUiOiJndWVzdCIsInNpdGVfaWQiOjEsInBhZ2VfbW9kZSI6IuW4uOinhOaooeW8jyJ9; session=dbf6ddfd9ff5474aaddc34951a62b3f1; aliyungf_tc=36c8c569804e2ad82596361667d9f0f3170f07055940a56a3d9c7e3562939ace; acw_tc=ac11000117205392078886629e6b0898b9b89946c61835cc454d67a900cd2c; SERVERID=daf947b71579cb2e324dcfdb35f0f984|1720539233|1720539036","Host":"search.zj.gov.cn","Origin":"https://search.zj.gov.cn","Referer":"https://search.zj.gov.cn/jsearchfront/search.do?websiteid=330000000000000&searchid=&pg=&p=3&tpl=1569&cateid=370&fbjg=&word=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&temporaryQ=&synonyms=&checkError=1&isContains=1&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&jgq=&eq=&begin=&end=&timetype=&_cus_pq_ja_type=&pos=title&sortType=1&siteCode=330000000000000&","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'websiteid': '330000000000000', 'pg': '10', 'p': '3', 'tpl': '1569', 'cateid': '370', 'word': '学习考察 考察学习', 'checkError': '1', 'isContains': '1', 'q': '学习考察 考察学习', 'pos': 'title,filenumber', 'sortType': '1', 'siteCode': '330000000000000'}

    page_num_name = 'p'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name)
    scraper.run()