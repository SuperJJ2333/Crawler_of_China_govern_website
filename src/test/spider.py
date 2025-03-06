import requests

url = "https://www.haodf.com/bingcheng/8875848706.html"
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                     '*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,'
                                                                                            'en-GB;q=0.7,'
                                                                                            'en-US;q=0.6',
           'priority': 'u=0, i', 'sec-ch-ua-mobile': '?0', 'sec-fetch-dest': 'document', 'sec-fetch-mode':
               'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'}


response = requests.get(url, headers=headers, allow_redirects=False)

print(response.text)

