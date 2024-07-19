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
    请求方法：POST
    获取数据：API
    提取方法：JSON -- data -- data -- title, createDate, url
    """

    city_info = {
        'city_name': '随州市',
        'province_name': '湖北省',
        'province': 'Hubei',
        'base_url': 'http://www.suizhou.gov.cn/ssp/search/api/search?time=1720979009651',
        'total_news_num': 1152,
        'each_page_news_num': 20,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"720","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"Hm_lvt_56981cb9c184f1ee96fd95b1d733b3c9=1720978953; Hm_lpvt_56981cb9c184f1ee96fd95b1d733b3c9=1720978953; HMACCOUNT=A202F23FD4E0D795; _trs_uv=lylufmq9_3347_b6oe; suiZhou_cookie=3e14c6fb-81b3-4353-9893-b8c50ddc0e94; SESSION=YWY2NThjYjgtNmVhYi00MWIzLWJmYTUtYTA0YzUyNGE1ZDA0; _trs_ua_s_1=lylw5smg_3347_h59f","Host":"www.suizhou.gov.cn","Origin":"http://www.suizhou.gov.cn","Referer":"http://www.suizhou.gov.cn/ssp/main/index.html?siteId=ff8080818bd0e0db018bd1839c460001","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest"}

    post_data = {'isCollapse': '', 'siteType': '1', 'typeQueryJsonToMap': '', 'pubOrgType': '', 'jiGuanList': '', 'siteCode': '', 'zhuTiIdList': '', 'isCrdept': '', 'mainSiteId': 'ff8080818bd0e0db018bd1839c460001', 'siteId': 'ff8080818bd0e0db018bd1839c460001', 'depSiteId': 'ff8080818bd0e0db018bd1839c460001', 'type': '2', 'page': '3', 'rows': '20', 'historyId': 'ff8080818e0daf150190b2563892543e', 'sourceType': 'SSP_ZHSS', 'isChange': '0', 'fullKey': 'N', 'wbServiceType': '13', 'fileType': '', 'feaTypeName': '', 'fileNo': '', 'pubOrg': '', 'zfgbPubOrg': '', 'themeType': '', 'searchTime': '', 'startDate': '', 'endDate': '', 'sortFiled': 'RELEVANCE', 'searchFiled': '', 'dirUseLevel': '', 'issueYear': '', 'publishYear': '', 'issueMonth': '', 'allKey': '', 'fullWord': '', 'oneKey': '', 'notKey': '', 'totalIssue': '', 'chnlName': '', 'zfgbTitle': '', 'zfgbContent': '', 'bsDeptId': '', 'siteName': '', 'keyWord': '学习考察 考察学习', 'isProvince': '1'}

    page_num_name = 'page'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name)
    scraper.run()

