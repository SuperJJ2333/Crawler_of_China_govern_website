import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('searchTotal', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('pubDate', '')
            url = item.get('url', '')
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
    请求方法：POST
    获取数据：API
    提取方法：JSON -- resultDocs -- resultDocs -- titleO, docDate, url
    """

    city_info = {
        'city_name': '赣州市',
        'province_name': '江西省',
        'province': 'Jiangxi',

        'base_url': 'https://zs.kaipuyun.cn/commonAggs',

        'total_news_num': 5382,
        'each_page_news_num': 10,
    }

    headers = {
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "Cookie": "HWWAFSESID=5d52d735252931f515; HWWAFSESTIME=1716213073175; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; firstWord=%u5B66%u4E60%u8003%u5BDF; 3607000056=5a2m5Lmg6ICD5a+fLOiAg+Wvn+WtpuS5oCzlrabkuaDogIPlr58g6ICD5a+f5a2m5Lmg; SECKEY_ABVK=TXuIX6p6HNd6ayGiHg9HgEa7Z07hqviBfiHKBm+QiX4%3D; BMAP_SECKEY=Z1ROGlRy-zdYROkyYNTEakFve6kHnQxjPQJpYWmAM0Nx5NSx29CwEyM3efTYRX4lm0bnbhJAIEebvFvVBTEzXl3X9GNr2Yo6fcFvdrdIAhetmZUK2YaveuHP-J-0Mp0bOX9Nde3ws0U9_ZpYgIcBVNuFMnba3MvcSLsYVxwlaj5YYzNb1I7JripbjOsOZMtZ; JSESSIONID=299431A9EE41FE56E69FA0587DF1F375; userSearch=siteCode-3607000056&column-%E5%85%A8%E9%83%A8&uc-0&firstWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&searchWord-%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&searchTime-20240520220114&searchUseTime-525",
  "Host": "zs.kaipuyun.cn",
  "Origin": "https://zs.kaipuyun.cn",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
  "X-Requested-With": "XMLHttpRequest",
  "sec-ch-ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\""
}

    post_data = 'searchWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%25E4%25BA%25A4%25E6%25B5%2581%25E5%25AD%25A6%25E4%25B9%25A0&siteCode=3607000056&column=%25E7%25AB%2599%25E7%25BE%25A4&wordPlace=0&orderBy=0&startTime=&endTime=&pageSize=10&pageNum=0&timeStamp=0&checkHandle=1&strFileType=&areaSearchFlag=1&secondSearchWords=&topical=&docName=&label=&countKey=0&searchBoxSettingsIndex=&manualWord=%25E5%25AD%25A6%25E4%25B9%25A0%25E8%2580%2583%25E5%25AF%259F%25E4%25BA%25A4%25E6%25B5%2581%25E5%25AD%25A6%25E4%25B9%25A0'

    page_num_name = 'pageNum'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name, page_num_start=0)
    scraper.run()