import time

from loguru import logger
import re
from DrissionPage import ChromiumPage
from concurrent.futures import ThreadPoolExecutor, as_completed

from src.common.form_utils import *


def fetch_news_data(titles, times, link, targeted_date, page_num):
    """获取URL中的标题与时间"""
    news_data = []
    for title, time in zip(titles, times):
        try:
            if not title or not time:
                continue

            if title.text is None and title is None and title.text.strip() == '':  # 更明确地检查标题元素和文本的存在性
                continue

            try:
                # 尝试获取链接和标题属性
                url = title.get('href', '')
            except:
                url = title.attr('href')
            try:
                topic = title.get('title', '').strip()
            except:
                topic = title.text.strip()

            # 如果链接不完整，添加基础链接
            if not url.startswith('http'):
                url = link + url

            # 检查time元素的存在性，并且确保text属性也存在
            if isinstance(time, str):
                date = time.strip()
            elif time.text and title.text.strip() != '':  # 修正这里的逻辑
                date = time.text.strip()
            else:
                date = ''

            data = clean_news_data({'url': url, 'topic': topic, 'date': date})

            # 判断是否符合目标年份
            if is_in_year(data['date'], targeted_date):
                news_data.append(data)
        except Exception as e:
            logger.warning(f"获取标题时出现问题 - {e} - {link} - {title.text}")
            continue
    logger.info(f"第{page_num}页 - 符合年份为{targeted_date}的新闻有 {len(news_data)}/{len(titles)} 条")
    return news_data


def fetch_page_content(page, url, title):
    """
    访问指定的 URL，获取网页内容，并清除不需要的内容。

    参数:
    page -- 页面操作对象。
    url -- 需要访问的 URL 地址。
    title -- 页面的标题，用于过滤和内容比对。

    返回:
    texts -- 清洗后的文本列表。
    """
    # 新建标签页并尝试访问 URL
    tab = page.new_tab()
    tab.get(url, retry=3, timeout=60)
    if not tab.wait.doc_loaded():
        logger.warning(f"页面加载超时 - {url}")
        tab.refresh()

    # 初始化文本容器
    unique_texts = set()
    texts = []

    page.wait(2, 5)  # 等待页面加载完成

    # 尝试获取页面的所有元素
    try:
        elements = tab.s_eles('@text()')
        if not elements:  # 如果未找到元素，尝试刷新页面
            tab.refresh()
            elements = tab.eles('@text()')
    except Exception as e:
        logger.error(f"没有必要元素 - {e} - {url}")
        tab.close()
        return texts

    # 定义非关键词和空白字符模式
    non_keywords = ['404 Not Found', '浏览量', '视力保护色', '版权所有', '无法访问', '联系我们', '门户网站',
                    '站点不存在', '公网安备', '网站地图', '背景颜色', 'ICP备案', '无障碍', '移动端显示模式',
                    '微信扫一扫', '打印本页', '分享微信', '浏览器推荐', '首页', '登录', '智能引导', '智能问答',
                    '站群导航', '政务机器人', 'Copyright', '找不到', '窃取您的信息', '不安全', '隐私权政策'
                    'index.html', '动态信息', '404页面', '极速模式', '黔南州人民政府网站', 'My97DatePicker',
                    '版权声明', '信息公开指南', '扫一下', '索引号', '邮政编码', '关怀版', '老年模式', '公安网备',
                    '导航区', '扫描二维码', '网络诊断', '网站导航', '阅读全文',
                    '长辈版', '运维电话', '网站标识码', '无法处理此请求', '网站标识码', '运维单位', '联系电话',
                    '友情链接',
                    '相关新闻', '上一篇', '下一篇', '360浏览器', '相关链接', '县、市、区政府网站', '技术支持',
                    'PlayPauseSeek',
                    '关闭', '天气预报', '县内网站', '网站管理员', '网站管理电话', '县区网站', '省直部门网站',
                    '国务院小程序',
                    '县区政府', '国务院小程序', '中央部委网站', '相关网站', 'E-Mail', 'E-mail', '上一条', '下一条',
                    '办公地点', '工作时间',
                    '验证码', '传真', '社会主义核心价值观：', '电话：', "var d", 'var day', '机构设置政协提案',
                    '北京天津河北山西内蒙古',
                    '索 引 号', '搜一下', '本站检索', '站群检索', '信息来源', '日 一 二 三 四 五 六', '发布时间',
                    '雅安领导', '重点领域公开专栏',
                    '历史搜索', '工作报告政府公报', '公共企事业单位信息', '热搜词：', '电话号码：', '搜索范围',
                    '热门搜索', '政府会议政策解读',
                    '栏目内搜索', '12345政务服务热线', 'QQ空间', '浏览次数', '保护视力色', "The People's Government",
                    '全方位建设模范自治区', '12345信箱', '全文下载', '政策咨询服务', '网上咨询|网上投诉', '快讯'
                    ]
    # 定义如果重复出现的关键词模式
    repeated_keywords = ["网", "局", "厅", "部", "省", "办", "委", '县', '区', '院']
    space_pattern = re.compile(r'\s+')

    logger.debug(f"开始处理页面 - 共有 {len(elements)} 个元素 - {title} - {url}")

    for element in elements:
        try:
            # 获取元素的文本
            text = element.text.strip()

            # 检查文本是否重复
            if text in unique_texts:
                continue
            unique_texts.add(text)

            # 过滤空白文本和无效文本
            if text == '' or len(text) < 30:
                logger.debug(f"过滤空白或较短文本 - '{text}' - {title} - {url}")
                continue
            elif (text.count('\n') >= 8 or text.count('\t') >= 8) and len(text) < 75:
                logger.debug(f"过滤过长的空白 - '{text}' - {title} - {url}")
                continue
            else:
                pass

            # 判断文本是否为中文
            if not is_mostly_chinese(text):
                continue

            # 检查文本是否包含非关键词，过滤过长的空白和无关信息
            if not any(nk in text for nk in non_keywords):
                cleaned_text = space_pattern.sub(' ', text)  # 替换多个空白字符为单个空格
                # 进一步根据长度和标题相关性过滤文本
                """
                判断规则为：
                1，文本含有“新闻标题”且比“新闻标题”还多15个字 且 含有“学习考察”或“考察学习”
                2，文本比“新闻标题”还多20个字 且 含有“学习考察”或“考察学习”
                3，字数超过40
                4，文本中不能出现7次以上重复关键词
                """
                # 判断规则应用
                rule_1 = contains_keywords(cleaned_text) and (len(cleaned_text) - len(
                    title)) > 25 and title in cleaned_text
                rule_2 = contains_keywords(cleaned_text) and (len(cleaned_text) - len(
                    title)) > 30 and title not in cleaned_text
                rule_3 = len(cleaned_text) > 40
                rule_5 = len(cleaned_text) > 100

                # 统计重复关键词的数量
                repeated_keywords_count = sum(cleaned_text.count(keyword) >= 8 for keyword in repeated_keywords)
                # 如果句子中包含太多关键字或特定字符，则不添加该句子
                rule_4 = any([
                    cleaned_text.count("人民政府") > 6,
                    cleaned_text.count("开发区") > 6,
                    # 统计所有重复关键词的数量若超过20个，则不添加该句子
                    sum(cleaned_text.count(keyword) for keyword in repeated_keywords) >= 20,
                    repeated_keywords_count >= 1,
                    cleaned_text.count("年") > 7,
                    cleaned_text.count("》") > 7])

                if not rule_4 or rule_5:
                    if rule_1 or rule_2 or rule_3:
                        texts.append(cleaned_text)
                        logger.debug(f"添加有效文本 - '{cleaned_text}' - {title} - {url}")
                    else:
                        logger.debug(f"长度不符合要求 - '{text}' - {title} - {url}")
                else:
                    logger.debug(f"包含过多重复关键词 - '{text}' - {title} - {url}")
            else:
                logger.debug(f"包含非关键词 - '{text}' - {title} - {url}")
        except Exception as e:
            logger.debug(f"遍历元素时出现问题 - {e}")
            continue

    if not texts:
        logger.debug(f"没有有效内容 - {title} - {url}")
    # 关闭标签页并返回结果
    tab.close()

    return texts


