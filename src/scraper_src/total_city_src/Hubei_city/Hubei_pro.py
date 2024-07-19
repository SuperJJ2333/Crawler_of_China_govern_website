import json
from urllib.parse import urlencode

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('page', {}).get('content', {})

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('trs_time', '')
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


def create_search_url(base_url, parameters):
    """
    构建搜索URL。

    :param base_url: 不包含查询参数的基础URL。
    :param parameters: 一个包含所有查询参数的字典。
    :return: 完整的URL。
    """
    # 将查询参数编码为URL格式
    query_string = urlencode(parameters, doseq=True)

    # 组合基础URL和查询字符串
    return f"{base_url}?{query_string}"


if __name__ == '__main__':
    """
    请求方法：GET
    获取数据：API
    提取方法：JSON -- data -- data -- title, createDate, url
    """

    city_info = {
        'city_name': '武汉市',
        'province_name': '湖北省',
        'province': 'Hubei',
        'base_url': 'https://www.anqing.gov.cn/searchFront/search/doSearch?pageSize=20&contentLength=80&isHighlight=1&columnId=&keywords=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&subkeywords=&typeCode=all&isAllSite=true&platformCode=&siteId=&fromCode=title&fuzzySearch=true&datecode=&orderType=0&doColloquialConvert=true&minScore=&fileNums=&publishDepartment=&pageIndex={page_num}',

        'total_news_num': 5000,
        'each_page_news_num': 10,
    }

    parameters = {
        "position": "",
        "timeOrder": "",
        "code": "d877ec2a23e741ddb3018f013c6786c5",
        "orderBy": "all",
        "pageSize": 10,
        "type": "",
        "time": "",
        "chnldesc": "",
        "aggrFieldName": "CHNLDESC",
        "sortByFocus": "true",
        "siteId": 54,
        "name": "武汉市",  # 可以改为 "荆门市" 或其他城市
        "sitename": "",
        "SITETYPE": "武汉市",  # 同上
        "searchWord": "学习考察 考察学习"  # 或其他搜索词
    }

    # 基础URL
    base_url = "https://www.hubei.gov.cn/igs/front/search.jhtml"

    city_names = ['武汉市', '黄石市', '十堰市', '宜昌市', '襄阳市', '鄂州市', '荆门市', '孝感市', '荆州市', '黄冈市',
                  '咸宁市', '随州市']

    headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br, zstd",
               "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", "Connection": "keep-alive",
               "Cookie": "JSESSIONID=0A3221FB7D56C40575D64B3754952426; 97badf5c34b18827e4=24803fbc5fd4622644cb84cb8ce5f78f; _trs_uv=ly3zosn3_3027_g0id; _trs_ua_s_1=ly3zosn3_3027_1emu; Hm_lvt_5544783ae3e1427d6972d9e77268f25d=1719899388; Hm_lpvt_5544783ae3e1427d6972d9e77268f25d=1719899388; token=139b4659-aabd-4239-a686-47da791f577e; uuid=139b4659-aabd-4239-a686-47da791f577e; 924omrTVcFchP=0qgnIAdfC_FX6Ur13w4K5QJxvABMHIM3CjAXVtjBnwL6cPR.WF3_ex5g1.kXJCXrU3q2JRGysjstmx3wQ_deUE9mDRw3a__Q9alYpLIHwFTngfSpKqxNanN0aSjEy1dasJk.O8T4ftdGZy6uZMvnN5R7ZrmJ0zygq4SarQKfyXWl1whRYU2DNC5OyvzWU89EbrXSwqvMr0iq7KgSdSUWGrAJoV9sgWGY2_ktZ49yNclD_ZkWgs.603qBfqxIenpUKVPuEKIeIjxueQbzYu0RplQ8DiYWLMEqO9qpSWp3MYrnGyWPdE_o90Sl8fSWJelJmfvZO2OzYNGwekh9HoQEVuToxuFXqiPh0Vot_7U9.6Na",
               "Host": "www.hubei.gov.cn", "Referer": "https://www.hubei.gov.cn/site/hb/", "Sec-Fetch-Dest": "empty",
               "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
               "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"",
               "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\""}

    for city_name in city_names:
        city_info['city_name'] = city_name
        city_info['base_url'] = create_search_url(base_url, parameters) + '&pageNumber={page_num}'

        parameters['name'] = city_name
        parameters['SITETYPE'] = city_name

        scraper = Scraper(city_info, method='get', data_type='json',
                          headers=headers, extracted_method=extract_news_info, is_headless=False)

        scraper.run()
