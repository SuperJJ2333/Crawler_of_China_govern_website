import json
from urllib.parse import unquote

from bs4 import BeautifulSoup

from scraper.scraper import Scraper


def extract_news_info(data_list, page_num, logger):
    if isinstance(data_list, dict):
        news_dict = data_list
    else:
        news_dict = json.loads(data_list)

    extracted_news_list = []

    data_dict = news_dict.get('result', {})

    for item in data_dict:
        # 解码HTML实体
        soup = BeautifulSoup(item, 'html.parser')
        try:
            # 提取标题
            title_tag = soup.find('a', title=True)
            topic = title_tag['title'] if title_tag else None

            # 提取URL
            url_tag = title_tag['href'] if title_tag else None
            url = url_tag.split('url=')[1].split('&')[0] if url_tag else None
            url = unquote(url)

            # 提取发布日期
            date_tag = soup.find('span', class_='jcse-news-date')
            date = date_tag.text.strip() if date_tag else None
            date = date.split()[-1] if date else None
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
    提取方法：JSON -- data -- data -- list -- title, createDate, url
    """

    city_info = {
        'city_name': '江苏省',
        'province_name': '江苏省',
        'province': 'Jiangsu',
        'base_url': 'https://www.js.gov.cn/jsearchfront/interfaces/cateSearch.do',

        'total_news_num': 90,
        'each_page_news_num': 19,
    }

    headers = {"Host":"www.js.gov.cn","sec-ch-ua":"\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\"","Accept":"application/json, text/javascript, */*; q=0.01","Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","sec-ch-ua-mobile":"?0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0","sec-ch-ua-platform":"\"Windows\"","Origin":"https://www.js.gov.cn","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://www.js.gov.cn/jsearchfront/search.do?websiteid=320500000000000&searchid=12&pg=&p=1&tpl=38&serviceType=&cateid=20&q=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&pq=&oq=&eq=&pos=title&sortType=0&begin=&end=","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","Cookie":"user_sid=2edc4f62b23f4321a147e43c07342cca; _city=%E5%B9%BF%E5%B7%9E%E5%B8%82; searchsign=1ef445f7044f4140bc31da766b5067a4; sid=beafd0e52c428d42793d4f4fe18e6484; __jsluid_s=18708801e5f4460bd746d43908b9d209; zh_choose_1=s; arialoadData=true; ariawapChangeViewPort=false; CUSSESSIONID=bebf6e85-6f69-4535-833d-08266d7ea203; _q=%u8003%u5BDF%u5B66%u4E60%20%u8003%u5BDF%u5B66%u4E60%3A%u5B66%u4E60%u8003%u5BDF%20%u8003%u5BDF%u5B66%u4E60%3A%u5B66%u4E60%u8003%u5BDF%3A; d7d579b9-386c-482a-b971-92cad6721901=WyIzNzc1Mzg2MTI0Il0"}

    city_data = {
        # '南京市': [328, 320100000000],
        # '无锡市': [235, 320200000000],
        # '徐州市': [48, 320300000000],
        # '常州市': [1064, 320400000000],
        # '苏州市': [615, 320500000000],
        # '南通市': [266, 320600000000],
        # '连云港市': [235, 320700000000],
        # '淮安市': [220, 320800000000],
        # '盐城市': [312, 320900000000],
        '扬州市': [472, 321000000000],
        '镇江市': [180, 321100000000],
        '泰州市': [285, 321200000000],
        '宿迁市': [153, 321300000000]
    }

    base_post_data = 'websiteid={city_code}&q=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&p=1&pg=19&cateid=40&pos=&pq=&oq=&eq=&begin=&sortType=0&end=&tpl=38'
    page_num_name = 'p'

    fiddler_proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }

    for city_name, city_code in city_data.items():
        city_info['city_name'] = city_name
        city_info['total_news_num'] = city_code[0]

        post_data = base_post_data.format(city_code=str(city_code[1]) + '000')

        scraper = Scraper(city_info, method='post', data_type='json',
                          headers=headers, extracted_method=extract_news_info, is_headless=True,
                          post_data=post_data, page_num_name=page_num_name,
                          proxies=fiddler_proxies, verify=False)
        scraper.session.post(url=city_info['base_url'], headers=headers, data=post_data, proxies=scraper.proxies, verify=False)
        scraper.total_news_num = scraper.session.json.get('total')
        scraper.total_page_num = scraper.count_page_num()
        print(f'{city_name}市共{scraper.total_news_num}条新闻，{scraper.total_page_num}页')

        scraper.run()
