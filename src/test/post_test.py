import time

import DrissionPage
import requests
import json
import certifi

from src.common.form_utils import *

import urllib3
from urllib3.util.ssl_ import create_urllib3_context

page = DrissionPage.SessionPage()

# 网址
url = 'http://www.rizhao.gov.cn/jsearchfront/interfaces/cateSearch.do'

data_json = 'websiteid=370500000000000&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&p=3&pg=10&cateid=14400&pos=title&pq=&oq=&eq=&begin=&end=&tpl=2142&dimension_filenumber=&dimension_fbjg='
data_dict = {'siteCode': '1301000003', 'tab': 'all', 'timestamp': '1718878865770',
             'wordToken': '0731c7435559f5ca77cca7a4a70e9f32', 'page': '1', 'pageSize': '20', 'qt': '学习考察',
             'timeOption': '0', 'sort': 'relevance', 'keyPlace': '0'}

json_str = '{"appendixType":"","beginDateTime":"","codes":"","dataTypeId":8,"configCode":"","endDateTime":"","granularity":"ALL","historySearchWords":[],"isSearchForced":0,"orderBy":"related","enableExactSearch":false,"pageNo":2,"pageSize":16,"searchBy":"title","searchWord":"考察学习","code":"189485830c1","customFilter":{"operator":"or","properties":[]},"filters":[]}'
json_str = json.loads(json_str)

params = {'websiteid': '371100000000000', 'q': '学习考察 考察学习', 'p': '1', 'pg': '10', 'cateid': '19481', 'pos': 'title', 'pq': '', 'oq': '', 'eq': '', 'begin': '', 'end': '', 'tpl': '1541', 'sortFields': 'null'}


non_proxies = {
    "http": None,
    "https": None
}

headers = {"Host":"www.rizhao.gov.cn","Accept":"application/json, text/javascript, */*; q=0.01","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","Content-Type":"application/x-www-form-urlencoded","Origin":"http://www.rizhao.gov.cn","Referer":"http://www.rizhao.gov.cn/jsearchfront/search.do?q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pos=title&p=1&webid=147&tpl=1541&websiteid=371100000000000&pg=&begin=&end=&searchid=6269&checkError=1","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"user_sid=18f0afa92741466fa48e34681e85731d; user_cid=c1905a6db60a4a269e1e195e0ce77359; hq=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; _city=%E5%B9%BF%E5%B7%9E%E5%B8%82; sid=188e0120828ab57da347d9805e9816d0; JSESSIONID=8D057775F02591C1FB2633DC8E240FEF; searchsign=c068e9881c684d7ebf31ef8c0912e858; zh_choose_147=s; wzaFirst=1; zh_choose_undefined=s","Content-Length":"135"}

fiddler_proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888"
}

# page.get(url=url, proxies=proxies)

# print(page.html)
# print(page.title)

# page.get(url, proxies=non_proxies)
response = requests.post(url, proxies=fiddler_proxies, verify=False, headers=headers, data=params)
# response = requests.post(url, proxies=non_proxies, verify=False, headers=headers)
# response = requests.post(url, proxies=fiddler_proxies, verify=False, headers=headers)
# response = requests.get(url, headers=headers)

# 将 response.content 解码为 utf-8
print(response.content.decode('utf-8'))

# url data没有
#
# url = page.ele('x://*[@id="results"]/div[1]/div[1]/a').attr('href')
# print(page.html)
# print(url)
