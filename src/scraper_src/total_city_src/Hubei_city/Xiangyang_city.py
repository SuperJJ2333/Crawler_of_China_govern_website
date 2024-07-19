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
        'city_name': '襄阳市',
        'province_name': '湖北省',
        'province': 'Hubei',
        'base_url': 'http://www.xiangyang.gov.cn/ssp/search/api/search',
        'total_news_num': 3517,
        'each_page_news_num': 10,
    }

    headers = {"Accept":"application/json, text/javascript, */*; q=0.01","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Content-Length":"621","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"mozi-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false}; Hm_lvt_b29a0fc8cf9f88dc79677b5ad985798b=1720962598; Hm_lpvt_b29a0fc8cf9f88dc79677b5ad985798b=1720962598; HMACCOUNT=A202F23FD4E0D795; SESSION=YWNjZmQ4YTQtMDk0MC00M2ZjLTlmYTQtNDQzNWQ2ZWIxZmNl","Host":"www.xiangyang.gov.cn","Origin":"http://www.xiangyang.gov.cn","Referer":"http://www.xiangyang.gov.cn/ssp/main/search.html?keyWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&siteId=ff8080818423348c018436624fd60004&isMain=","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","X-Requested-With":"XMLHttpRequest"}

    post_data = {'isCollapse': 'N', 'siteType': '1', 'mainSiteId': 'ff8080818423348c018436624fd60004', 'siteId': 'ff8080818423348c018436624fd60004', 'type': '1', 'page': '3', 'rows': '10', 'historyId': 'ff8080818ff1782d0190b15a9b7b790b', 'sourceType': 'SSP_ZHSS', 'isChange': '0', 'fullKey': 'N', 'wbServiceType': '13', 'fileType': '', 'pubOrg': '', 'themeType': '', 'searchTime': '', 'startDate': '', 'endDate': '', 'sortFiled': 'RELEVANCE', 'searchFiled': '', 'dirUseLevel': '', 'issueYear': '', 'issueMonth': '', 'allKey': '', 'fullWord': '', 'oneKey': '', 'notKey': '', 'totalIssue': '', 'chnlName': '', 'zfgbTitle': '', 'zfgbContent': '', 'zfgbPubOrg': '', 'zwgkPubDate': '', 'zwgkDoctitle': '', 'zwgkDoccontent': '', 'zhPubOrg': '1', 'keyWord': '学习考察考察学习', 'areaCode': '420600000000', 'areaGrade': '3'}

    page_num_name = 'page'

    scraper = Scraper(city_info, method='post', data_type='json',
                      headers=headers, extracted_method=extract_news_info, is_headless=True,
                      post_data=post_data, page_num_name=page_num_name)
    scraper.run()

