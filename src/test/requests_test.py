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
url = 'https://www.gansu.gov.cn/guestweb4/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&column=%25E5%2585%25A8%25E9%2583%25A8&wordPlace=1&orderBy=0&startTime=&endTime=&pageSize=10&pageNum={page_num}&timeStamp=0&siteCode=6200000001&sonSiteCode=&checkHandle=1&strFileType=&govWorkBean=%257B%257D&sonSiteCode=&areaSearchFlag=-1&secondSearchWords=&topical=&pubName=&countKey=0&uc=0&isSonSite=false&left_right_index=0'

data_json = 'siteCode=1301000003&tab=all&timestamp=1718876469838&wordToken=2af54ea4e5bf96ad472de53877daddac&page=1&pageSize=20&qt=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&timeOption=0&sort=relevance&keyPlace=0&fileType='

data_dict = {'siteCode': '1301000003', 'tab': 'all', 'timestamp': '1718878865770',
             'wordToken': '0731c7435559f5ca77cca7a4a70e9f32', 'page': '1', 'pageSize': '20', 'qt': '学习考察',
             'timeOption': '0', 'sort': 'relevance', 'keyPlace': '0'}

json_str = '{"token":"","pn":10,"rn":10,"sdt":"2020-12-31T16:00:00.000Z","edt":"2021-12-30T16:00:00.000Z",' \
           '"wd":"%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0","inc_wd":"","exc_wd":"","fields":"title;content",' \
           '"cnum":"001;002;","sort":"{\"sysscore\":\"0\"}","ssort":"title","cl":500,"terminal":"","condition":null,' \
           '"time":null,"highlights":"title;content","statistics":null,"unionCondition":null,"accuracy":"",' \
           '"noParticiple":"0","searchRange":null}'

params = {
    'websiteid': '370900000000000',
    'q': '%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F',
    'p': '7',
    'pg': '5',
    'cateid': '19002',
    'tpl': '2885',
    'checkError': '1',
    'word': '学习考察'
}

non_proxies = {
    "http": None,
    "https": None
}

headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Host":"www.gansu.gov.cn","Referer":"https://www.gansu.gov.cn/guestweb4/s?searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%2520%25E8%2580%2583%25E5%25AF%259F%25E5%25AD%25A6%25E4%25B9%25A0&column=%25E5%2585%25A8%25E9%2583%25A8&wordPlace=1&orderBy=0&startTime=&endTime=&pageSize=10&pageNum=0&timeStamp=0&siteCode=6200000001&sonSiteCode=&checkHandle=1&strFileType=&govWorkBean=%257B%257D&sonSiteCode=&areaSearchFlag=-1&secondSearchWords=&topical=&pubName=&countKey=0&uc=0&isSonSite=false&left_right_index=0","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

fiddler_proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888"
}

# page.get(url=url, proxies=proxies)

# print(page.html)
# print(page.title)

# page.get(url, proxies=non_proxies)
# response = requests.get(url, verify=False, headers=headers)
# response = requests.get(url, proxies=non_proxies, verify=False, headers=headers)
response = requests.get(url, proxies=fiddler_proxies, verify=False, headers=headers)
# response = requests.get(url, headers=headers, proxies=non_proxies)

# 将 response.content 解码为 utf-8
print(response.content.decode('utf-8'))

# url data没有
#
# url = page.ele('x://*[@id="results"]/div[1]/div[1]/a').attr('href')
# print(page.html)
# print(url)