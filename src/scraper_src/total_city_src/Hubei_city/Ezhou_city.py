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
        'city_name': '鄂州市',
        'province_name': '湖北省',
        'province': 'Hubei',
        'base_url': 'https://www.ezhou.gov.cn/ssp/search/api/search',
        'total_news_num': 22452,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"718","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"Hm_lvt_54775391a0b0a31ca0feac1d0e57fbb0=1720963226; Hm_lpvt_54775391a0b0a31ca0feac1d0e57fbb0=1720963226; HMACCOUNT=A202F23FD4E0D795; mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; Hm_lvt_15a255313f9032ed6a445a9396730ee0=1720963248; Hm_lpvt_15a255313f9032ed6a445a9396730ee0=1720963248","Host":"www.ezhou.gov.cn","Origin":"https://www.ezhou.gov.cn","Referer":"https://www.ezhou.gov.cn/ssp/main/index.html?key=&siteId=4028488186ba901c0186ba90437d001f","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\"Windows\""}

    post_data = {'isCollapse': '', 'siteCode': '', 'zhuTiIdList': '', 'isCrdept': '', 'mainSiteId': '4028488186ba901c0186ba90437d001f', 'siteId': '4028488186ba901c0186ba90437d001f', 'depSiteId': '4028488186ba901c0186ba90437d001f', 'type': '0', 'page': '3', 'rows': '10', 'historyId': 'ff8080818fe23cde0190b16568184376', 'sourceType': 'SSP_ZHSS', 'isChange': '0', 'fullKey': 'N', 'wbServiceType': '13', 'head': '', 'fileType': '', 'feaTypeName': '', 'fileNo': '', 'pubOrg': '', 'zfgbPubOrg': '', 'themeType': '', 'searchTime': '', 'startDate': '', 'endDate': '', 'sortFiled': 'RELEVANCE', 'searchFiled': '', 'dirUseLevel': '', 'issueYear': '', 'issueMonth': '', 'allKey': '', 'fullWord': '', 'oneKey': '', 'notKey': '', 'totalIssue': '', 'chnlName': '', 'zfgbTitle': '', 'zfgbContent': '', 'bsDeptId': '', 'siteName': '鄂州市人民政府网', 'yearOfCommunique': '', 'zhuti': '', 'keyWord': '学习考察', 'orgCodeList': ''}

    page_num_name = 'page'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name)
    scraper.run()

