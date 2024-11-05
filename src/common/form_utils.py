import json
from urllib import parse
from urllib.parse import unquote, quote
from datetime import datetime
import os
import re
import pandas as pd
from loguru import logger


def save_to_excel(unique_news, name, province):
    """
    将新闻数据保存为Excel文件。
    参数:
    unique_news -- 包含新闻数据的列表，其中每个元素是一个字典。
    name -- 用于生成Excel文件名的标识字符串。

    函数会将Excel文件保存在项目根目录外的`output`文件夹中。
    """
    # 创建DataFrame
    df = pd.DataFrame(unique_news)

    # 按照指定顺序排列列
    df = df[["code", "province", "city", "topic", "date", "url", "content"]]

    # 获取当前文件的目录（假设此脚本位于src/utils文件夹中）
    current_dir = os.path.dirname(__file__)

    if not os.path.exists(os.path.join(current_dir, f'../../output/{province}')):
        os.makedirs(os.path.join(current_dir, f'../../output/{province}'))  # 如果输出目录不存在，创建它

    # 构造文件完整路径
    filename = os.path.join(current_dir, f'../../output/{province}', f'{name}_学习考察.xlsx')

    # 保存到Excel，不包含索引
    df.to_excel(filename, index=False)

    # 日志记录文件保存位置
    logger.info(f"文件已保存至: {filename}")


def remove_duplicates(news_data, unique_news):
    """
    去除新闻数据中的重复条目，基于标题和日期。
    参数:
    news_data -- 新闻数据列表，每个元素是一个字典，包含'url', 'topic', 'date'等键。
    unique_news -- 用于存储已见过的(topic, date, url)元组的集合。
    返回:
    无重复的新闻数据列表。
    """
    seen = unique_news  # 用于存储已见过的(topic, date)元组
    unique_news = []

    for news in news_data:
        identifier = (news['topic'], news['date'])  # 创建一个用于识别重复的元组
        if identifier not in seen:
            seen.add(identifier)
            unique_news.append(news)
        else:
            logger.warning(f"跳过重复URL: {news['topic']} - 日期为：{news['date']}")

    return unique_news


def clean_news_data(news):
    """
    清洗新闻数据字典中的topic和date字段。
    参数:
    news -- 新闻数据字典，格式为：
        {'url': 'some_url',
        'topic': 'some_topic',
        'date': 'some_date'}

    返回:
    news -- 清洗后的新闻数据字典。
    """
    # 清洗topic，只保留中文字符
    if 'topic' in news and news['topic'] is not None:
        # 使用正则表达式匹配中文字符
        news['topic'] = ''.join(re.findall(r'[\u4e00-\u9fff]+', news['topic']))
    else:
        logger.warning(f"新闻数据中缺少'topic'字段: {news}")

    # 清洗date，确保其符合YYYY-MM-DD格式
    if 'date' in news and news['date'] is not None:
        news['date'] = format_date(news['date'])
    else:
        logger.warning(f"新闻数据中缺少'date'字段: {news}")

    if 'url' in news and news['url'] is not None:  # 清洗url，只保留域名部分
        news['url'] = format_url(news['url'])
    else:
        # pass
        logger.warning(f"新闻数据中缺少'url'字段: {news}")
    return news


def format_date(date_str):
    """
    将不同格式的日期字符串转换为 'YYYY-MM-DD' 格式。

    参数:
    date_str (str): 输入的日期字符串。

    返回:
    str: 标准化的日期字符串或者None（如果无法识别格式）。
    """
    if isinstance(date_str, str):
        if not date_str or date_str.strip() == '' or date_str.lower() == 'nan':
            return ''
    elif isinstance(date_str, float):
        if pd.isnull(date_str):
            return ''
    elif isinstance(date_str, datetime):
        return date_str.strftime('%Y-%m-%d')
    elif pd.isnull(date_str):
        return ''

    # 尝试匹配英文日期格式
    try:
        date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Z %Y")
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        pass  # 如果不匹配，继续尝试其他格式

    # 匹配 YYYY-MM-DD 格式
    match_iso = re.search(r'\d{4}-\d{1,2}-\d{1,2}', date_str)
    if match_iso:
        return match_iso.group(0)

    # 匹配 YYYY年MM月DD日 格式
    match_extended = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', date_str)
    if match_extended:
        year, month, day = match_extended.groups()
        return f"{year}-{month.zfill(2)}-{day.zfill(2)}"

    # 匹配 YYYY/MM/DD 格式
    match_line = re.search(r'(\d{4})/(\d{1,2})/(\d{1,2})', date_str)
    if match_line:
        year, month, day = match_line.groups()
        return f"{year}-{month.zfill(2)}-{day.zfill(2)}"

    # 匹配 YYYY.MM.DD 格式
    match_dot = re.search(r'(\d{4})\.(\d{1,2})\.(\d{1,2})', date_str)
    if match_dot:
        year, month, day = match_dot.groups()
        return f"{year}-{month.zfill(2)}-{day.zfill(2)}"

    # 匹配 DD-MM-YY 格式
    match_dmy = re.search(r'(\d{1,2})-(\d{1,2})-(\d{2})', date_str)
    if match_dmy:
        day, month, year = match_dmy.groups()
        year = '20' + year  # 假设年份在2000年之后
        return f"{year}-{month.zfill(2)}-{day.zfill(2)}"

    return None


