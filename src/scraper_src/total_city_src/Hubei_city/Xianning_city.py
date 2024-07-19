import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('datas', {})

    for item in data_dict:

        try:
            topic = item.get('doctitle', '')
            date = item.get('docreltime', '')
            url = item.get('docpuburl', '')
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
    请求方法：GET
    获取数据：API
    提取方法：JSON -- page -- content -- title, trs_time, url
    """

    city_info = {
        'city_name': '咸宁市',
        'province_name': '湖北省',
        'province': 'Hubei',
        'base_url': 'http://www.xianning.gov.cn/ssp/search/api/search',

        'total_news_num': 1782,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"656","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"_trs_uv=lxfmjvzr_248_3glc; wzws_sessionid=gTVmNDU5MYAyMDAxOjI1MDozMDA3OjgwMDI6OTFhMDpiODUwOmQxNmM6MzM4YYIyMTNjYmSgZpPs7Q==; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; _trs_ua_s_1=lylpe1af_248_6b0g","Host":"www.xianning.gov.cn","Origin":"http://www.xianning.gov.cn","Referer":"http://www.xianning.gov.cn/ssp/main/index.html?siteId=8ada93e184a906cb0184bbdb3b3d000a","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest"}

    post_data = {'isCollapse': '', 'siteCode': '', 'zhuTiIdList': '', 'isCrdept': '', 'mainSiteId': '8ada93e184a906cb0184bbdb3b3d000a', 'siteId': '8ada93e184a906cb0184bbdb3b3d000a', 'depSiteId': '8ada93e184a906cb0184bbdb3b3d000a', 'type': '0', 'page': '3', 'rows': '10', 'historyId': '8ada93e18b473e390190b1d5d89c5b96', 'sourceType': 'SSP_DOCUMENT', 'isChange': '0', 'fullKey': 'N', 'wbServiceType': '13', 'fileType': '', 'feaTypeName': '', 'fileNo': '', 'pubOrg': '', 'zfgbPubOrg': '', 'themeType': '', 'searchTime': '', 'startDate': '', 'endDate': '', 'sortFiled': 'RELEVANCE', 'searchFiled': '', 'dirUseLevel': '', 'issueYear': '', 'issueMonth': '', 'allKey': '', 'fullWord': '', 'oneKey': '', 'notKey': '', 'totalIssue': '', 'chnlName': '', 'zfgbTitle': '', 'zfgbContent': '', 'bsDeptId': '', 'siteName': '', 'keyWord': '学习考察 考察学习', 'orgCodeList': ''}

    page_num_name = 'page'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name)
    scraper.run()