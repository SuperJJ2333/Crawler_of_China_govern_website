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
url = 'http://www.dongying.gov.cn/jsearchfront/interfaces/cateSearch.do'

data_json = "websiteid=370000000088000&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&p=3&pg=12&cateid=18021&pos=title&pq=&oq=&eq=&begin=&end=&tpl=2204&sortFields=[{'name':'top','clause':1},{'name':'score','clause':1}]"
data_dict = {'siteCode': '1301000003', 'tab': 'all', 'timestamp': '1718878865770',
             'wordToken': '0731c7435559f5ca77cca7a4a70e9f32', 'page': '1', 'pageSize': '20', 'qt': '学习考察',
             'timeOption': '0', 'sort': 'relevance', 'keyPlace': '0'}

json_str = '{"page":"4","keywords":"学习考察 考察学习","sort":"smart","site_id":"2","range":"site","position":"title","recommand":1,"gdbsDivision":"440000","service_area":1}'

json_str = json.loads(json_str)

params = {'websiteid': '370500000000000', 'q': '学习考察 考察学习', 'p': '3', 'pg': '10', 'cateid': '14400', 'pos': 'title,content', 'pq': '', 'oq': '', 'eq': '', 'begin': '', 'end': '', 'tpl': '2142', 'dimension_filenumber': '', 'dimension_fbjg': ''}

non_proxies = {
    "http": None,
    "https": None
}

headers = {"Host":"www.dongying.gov.cn","Connection":"keep-alive","Content-Length":"217","Accept":"application/json, text/javascript, */*; q=0.01","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","Content-Type":"application/x-www-form-urlencoded","Origin":"http://www.dongying.gov.cn","Referer":"http://www.dongying.gov.cn/jsearchfront/search.do?websiteid=370500000000000&searchid=4954&pg=&p=3&tpl=2142&cateid=14400&total=&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pq=&oq=&eq=&dimension_filenumber=&dimension_fbjg=&pos=title%2Ccontent&begin=&end=","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"user_cid=7039879a656c4a9db5830cb3363c06e3; hq=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0; user_sid=b61c0ac3254b4ce3bfb584145c5113af; sid=b1012adc335a3d46c797a0224dccd4e0; JSESSIONID=9F2C765E0575840935236BF31DFD9FF9; _city=%E5%B9%BF%E5%B7%9E%E5%B8%82; searchsign=cc03d09c7cc945b6b54f280c485d7e9d; zh_choose_207=s"}

fiddler_proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888"
}

# page.get(url=url, proxies=proxies)

# print(page.html)
# print(page.title)

# page.get(url, proxies=non_proxies)
response = requests.post(url, proxies=fiddler_proxies, verify=False, headers=headers, data=params)
# response = requests.post(url, proxies=non_proxies, verify=False, headers=headers, data=params)
# response = requests.post(url, proxies=non_proxies, verify=False, headers=headers, json=json_str)
# response = requests.post(url, proxies=non_proxies, verify=True, headers=headers, data=json_str)
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