def is_content_valuable(news, page):
    """
    检查新闻内容是否包含关键词并记录。
    参数:
    news -- 新闻数据字典。
    page -- 页面操作对象。
    返回:
    news -- 更新后的新闻字典或 None。
    """
    if news['url'] and news['url'] != '':
        texts = fetch_page_content(page, news['url'], news['topic'])
    else:
        return None

    if not texts:
        logger.error(f"无内容可抓取 - {news['topic']} - {news['url']}")
        return None

    # 判断标题是否含有关键词
    title_contains = contains_keywords(news['topic'])
    # 判断全文是否含有关键词
    content_contains = any(contains_keywords(text) for text in texts)

    if title_contains or content_contains:
        logger.success(f"{news['topic']}--"
                       f"新闻内容为: {texts[0][:200]}")
        news['content'] = texts
        return news
    elif not title_contains and not content_contains:
        # if not title_contains:
        #     logger.warning(f"{news['topic']}--标题中不包含关键词：{news['url']}")
        # if not content_contains:
        logger.warning(f"内容中不包含关键词 - {news['topic']} - {news['url']}")
    return None


def contains_keywords(text):
    """
    检查文本中是否含有设定的关键词。
    参数:
    text -- 要检查的文本字符串。
    返回:
    boolean -- 是否包含关键词。
    """
    keywords = ["考察", "学习"]
    return any(keyword in text for keyword in keywords)


def process_news_content(news_data: list, page: ChromiumPage, unique_news: list):
    """
    使用多线程处理所有新闻数据，并提取有价值的内容。

    :param
        news_data -- 新闻数据列表：格式为
            [{'url': 'https://www.baidu.com', 'topic': '百度', 'date': '2021-01-01'}]

        page -- 页面操作对象。 模拟浏览器

        unique_news -- 已访问的新闻标识集合。格式为
            [{'url': 'https://www.baidu.com', 'topic': '百度', 'date': '2021-01-01'}]

    :return:
        unique_news -- 已处理的有价值新闻列表。
        格式为
            [{'url': 'https://www.baidu.com', 'topic': '百度', 'date': '2021-01-01', ‘content': ['文本1', '文本2'}
            {}，{}，{}，{}，{}]
    """
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(is_content_valuable, news, page) for news in news_data]

        for future in as_completed(futures):
            try:
                result = future.result()
                if result:
                    unique_news.append(result)
            except Exception as e:
                logger.error(f"处理新闻内容时出现问题 - {e}")
                continue
    return unique_news
