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
url = 'https://search.gd.gov.cn/api/search/all'

data_json = "websiteid=370000000088000&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&p=3&pg=12&cateid=18021&pos=title&pq=&oq=&eq=&begin=&end=&tpl=2204&sortFields=[{'name':'top','clause':1},{'name':'score','clause':1}]"
data_dict = {'siteCode': '1301000003', 'tab': 'all', 'timestamp': '1718878865770',
             'wordToken': '0731c7435559f5ca77cca7a4a70e9f32', 'page': '1', 'pageSize': '20', 'qt': '学习考察',
             'timeOption': '0', 'sort': 'relevance', 'keyPlace': '0'}

json_str = '{"page":"4","keywords":"学习考察 考察学习","sort":"smart","site_id":"2","range":"site","position":"title","recommand":1,"gdbsDivision":"440000","service_area":1}'

json_str = json.loads(json_str)

params = {'searchWord': '%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F', 'siteCode': '2300000061', 'column': '%E5%85%A8%E9%83%A8', 'pageSize': '10', 'pageNum': '2', 'checkHandle': '1', 'searchSource': '0', 'areaSearchFlag': '0', 'secondSearchWords': '', 'topical': '', 'docName': '', 'label': '', 'countKey': '0', 'uc': '0', 'left_right_index=': '0', 'searchBoxSettingsIndex': '0', 'orderBy': '1', 'startTime': '', 'endTime': '', 'timeStamp': '0', 'strFileType': '', 'wordPlace': '0'}

non_proxies = {
    "http": None,
    "https": None
}

headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"371","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"yfx_c_g_u_id_10000001=_ck24070203030416963145628475696; yfx_sv_c_g_u_id=_ck24070203030416963145628475696; yfx_f_l_v_t_10000001=f_t_1719860584659__r_t_1720533945595__v_t_1720533945595__r_c_1; yfx_mr_10000001=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_mr_f_10000001=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_key_10000001=; JSESSIONID=1E0D8F38DF77E38664A82233F4F188EB; arialoadData=true; route=bea1247a7b00595e282a28e54893eb3b; 2300000061=5a2m5Lmg6ICD5a+fLOiAg+Wvn+WtpuS5oCzlrabkuaDogIPlr58g6ICD5a+f5a2m5Lmg","Host":"www.hlj.gov.cn","Origin":"https://www.hlj.gov.cn","Referer":"https://www.hlj.gov.cn/search5/html/searchResult_heilongjiang.html?siteCode=2300000061&searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&column=%2525E5%252585%2525A8%2525E9%252583%2525A8%26&left_right_index=0&searchSource=1","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

fiddler_proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888"
}

# page.get(url=url, proxies=proxies)

# print(page.html)
# print(page.title)

# page.get(url, proxies=non_proxies)
# response = requests.post(url, proxies=fiddler_proxies, verify=False, headers=headers, data=params)
# response = requests.post(url, proxies=non_proxies, verify=False, headers=headers, data=params)
# response = requests.post(url, proxies=non_proxies, verify=False, headers=headers, json=json_str)
response = requests.post(url, proxies=non_proxies, verify=True, headers=headers, data=json_str)
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
