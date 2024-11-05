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

url = 'https://www.dxal.gov.cn/search5/search/s'
header = None

# 创建一个空的代理字典
non_proxies = {
    "http": None,
    "https": None
}

headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"449","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"name=value; name=value; name=value; verid=false; arialoadData=false; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; 2327000040=5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oCzogIPlr5/lrabkuaAs5a2m5Lmg6ICD5a+f","Host":"www.dxal.gov.cn","Origin":"https://www.dxal.gov.cn","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}


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

json_str = 'searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&siteCode=2327000040&column=%25E5%2585%25A8%25E9%2583%25A8&pageSize=10&pageNum=1&sonSiteCode=&checkHandle=1&searchSource=0&areaSearchFlag=0&secondSearchWords=&topical=&docName=&label=&countKey=0&uc=0&left_right_index%3D=0&searchBoxSettingsIndex=0&orderBy=0&startTime=&endTime=&timeStamp=0&strFileType=&wordPlace=1'

# page.get(url, headers=headers, verify=False)
# page.post(url, data=data_dict, proxies=proxies, headers=headers)
# page.post(url, params=params_dict, proxies=non_proxies, headers=headers)
# page.post(url, params=params_dict, proxies=non_proxies, headers=headers, verify=False)
page.post(url, json=json_str, proxies=non_proxies, headers=headers, verify=False)

# request = requests.post(url, params=data_dict, proxies=non_proxies, headers=headers, verify=True)

# print(request.text)


print(page.html)
print(page.json)
print(page.title)
