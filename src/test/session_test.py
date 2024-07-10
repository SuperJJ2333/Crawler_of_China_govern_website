import time

import DrissionPage
import requests
import json

from src.common.form_utils import *

import urllib3
from urllib3.util.ssl_ import create_urllib3_context
from urllib.parse import urlencode
import urllib.parse

page = DrissionPage.SessionPage()

url = 'https://intellsearch.jl.gov.cn/api/data/list'
header = None

# 创建一个空的代理字典
non_proxies = {
    "http": None,
    "https": None
}

headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"771","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"_trs_uv=ly41tlqg_79_f0tk; trs_search_uv=4FC1B33D9B3B4043BA1AECC2D51B930F432; wzws_sessionid=gTVmNDU5MaBmjSuigDEyMC4yMzYuMTYzLjExMIIwNzY0YzU=; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221907234ba7f80-0599e184cf9bfd-4c657b58-1327104-1907234ba80489%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkwNzIzNGJhN2Y4MC0wNTk5ZTE4NGNmOWJmZC00YzY1N2I1OC0xMzI3MTA0LTE5MDcyMzRiYTgwNDg5In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221907234ba7f80-0599e184cf9bfd-4c657b58-1327104-1907234ba80489%22%7D","Host":"intellsearch.jl.gov.cn","Origin":"https://intellsearch.jl.gov.cn","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}


proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888"
}

data_dict = {"aliasName": "article_data,open_data,mailbox_data,article_file", "keyWord": "学习考察",
             "lastkeyWord": "学习考察", "searchKeyWord": 'false', "orderType": "score", "searchType": "text",
             "searchScope": 3, "searchOperator": 0, "searchDateType": "custom",
             "searchDateName": "2021-01-01-2021-12-31",
             "beginDate": "2021-01-01", "endDate": "2021-12-31", "showId": "c2ee13065aae85d7a998b8a3cd645961",
             "auditing": ["1"], "owner": "1912126876", "token": "tourist", "urlPrefix": "/aop_component/",
             "page": {"current": 5, "size": 10, "pageSizes": [2, 5, 10, 20, 50, 100], "total": 2348, "totalPage": 235,
                      "indexs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}, "advance": 'false', "advanceKeyWord": "",
             "lang": "i18n_zh_CN"}

encoded_params = "%7B%22word%22%3A%22%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%22%2C%22page%22%3A2%2C%22size%22%3A20%2C%22stype%22%3A%2210%22%2C%22area%22%3A%22220000%22%2C%22atype%22%3A%221%22%2C%22dept%22%3A%22%22%2C%22ttype%22%3A%220%22%2C%22start%22%3A%22%22%2C%22end%22%3A%22%22%2C%22itype%22%3A%22%22%2C%22mattType%22%3A%220%22%2C%22serverType%22%3A%220%22%2C%22sort%22%3A0%2C%22aword%22%3A%22%22%2C%22hword%22%3A%22%22%2C%22nword%22%3A%22%22%2C%22dtword%22%3A%22%22%2C%22scope%22%3A%221%22%2C%22selecttp%22%3A%220%22%2C%22filetype%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22fileyear%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22stypeChild%22%3A%220%22%2C%22hs%22%3A%220%22%2C%22flag%22%3A%22%22%2C%22satisfiedId%22%3A%22527D9B2B57874665A571E9585ED97717813%22%7D"


# 解码URL编码的字符串
decoded_params = urllib.parse.unquote(encoded_params)

params_dict = json.loads(decoded_params)

json_str = 'siteCode=3713000037&tab=bz&timestamp=1715158913819&wordToken=e8f8716f75089af50052448c127596d9&page=3&pageSize=20&qt=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&timeOption=2&sort=relevance&keyPlace=0&fileType=&startDateStr=2018-01-01&endDateStr=2018-12-31'

# page.get(url, headers=headers, verify=False)
# page.post(url, data=data_dict, proxies=proxies, headers=headers)
# page.post(url, params=params_dict, proxies=non_proxies, headers=headers)
page.post(url, params=params_dict, proxies=non_proxies, headers=headers, verify=False)

# request = requests.post(url, params=data_dict, proxies=non_proxies, headers=headers, verify=True)

# print(request.text)


print(page.html)
print(page.json)
print(page.title)
