import re

# 给定的字符串
input_string = "javascript:geturl('http://www.xingtai.gov.cn/ywdt/jrxt/qxdt/nqx/202304/t20230424_666523.html','','20')"

# 使用正则表达式提取URL
url_pattern = r"'([^']+)'"
match = re.search(url_pattern, input_string)

if match:
    url = match.group(1)
    print("提取的URL是: " + url)
else:
    print("未找到URL")
