import math

from common.form_utils import *
from scraper.spider_mother import PageMother


# def input_date(page):
#     # 输入日期
#     begin_input = page.ele('xpath://*[@placeholder="开始日期"]')
#     end_input = page.ele('xpath://*[@placeholder="结束日期"]')
#     enter_button = page.ele('xpath://*[text()="确定"]')
#     begin_input.input('2018-01-01', by_js=True)
#     time.sleep(5)
#     end_input.input('2018-12-31', by_js=True)
#     time.sleep(5)
#     enter_button.click()


def get_data_from_dict(data_dict):
    data_list = []
    for data in data_dict['data']['middle']['listAndBox']:
        item = data['data']

        # 使用get方法简化访问，如果'item'中的对应键不存在，则尝试从嵌套的字典中获取
        url = item.get('url', item.get('list', [{}])[0].get('data', [{}])[0].get('url', ''))
        topic = item.get('title', item.get('list', [{}])[0].get('data', [{}])[0].get('title', ''))
        date = item.get('time', item.get('list', [{}])[0].get('data', [{}])[0].get('time', ''))

        # 确保格式正常
        cleaned_dict = clean_news_data({'url': url, 'topic': topic, 'date': date})

        data_list.append(cleaned_dict)

    return data_list


if __name__ == '__main__':
    page_num = math.ceil(261 / 17)
    # page_num = math.ceil(20 / 10)

    name = 'Tongling'
    url = 'https://www.tl.gov.cn/home?searchWord=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F&siteid=1678666940295417856&isall=all&isxmt='

    button_xpath = 'xpath://*[text()=">>"]'
    target_pack = 'front/search'

    city_info = PageMother(name, url, page_num, is_headless=False)

    city_info.fetch_web_by_click(button_xpath, get_data_from_dict, target_path=target_pack, is_by_listen=True)
