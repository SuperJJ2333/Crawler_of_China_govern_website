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

        try:
            topic = item.get('title', '')
            date = item.get('createDate', '')
            url = item.get('url', '')
        except Exception as e:
            logger.error(f'{page_num}页 - 数据解析出错：{e}')
            continue

        if not url.startswith('http') and not url.startswith('https'):
            url = 'https:' + url

        news_info = {
            'topic': topic,
            'date': date,
            'url': url,
        }
        extracted_news_list.append(news_info)

    return extracted_news_list


if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：API
    提取方法：JSON -- resultDocs -- resultDocs -- titleO, docDate, url
    """

    city_info = {
        'city_name': '天水市',
        'province_name': '甘肃省',
        'province': 'Gansu',
        'base_url': 'https://www.tianshui.gov.cn/aop_component//webber/search/search/search/queryPage',

        'total_news_num': 1151,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Authorization":"tourist","Connection":"keep-alive","Content-Length":"643","Content-Type":"application/json;charset=UTF-8","Cookie":"coverlanguage_bb=0; JSESSIONID=5BECD2D814BACEB5026F57806A992506; appsearch_sessionid=20255A18B966FE7A7B02A81C1B58AA7D","Host":"www.tianshui.gov.cn","Origin":"https://www.tianshui.gov.cn","Referer":"https://www.tianshui.gov.cn/views/search/modules/resultpc/soso.html?query=eyJrZXlXb3JkIjoi5a2m5Lmg6ICD5a+fIOiAg+Wvn+WtpuS5oCIsIm93bmVyIjoiMTkxMjEyNjg3NiIsInRva2VuIjoidG91cmlzdCIsInVybFByZWZpeCI6Ii9hb3BfY29tcG9uZW50LyIsImxhbmciOiJpMThuX3poX0NOIn0=","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","owner":"1912126876","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = '{"aliasName":"article_data,open_data,mailbox_data,article_file","keyWord":"学习考察 考察学习","lastkeyWord":"学习考察 交流学习","searchKeyWord":false,"orderType":"score","searchType":"text","searchScope":"3","searchOperator":0,"searchDateType":"","searchDateName":"time.any_time","beginDate":"","endDate":"2024-07-13","showId":"c2ee13065aae85d7a998b8a3cd645961","auditing":["1"],"owner":"1912126876","token":"tourist","urlPrefix":"/aop_component/","page":{"current":2,"size":10,"pageSizes":[2,5,10,20,50,100],"total":1007,"totalPage":101,"indexs":[1,2,3,4,5,6,7,8,9,10]},"advance":false,"advanceKeyWord":"","lang":"i18n_zh_CN"}'

    post_data = json.loads(post_data)

    page_num_name = 'page.current'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, is_post_by_json=True,
                      thread_num=1)
    scraper.run()