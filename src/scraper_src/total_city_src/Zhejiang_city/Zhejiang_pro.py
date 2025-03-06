import json
import re
from html import unescape
from urllib.parse import unquote

from bs4 import BeautifulSoup

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('result', {})

    for item in data_dict:
        html = item
        try:
            title_search = re.search(r"<a target=\"_blank\" href='[^']+?'>(.*?)</a>", html)
            date_search = re.search(r"时间:(\d{4}-\d{2}-\d{2})", html)
            url_search = re.search(r"<a target=\"_blank\" href='([^']+)'", html)

            if title_search:
                title = re.sub(r'<[^>]*>', '', title_search.group(1))  # Remove HTML tags
                topic = unescape(title)  # Convert HTML entities to normal text
            else:
                topic = "No Title Found"

            date = date_search.group(1) if date_search else "No Date Found"
            url = url_search.group(1) if url_search else "No URL Found"

        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        if not url.startswith('http') and not url.startswith('https'):
            url = 'https://search.zj.gov.cn/jsearchfront/' + url

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
        'province': 'Zhejiang',
        'base_url': 'https://search.zj.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 1500,
        'each_page_news_num': 10,
    }

    headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br, zstd",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
               "Content-Type": "application/x-www-form-urlencoded",
               "Cookie": "user_sid=0f7a705ae4af4305ac4ca8bc9652d0f5; _q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; sid=ec0dc0363525a862a398fd26067526cf; JSESSIONID=D9E5C43A316B3889F4AEDDB8897B4FF8; searchsign=197012db54e9420eb827de5dc8288c30; searchid=ecf0bb0a20b7414fba179272fde65821; cna=PW7UHlaEJGICAf/////co69V; zh_choose_undefined=s; cssstyle=1; session=2601c3351bdc49759ea32f8c0de271d0; zwlogBaseinfo=eyJsbF91c2VyaWQiOiIiLCJsb2dfc3RhdHVzIjoi5pyq55m75b2VIiwidXNlclR5cGUiOiJndWVzdCIsInNpdGVfaWQiOjEsInBhZ2VfbW9kZSI6IuW4uOinhOaooeW8jyJ9; arialoadData=false; aliyungf_tc=917df4b7e777d163c9e01c86b15ef7cc63439c95937323304a2ae8bafd0c74c4; acw_tc=ac11000117201194537463887e993efaad4c7a6fc66f44db9fb3f352c6396e; _ud_=07f0ac6395394b759a85340c9d28ac3e; SERVERID=65057fbec3ef1a088569d392e2faddc9|1720119632|1720119443",
               "Host": "search.zj.gov.cn", "Origin": "https://search.zj.gov.cn",
               "Referer": "https://search.zj.gov.cn/jsearchfront/search.do?websiteid=330100000000000&searchid=&pg=&p=2&tpl=1569&cateid=370&fbjg=&word=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&temporaryQ=&synonyms=&checkError=1&isContains=1&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&jgq=&eq=&begin=&end=&timetype=&_cus_pq_ja_type=&pos=title&sortType=1&siteCode=330101000000000&",
               "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
               "X-Requested-With": "XMLHttpRequest",
               "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
               "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\""}

    post_data = {'websiteid': '330100000000000', 'pg': '10', 'p': '2', 'tpl': '1569', 'cateid': '370',
                 'word': '学习考察 考察学习', 'checkError': '1', 'isContains': '1', 'q': '学习考察 考察学习',
                 'pos': 'filenumber,title,content,keyword', 'sortType': '1', 'siteCode': '330101000000000'}

    page_num_name = 'p'

    city_code = {
        # '宁波市': '330200000000000',
        # '杭州市': '330100000000000',
        # '台州市': '331000000000000',
        # '舟山市': '330900000000000',
        # '绍兴市': '330600000000000',
        # '湖州市': '330500000000000',
        # '丽水市': '331100000000000',
        '衢州市': '330800000000000',
        '金华市': '330700000000000',
        '温州市': '330300000000000',
        '嘉兴市': '330400000000000'
    }

    for city_name, city_code in city_code.items():
        post_data['websiteid'] = city_code
        post_data['siteCode'] = city_code

        city_info['city_name'] = city_name

        scraper = Scraper(city_info, method='post', data_type='json',
                          headers=headers, extracted_method=extract_news_info, is_headless=True,
                          post_data=post_data, page_num_name=page_num_name)
        scraper.session.post(url=city_info['base_url'], headers=headers, data=post_data, proxies=scraper.proxies)
        scraper.total_news_num = scraper.session.json.get('total')
        scraper.total_page_num = scraper.count_page_num()
        print(f'{city_name}市共{scraper.total_news_num}条新闻，{scraper.total_page_num}页')

        scraper.run()
