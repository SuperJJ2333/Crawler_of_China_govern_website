import json

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('data', {}).get('info', {})

    for item in data_dict:
        item = item.get('_source')
        try:
            topic = item.get('title', '')
            date = item.get('inputtime', '')
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
    请求方法：GET
    获取数据：API
    提取方法：JSON -- data -- datas -- title, pubDate, url
    """

    city_info = {
        'city_code': 321,
        'city_name': '迪庆藏族自治州',
        'province_name': '云南省',
        'province': '云南省',

        'base_url': 'http://seacher.diqing.gov.cn/subsiteIndex/es/content/search?pageSize=20&subsiteId=&keyWord=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&start={page_num}',
        'total_news_num': 280,
        'each_page_news_num': 20,
    }

    content_xpath = {'frames': 'x://div[4]/div[2]/div[1]/dl/dd',
                     'title': 'x://div[@class="text"]/div[1]/a[2]',
                     'date': ['xpath://div[@class="text"]/div[3]/span[1]'],
                     # 'url': 'x://a'
                     }

    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Connection":"keep-alive","Cookie":"AYKJUSER=e932d0be-68f1-4381-bad1-4e4f3f21166f; Qs_lvt_550634=1730545309%2C1730708360; Qs_pv_550634=43344756243956824%2C4123430223730263000%2C2497920845392590000%2C1370213973319224000%2C3104010467959942700","Host":"seacher.diqing.gov.cn","Referer":"http://seacher.diqing.gov.cn/subsiteIndex/es/content/search?pageSize=20&subsiteId=&keyWord=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&start=2","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}

    fiddler_proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    scraper = Scraper(city_info, method='get', data_type='html',
                      content_xpath=content_xpath, headers=headers, is_headless=True,
                      proxies=fiddler_proxies, verify=False)
    scraper.run()