import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('page', {}).get('records', {})

    for item in data_dict:
        # item = item.get('data', {})
        try:
            topic = item.get('title', '')
            date = item.get('createDate', '')
            url = item.get('url', '')

            if not url.startswith('http'):
                url = 'https:' + url

        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        news_info = {
            'topic': topic,
            'date': date,
            'url': url,
        }
        extracted_news_list.append(news_info)

    return extracted_news_list


if __name__ == '__main__':
    """
    请求方法：POST -- verify
    获取数据：API -- by_json
    提取方法：JSON -- data -- middle -- listAndBox -- titleO, docDate, url
    """

    city_info = {
        'city_code': 315,
        'city_name': '红河哈尼族彝族自治州',
        'province_name': '云南省',
        'province': '云南省',

        'base_url': 'https://www.hh.gov.cn/aop_component//webber/search/search/search/queryPage',

        'total_news_num': 1265,
        # 'total_news_num': 12,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Authorization":"preview","Connection":"keep-alive","Content-Length":"509","Content-Type":"application/json;charset=UTF-8","Cookie":"JSESSIONID=c0e98a0dd40f8fbe241bc0386904","Host":"www.hh.gov.cn","Origin":"https://www.hh.gov.cn","Referer":"https://www.hh.gov.cn/ssjgy.htm?query=eyJhbGlhc05hbWUiOiJhcnRpY2xlX2RhdGEsb3Blbl9kYXRhIiwic2VhcmNoVHlwZSI6InN0cmluZyIsIm9yZGVyVHlwZSI6InNjb3JlIiwic2VhcmNoRGF0ZVR5cGUiOiJjdXN0b20iLCJiZWdpbkRhdGUiOiIiLCJlbmREYXRlIjoiIiwiYXVkaXRpbmciOlsiMSJdLCJvd25lciI6IjE5ODA0NDU5NzQiLCJjb2x1bW5JZCI6IiIsImtleVdvcmQiOiLlrabkuaDogIPlr58iLCJzZWFyY2hLZXlXb3JkVGVtcCI6IuWtpuS5oOiAg+WvnyIsInBhZ2UiOnsiY3VycmVudCI6MCwic2l6ZSI6MTAsInRvdGFsIjowLCJ0b3RhbFBhZ2UiOjAsImdvVG9DdXJyZW50IjoxLCJpbmRleHMiOlsxLDIsMyw0LDUsNiw3LDgsOSwxMF19LCJmaWVsZCI6W10sImZpZWxkVGVtcCI6e30sImZpbHRlciI6e30sImZpbHRlclRlcm0iOnt9LCJhZ2dGaWVsZHMiOnsiY29sdW1uIjoiIiwiY29sdW1uTmFtZSI6IiJ9fQ==&other=eyJncm91cFNlbGVjdCI6IiIsImdyb3VwIjp7IuWIhuexuyI6W3siZ3JvdXBJZCI6IjExIiwibGFiZWwiOiLmlL/nrZYiLCJpc0Nob2ljZSI6ZmFsc2V9LHsiZ3JvdXBJZCI6IjExIiwibGFiZWwiOiLop6Por7siLCJpc0Nob2ljZSI6ZmFsc2V9LHsiZ3JvdXBJZCI6IjExIiwibGFiZWwiOiLlhazlvIAiLCJpc0Nob2ljZSI6ZmFsc2V9LHsiZ3JvdXBJZCI6IjExIiwibGFiZWwiOiLkupLliqgiLCJpc0Nob2ljZSI6ZmFsc2V9XX0sImRhdGVUeXBlIjoibm9uZSIsInprTmFtZSI6IuWxleW8gCIsInprSGVpZ2h0IjoiMTQ1cHgifQ==","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0","X-Requested-With":"XMLHttpRequest","owner":"1581564523","sec-ch-ua":"\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"aliasName":"article_data,open_data","searchType":"string","orderType":"score","searchDateType":"custom","beginDate":"","endDate":"","auditing":["1"],"owner":"1980445974","columnId":"","keyWord":"","searchKeyWordTemp":"学习考察","page":{"current":1,"size":10,"total":1265,"totalPage":127,"goToCurrent":2,"indexs":[1,2,3,4,5,6,7,8,9,10]},"field":[{"fieldName":"title","fieldValue":"学习考察"}],"fieldTemp":{"title":"学习考察"},"filter":{},"filterTerm":{},"aggFields":{"column":"","columnName":""}}'

    post_data = json.loads(post_data)

    page_num_name = ['page.goToCurrent', 'page.current']

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, proxies=fiddler_proxies, verify=False,
                      is_post_by_json=True, page_num_start=0)
    scraper.run()