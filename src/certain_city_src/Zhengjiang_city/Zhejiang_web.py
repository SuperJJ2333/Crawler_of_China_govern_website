import logging
import re
from DrissionPage import ChromiumPage, ChromiumOptions
import pandas as pd

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ZhengJiangSpider:
    def __init__(self):
        self.name = ''
        self.base_url = 'https://search.zj.gov.cn/jrobotfront/search.do'
        self.search_params = {
            'searchid': '',
            'pg': '',
            'tpl': '2296',
            'cateid': '370',
            'fbjg': '',
            'word': '学习考察',
            'temporaryQ': '',
            'synonyms': '',
            'checkError': '1',
            'isContains': '1',
            'q': '学习考察',
            'jgq': '',
            'eq': '',
            'timetype': '5',
            '_cus_pq_ja_type': '',
            'pos': '',
            'sortType': '1'
        }

        # 网站编号与代码
        self.website_id_list = [
            {'330200000000000': {'begin': '20150101', 'end': '20151231'}},

            {'330100000000000': {'begin': '20160101', 'end': '20161231'}},

            {'331000000000000': {'begin': '20170101', 'end': '20171231'}},
            {'330900000000000': {'begin': '20170101', 'end': '20171231'}},
            {'330600000000000': {'begin': '20170101', 'end': '20171231'}},
            {'330500000000000': {'begin': '20170101', 'end': '20171231'}},

            {'331100000000000': {'begin': '20180101', 'end': '20181231'}},
            {'330800000000000': {'begin': '20180101', 'end': '20181231'}},
            {'330700000000000': {'begin': '20180101', 'end': '20181231'}},
            {'330300000000000': {'begin': '20180101', 'end': '20181231'}},

            {'330400000000000': {'begin': '20190101', 'end': '20191231'}},
        ]

        self.name_list = ['Ningbo', 'Hangzhou', 'Taishan', 'Zhoushan', 'Zhaoxin',
                          'Huzhou', 'Lishui', 'Quzhou', 'Jinhua', 'Wenzhou',
                          'Jiaxin']
        self.url = ''

        # 关键词列表
        self.keywords = ["学习考察", "考察学习"]

        # 创建一个浏览器页面对象，这里使用的是默认的配置
        co = ChromiumOptions().headless()
        self.page = ChromiumPage(co)
        # self.page = ChromiumPage()

    def run(self):
        # 循环遍历 website_id_list
        for idx, site_info in enumerate(self.website_id_list):
            for website_id, date_range in site_info.items():
                # 生成基础URL
                base_url_with_params = f"{self.base_url}?websiteid={website_id}&{'&'.join([f'{key}={value}' for key, value in self.search_params.items()])}&begin={date_range['begin']}&end={date_range['end']}"
                self.name = self.name_list[idx]
                self.get_news(self.page, base_url_with_params)  # 传递完整的基础URL

    def get_news(self, page, url):
        page.get(url)

        total_page = page.ele('.totalPage').text.strip()
        total_page_number = re.search(r'\d+', total_page).group()
        logging.info(f"{self.name}--总页数为：{total_page_number}页")

        tab = page.new_tab()
        unique_news = []
        for page_num in range(1, int(total_page_number) + 1):
            # 更新URL来包含当前页码
            current_url = f"{url}&p={page_num}"
            # 访问"学习考察"的数据资源页
            page.get(current_url)
            logging.info(f"当前的页数：{page_num} - URL：{current_url}")
            news_data = self.fetch_news_data(page)
            visited = set()

            for news in news_data:
                key = (news['date'], news['topic'])
                if key not in visited:
                    texts = self.fetch_page_content(tab, news['url'])
                    # 判断标题与正文中是否含有关键词
                    if texts and \
                            (self.contains_keywords(news['topic'], self.keywords) or any(self.contains_keywords(text, self.keywords) for text in texts)):
                        logging.info(f"{news['topic']}--获取新闻内容为: {texts[0][:100]}")
                        visited.add(key)
                        news['content'] = texts
                        unique_news.append(news)
                else:
                    logging.info(f'{news["topic"]}--已跳过：{news["url"]}')

        df = pd.DataFrame(unique_news)
        df.to_excel(f'../output/{self.name}_news.xlsx', index=False)
        logging.info("保存完毕！！")

        # 关闭浏览器
        tab.close()

    @staticmethod
    def fetch_news_data(page):
        titles = page.eles('@mqy_name=search_list ')
        times = page.eles('xpath://*[@id="search-form"]/div[7]/div/div[1]/div[11]/div/div[2]/div[2]/div/span[2]')
        news_data = []

        for title, time in zip(titles, times):
            url = title.attr('href')
            topic = title.text.strip()
            date_match = re.search(r'\d{4}-\d{2}-\d{2}', time.text)
            date = date_match.group(0) if date_match else None

            news_data.append({'url': url, 'topic': topic, 'date': date})

        return news_data

    @staticmethod
    def fetch_page_content(page, url):
        page.get(url, retry=1, timeout=5)
        try:
            elements = page.eles('xpath://*')
            texts = []

            # 排除的关键字列表
            non_keywords = ['版权所有', '联系我们', '网站地图', 'ICP备案', '浏览器推荐',
                            'index.html', '版权声明', '信息公开指南', '扫一下', '索引号',
                            '邮政编码', '智能问答用户', '关怀版', '老年模式', '公安网备']

            for element in elements:
                try:
                    text = element.text
                    # 排除不符合要求的段落，字数少于75，有大量无意义符号
                    if len(text) > 75 and text.count('\n') <= 10 and text.count('\t') <= 7:
                        if not any(non_keyword in text for non_keyword in non_keywords):
                            # logging.info(f"获取新闻内容为: {text}")
                            cleaned_text = re.sub(r'\s+', '', text)
                            texts.append(cleaned_text)
                except Exception as e:
                    # logging.info(f"Error processing element: {e}")
                    pass
            return texts
        except:
            logging.error(f"{url} 存在问题！")
            return []

    @staticmethod
    def contains_keywords(text, keywords):
        """检查文本中是否包含给定的关键词列表中的任一关键词。"""
        return any(keyword in text for keyword in keywords)


if __name__ == '__main__':
    Test = ZhengJiangSpider()
    Test.run()
