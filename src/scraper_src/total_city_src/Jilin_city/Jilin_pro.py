import json
import urllib.parse

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('data', {}).get('list', [])

    for item in data_dict:

        try:
            topic = item.get('title', '')
            date = item.get('pubtime', '')
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

def dict_to_json(encoded_params):
    # URL 解码
    decoded_params = urllib.parse.unquote(encoded_params)

    # 将 JSON 字符串转换为字典
    params_dict = json.loads(decoded_params)

    # 重新编码为 URL 编码的字符串
    encoded_back = urllib.parse.urlencode(params_dict)

    # 构建最终的字符串形式
    final_params = f"params={encoded_back}"

    return final_params


if __name__ == '__main__':
    """
    请求方法：POST
    获取数据：API
    提取方法：JSON -- data -- data -- list -- title, createDate, url
    """

    city_info = {
        'city_name': '吉林市',
        'province_name': '吉林省',
        'province': 'Jilin',
        'base_url': 'https://intellsearch.jl.gov.cn/api/data/list',

        'total_news_num': 90,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"_trs_uv=ly41tlqg_79_f0tk; wzws_sessionid=gTVmNDU5MaBmg6MAgjA3NjRjNYAyMjEuNC4zMi4yNA==; sajssdk_2015_cross_new_user=1; trs_search_uv=4FC1B33D9B3B4043BA1AECC2D51B930F432; _trs_ua_s_1=ly41ttcy_79_aevk; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221907234ba7f80-0599e184cf9bfd-4c657b58-1327104-1907234ba80489%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22http%3A%2F%2Fwww.jlcity.gov.cn%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkwNzIzNGJhN2Y4MC0wNTk5ZTE4NGNmOWJmZC00YzY1N2I1OC0xMzI3MTA0LTE5MDcyMzRiYTgwNDg5In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221907234ba7f80-0599e184cf9bfd-4c657b58-1327104-1907234ba80489%22%7D","Host":"intellsearch.jl.gov.cn","Origin":"https://intellsearch.jl.gov.cn","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    city_data = {
                 # '吉林市': [354, 'params=%7B%22word%22%3A%22%22%2C%22page%22%3A1%2C%22size%22%3A10%2C%22stype%22%3A%2210%22%2C%22area%22%3A%22220200%22%2C%22atype%22%3A%223%22%2C%22dept%22%3A%22%22%2C%22ttype%22%3A%220%22%2C%22start%22%3A%22%22%2C%22end%22%3A%22%22%2C%22itype%22%3A%22%22%2C%22mattType%22%3A%220%22%2C%22serverType%22%3A%220%22%2C%22sort%22%3A%220%22%2C%22aword%22%3A%22%22%2C%22hword%22%3A%22%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%22%2C%22nword%22%3A%22%22%2C%22dtword%22%3A%22%22%2C%22scope%22%3A%223%22%2C%22selecttp%22%3A%2210%22%2C%22filetype%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22fileyear%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22stypeChild%22%3A%220%22%2C%22hs%22%3A%220%22%2C%22flag%22%3A%22senior%22%2C%22satisfiedId%22%3A%2256EE83FF3164426FA885F758124C57FA564%22%7D'],
                 #
                 # '长春市': [453, 'params=%7B%22word%22%3A%22%22%2C%22page%22%3A1%2C%22size%22%3A10%2C%22stype%22%3A%2210%22%2C%22area%22%3A%22220100%22%2C%22atype%22%3A%223%22%2C%22dept%22%3A%22%22%2C%22ttype%22%3A%220%22%2C%22start%22%3A%22%22%2C%22end%22%3A%22%22%2C%22itype%22%3A%22%22%2C%22mattType%22%3A%220%22%2C%22serverType%22%3A%220%22%2C%22sort%22%3A%220%22%2C%22aword%22%3A%22%22%2C%22hword%22%3A%22%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%22%2C%22nword%22%3A%22%22%2C%22dtword%22%3A%22%22%2C%22scope%22%3A%223%22%2C%22selecttp%22%3A%2210%22%2C%22filetype%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22fileyear%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22stypeChild%22%3A%220%22%2C%22hs%22%3A%220%22%2C%22flag%22%3A%22senior%22%2C%22satisfiedId%22%3A%22D3E593DFD5824384B28FC42BEDB22550362%22%7D'],

                 '四平市': [444, 'params=%7B%22word%22%3A%22%22%2C%22page%22%3A1%2C%22size%22%3A10%2C%22stype%22%3A%2210%22%2C%22area%22%3A%22220300%22%2C%22atype%22%3A%223%22%2C%22dept%22%3A%22%22%2C%22ttype%22%3A%220%22%2C%22start%22%3A%22%22%2C%22end%22%3A%22%22%2C%22itype%22%3A%22%22%2C%22mattType%22%3A%220%22%2C%22serverType%22%3A%220%22%2C%22sort%22%3A%220%22%2C%22aword%22%3A%22%22%2C%22hword%22%3A%22%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%22%2C%22nword%22%3A%22%22%2C%22dtword%22%3A%22%22%2C%22scope%22%3A%223%22%2C%22selecttp%22%3A%2210%22%2C%22filetype%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22fileyear%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22stypeChild%22%3A%220%22%2C%22hs%22%3A%220%22%2C%22flag%22%3A%22senior%22%2C%22satisfiedId%22%3A%22938D7EF9F6CE4BBC821EB71A83E29046735%22%7D'],

                 '辽源市': [286, 'params=%7B%22word%22%3A%22%22%2C%22page%22%3A1%2C%22size%22%3A10%2C%22stype%22%3A%2210%22%2C%22area%22%3A%22220400%22%2C%22atype%22%3A%223%22%2C%22dept%22%3A%22%22%2C%22ttype%22%3A%220%22%2C%22start%22%3A%22%22%2C%22end%22%3A%22%22%2C%22itype%22%3A%22%22%2C%22mattType%22%3A%220%22%2C%22serverType%22%3A%220%22%2C%22sort%22%3A%220%22%2C%22aword%22%3A%22%22%2C%22hword%22%3A%22%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%22%2C%22nword%22%3A%22%22%2C%22dtword%22%3A%22%22%2C%22scope%22%3A%223%22%2C%22selecttp%22%3A%2210%22%2C%22filetype%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22fileyear%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22stypeChild%22%3A%220%22%2C%22hs%22%3A%220%22%2C%22flag%22%3A%22senior%22%2C%22satisfiedId%22%3A%220740E1DEC0234BB597B6283727105B03295%22%7D'],

                 '通化市': [202, 'params=%7B%22word%22%3A%22%22%2C%22page%22%3A1%2C%22size%22%3A10%2C%22stype%22%3A%2210%22%2C%22area%22%3A%22220500%22%2C%22atype%22%3A%223%22%2C%22dept%22%3A%22%22%2C%22ttype%22%3A%220%22%2C%22start%22%3A%22%22%2C%22end%22%3A%22%22%2C%22itype%22%3A%22%22%2C%22mattType%22%3A%220%22%2C%22serverType%22%3A%220%22%2C%22sort%22%3A%220%22%2C%22aword%22%3A%22%22%2C%22hword%22%3A%22%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%22%2C%22nword%22%3A%22%22%2C%22dtword%22%3A%22%22%2C%22scope%22%3A%223%22%2C%22selecttp%22%3A%2210%22%2C%22filetype%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22fileyear%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22stypeChild%22%3A%220%22%2C%22hs%22%3A%220%22%2C%22flag%22%3A%22senior%22%2C%22satisfiedId%22%3A%22FE2E3B1430544B44A5E4609A64B32398555%22%7D'],

                 '白山市': [220, 'params=%7B%22word%22%3A%22%22%2C%22page%22%3A1%2C%22size%22%3A10%2C%22stype%22%3A%2210%22%2C%22area%22%3A%22220600%22%2C%22atype%22%3A%223%22%2C%22dept%22%3A%22%22%2C%22ttype%22%3A%220%22%2C%22start%22%3A%22%22%2C%22end%22%3A%22%22%2C%22itype%22%3A%22%22%2C%22mattType%22%3A%220%22%2C%22serverType%22%3A%220%22%2C%22sort%22%3A%220%22%2C%22aword%22%3A%22%22%2C%22hword%22%3A%22%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%22%2C%22nword%22%3A%22%22%2C%22dtword%22%3A%22%22%2C%22scope%22%3A%223%22%2C%22selecttp%22%3A%2210%22%2C%22filetype%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22fileyear%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22stypeChild%22%3A%220%22%2C%22hs%22%3A%220%22%2C%22flag%22%3A%22senior%22%2C%22satisfiedId%22%3A%22616248F728BC42F281C8FD0BFCB6A276182%22%7D'],

                 '松原市': [275, 'params=%7B%22word%22%3A%22%22%2C%22page%22%3A1%2C%22size%22%3A10%2C%22stype%22%3A%2210%22%2C%22area%22%3A%22220700%22%2C%22atype%22%3A%223%22%2C%22dept%22%3A%22%22%2C%22ttype%22%3A%220%22%2C%22start%22%3A%22%22%2C%22end%22%3A%22%22%2C%22itype%22%3A%22%22%2C%22mattType%22%3A%220%22%2C%22serverType%22%3A%220%22%2C%22sort%22%3A%220%22%2C%22aword%22%3A%22%22%2C%22hword%22%3A%22%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%22%2C%22nword%22%3A%22%22%2C%22dtword%22%3A%22%22%2C%22scope%22%3A%223%22%2C%22selecttp%22%3A%2210%22%2C%22filetype%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22fileyear%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22stypeChild%22%3A%220%22%2C%22hs%22%3A%220%22%2C%22flag%22%3A%22senior%22%2C%22satisfiedId%22%3A%22A9BE1BEDAE8E49B78D23FAF4C123617D319%22%7D'],

                 '白城市': [327, 'params=%7B%22word%22%3A%22%22%2C%22page%22%3A1%2C%22size%22%3A10%2C%22stype%22%3A%2210%22%2C%22area%22%3A%22220800%22%2C%22atype%22%3A%223%22%2C%22dept%22%3A%22%22%2C%22ttype%22%3A%220%22%2C%22start%22%3A%22%22%2C%22end%22%3A%22%22%2C%22itype%22%3A%22%22%2C%22mattType%22%3A%220%22%2C%22serverType%22%3A%220%22%2C%22sort%22%3A%220%22%2C%22aword%22%3A%22%22%2C%22hword%22%3A%22%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F+%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0%22%2C%22nword%22%3A%22%22%2C%22dtword%22%3A%22%22%2C%22scope%22%3A%223%22%2C%22selecttp%22%3A%2210%22%2C%22filetype%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22fileyear%22%3A%22%E5%85%A8%E9%83%A8%22%2C%22stypeChild%22%3A%220%22%2C%22hs%22%3A%220%22%2C%22flag%22%3A%22senior%22%2C%22satisfiedId%22%3A%22F63FEC37FD894513B66F35B506C93146279%22%7D'],

                 }

    page_num_name = 'page'

    for city_name, city_code in city_data.items():
        city_info['city_name'] = city_name
        city_info['total_news_num'] = city_code[0]

        post_data = city_code[1]

        scraper = Scraper(city_info, method='post', data_type='json',
                          headers=headers, extracted_method=extract_news_info, is_headless=True,
                          post_data=post_data, page_num_name=page_num_name)
        scraper.run()

