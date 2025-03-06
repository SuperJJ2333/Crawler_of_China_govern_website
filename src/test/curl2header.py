import re


def curl_to_requests_headers(curl_command):
    # 移除可能的转义字符并标准化命令
    curl_command = curl_command.replace('^', '').replace('\\', '')

    # 定义一个正则表达式来提取 cURL 命令中的 -H 请求头
    headers = {}

    # 匹配 -H 后面的请求头
    header_pattern = r'-H\s+"([^:]+):\s([^"]+)"'
    matches = re.findall(header_pattern, curl_command)

    for header_name, header_value in matches:
        headers[header_name] = header_value

    return headers


# 示例 cURL 命令
curl_command = """
curl ^"https://www.haodf.com/bingcheng/8906882795.html^" ^
  -H ^"accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7^" ^
  -H ^"accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6^" ^
  -H ^"priority: u=0, i^" ^
  -H ^"sec-ch-ua: ^\^"Not(A:Brand^\^";v=^\^"99^\^", ^\^"Microsoft Edge^\^";v=^\^"133^\^", ^\^"Chromium^\^";v=^\^"133^\^"^" ^
  -H ^"sec-ch-ua-mobile: ?0^" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  -H ^"sec-fetch-dest: document^" ^
  -H ^"sec-fetch-mode: navigate^" ^
  -H ^"sec-fetch-site: none^" ^
  -H ^"sec-fetch-user: ?1^" ^
  -H ^"upgrade-insecure-requests: 1^" ^
  -H ^"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0^"
"""
# 提取请求头
headers = curl_to_requests_headers(curl_command)

# 输出结果
print(headers)
