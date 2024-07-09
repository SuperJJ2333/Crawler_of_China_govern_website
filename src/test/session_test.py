import time

import DrissionPage
import requests
import json

from src.common.form_utils import *

import urllib3
from urllib3.util.ssl_ import create_urllib3_context

page = DrissionPage.SessionPage()

url = 'https://www.jz.gov.cn/hhjsjgy.jsp?wbtreeid=1001&keyword=5a2m5Lmg6ICD5a%2BfIOiAg%2BWvn%2BWtpuS5oA%3D%3D&cc=W10' \
      '%3D&ot=1&rg=4&tg=5&clid=0&currentnum=2'
header = None

# 创建一个空的代理字典
non_proxies = {
    "http": None,
    "https": None
}

headers = {
  "Host": "www.jz.gov.cn",
  "Connection": "keep-alive",
  "sec-ch-ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-User": "?1",
  "Sec-Fetch-Dest": "document",
  "Referer": "https://www.jz.gov.cn/hhjsjgy.jsp?wbtreeid=1001&keyword=5a2m5Lmg6ICD5a%2BfIOiAg%2BWvn%2BWtpuS5oA%3D%3D&cc=W10%3D&ot=1&rg=4&tg=5&clid=0&currentnum=6",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Cookie": "HWWAFSESID=d506cac52811118f37; HWWAFSESTIME=1715871684373; JSESSIONID=2d47a3ecbdfc1bedc329dd7248b4"
}

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

json_str = 'siteCode=3713000037&tab=bz&timestamp=1715158913819&wordToken=e8f8716f75089af50052448c127596d9&page=3&pageSize=20&qt=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&timeOption=2&sort=relevance&keyPlace=0&fileType=&startDateStr=2018-01-01&endDateStr=2018-12-31'

page.get(url, headers=headers, verify=False)
# page.post(url, data=data_dict, proxies=proxies, headers=headers)

print(page.html)
print(page.title)