def format_url(url_str):
    url_match = re.search(r"geturl\('(.*?)'", url_str)
    url_match_v2 = re.search(r"'([^']+)'", url_str)
    if url_match:
        url = url_match.group(1)
    elif url_match_v2:
        url = url_match_v2.group(1)
    else:
        url = url_str

    if not url.startswith('http'):
        logger.warning(f"URL格式不正确: {url}")
        url = ''

    return url


def is_in_year(date_str, year):
    """
    判断给定的日期字符串是否属于指定的年份。

    参数:
    date_str (str): 日期字符串，格式为 "YYYY-MM-DD"。
    year (int): 指定的年份。

    返回:
    bool: 如果日期属于指定年份，返回 True，否则返回 False。
    """
    # 从日期字符串中提取年份部分
    extracted_year = int(date_str[:4])

    # 比较提取的年份和指定的年份是否相同
    return extracted_year == year


def set_nested_value(dic, path, value):
    """
       根据点分隔的路径或键列表在嵌套字典中设置值。
       例如，给定字典 `{'a': {'b': 1}}`，路径 `a.b`，值 `2`，则函数会修改字典为 `{'a': {'b': 2}}`。
       如果路径是列表，例如 ['a', 'b']，则在字典的顶层为每个键设置相同的值。

       :param dic: 要修改的字典。
       :param path: 表示目标位置路径的字符串或键的列表，字符串路径各部分由点分隔。
       :param value: 在目标位置设置的值。
   """
    if 'params' in dic:
        dic = set_nested_value_by_list(dic, path, value)
        return dic

    if '__EVENTARGUMENT' in dic:
        # 防止是字符串，做额外处理
        if isinstance(path, str):
            parsed_query = parse.parse_qs(dic)
            parsed_query[path] = f'Page${value}'

            # 将解析后的查询参数转换回查询字符串
            updated_query_string = parse.urlencode(parsed_query, doseq=True)

            return updated_query_string
        dic[path] = f'Page${value}'
        return dic

    if isinstance(dic, str):
        parsed_query = parse.parse_qs(dic)

        # 修改参数 p 的值
        parsed_query[path] = [value]

        # 将解析后的查询参数转换回查询字符串
        updated_query_string = parse.urlencode(parsed_query, doseq=True)

        return updated_query_string

    if isinstance(path, list):
        # 如果路径是列表，为每个键设置相同的值
        for each_key in path:
            if "." not in each_key:
                dic[each_key] = value
                continue

            # 如果路径是点分隔的字符串，按照现有逻辑处理
            new_key = each_key.split('.')  # 通过点分割路径字符串获取所有键
            current_dict = dic  # 复制字典引用

            for true_key in new_key[:-1]:  # 遍历所有键（除了最后一个）
                if true_key not in current_dict or not isinstance(current_dict[true_key], dict):
                    current_dict[true_key] = {}  # 如果键不存在或其值不是字典，则初始化为字典
                current_dict = current_dict[true_key]  # 获取键对应的字典值

            # 特殊情况
            if new_key[-1] == 'goToCurrent':
                current_dict[new_key[-1]] = int(value) + 1 # 在最后一个键处设置值
                continue

            current_dict[new_key[-1]] = int(value)  # 在最后一个键处设置值

    elif isinstance(path, str):
        # 如果路径是点分隔的字符串，按照现有逻辑处理
        keys = path.split('.')  # 通过点分割路径字符串获取所有键
        current_dict = dic  # 复制字典引用

        for key in keys[:-1]:  # 遍历所有键（除了最后一个）
            if key not in current_dict or not isinstance(current_dict[key], dict):
                current_dict[key] = {}  # 如果键不存在或其值不是字典，则初始化为字典
            current_dict = current_dict[key]  # 获取键对应的字典值

        current_dict[keys[-1]] = value  # 在最后一个键处设置值

    return dic

def set_nested_value_by_list(dic, path, value):
    # 解码URL编码的字符串
    decoded_params = unquote(dic)

    # 从字符串中截取JSON部分
    json_str = decoded_params.split('params=')[1]

    # 将JSON字符串转换为字典
    params_dict = json.loads(json_str)

    # 修改page值
    params_dict[path] = int(value)  # 假设你要将页码改为3

    # 将字典转换回JSON字符串
    updated_json_str = json.dumps(params_dict, ensure_ascii=False, separators=(',', ':'))

    # 重新编码为URL格式
    updated_encoded_params = "params=" + quote(updated_json_str, safe='', encoding='utf-8')

    return updated_encoded_params.replace('%2B', '+')

def convert_timestamp_to_date(timestamp: int) -> str:

    if isinstance(timestamp, str):
        timestamp = int(timestamp)

    if len(str(timestamp)) >= 13:
        # 将时间戳转换为datetime对象
        dt_object = datetime.fromtimestamp(timestamp / 1000)
    else:
        dt_object = datetime.fromtimestamp(timestamp)
    # 格式化为YYYY-MM-DD字符串
    formatted_date = dt_object.strftime('%Y-%m-%d')
    return formatted_date


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    except TypeError as e:
        return False
    return True


def is_mostly_chinese(text):
    # 统计中文字符数量
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', text)
    num_chinese = len(chinese_chars)

    # 统计总字符数量
    total_chars = len(text)

    # 计算中文字符比例
    if total_chars == 0:
        return False
    chinese_ratio = num_chinese / total_chars

    # 返回中文字符比例是否大于一半
    return chinese_ratio > 0.7

