import copy
import json
import urllib
from urllib import parse
from urllib.parse import unquote, quote

from bs4 import BeautifulSoup


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


def set_nested_value(dic, path, value):
    """
    根据点分隔的路径在嵌套字典中设置值。
    例如，给定字典 `{'a': {'b': 1}}`，路径 `a.b`，值 `2`，则函数会修改字典为 `{'a': {'b': 2}}`。

    :param dic: 要修改的字典。
    :param path: 表示目标位置路径的字符串，路径各部分由点分隔。
    :param value: 在目标位置设置的值。
    """
    if isinstance(dic, str):
        parsed_query = parse.parse_qs(dic)

        # 修改参数 p 的值
        parsed_query[path] = [value]  # 将 p 的值修改为 2

        # 将解析后的查询参数转换回查询字符串
        updated_query_string = parse.urlencode(parsed_query, doseq=True)

        return updated_query_string

    if 'params' in dic:
        dic = set_nested_value_by_list(dic, path, value)
        return dic

    keys = path.split('.')  # 通过点分割路径字符串获取所有键
    for key in keys[:-1]:  # 遍历所有键（除了最后一个）
        dic = dic.setdefault(key, {})  # 获取键对应的字典值，如果不存在，则初始化为字典并返回
    dic[keys[-1]] = int(value)  # 在最后一个键处设置值

    return dic


def query_string_to_dict_parse(encoded_data):
    decoded_data = urllib.parse.unquote(encoded_data)
    data_dict = json.dumps(decoded_data)
    return decoded_data


if __name__ == '__main__':
    # post_data = 'websiteid={city_code}&q=%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&p=1&pg=19&cateid=40&pos=title&pq=&oq=&eq=&begin=&sortType=0&end=&tpl=38'
    #
    # path = 'p'
    # value = 4
    # data_copy = copy.deepcopy(post_data) if post_data else {}
    #
    # updated_post_data = set_nested_value(post_data, path, value)
    # print(updated_post_data)
    # # print(post_data)
    # print("*" * 20)
    #
    # print(query_string_to_dict_parse(updated_post_data))
    # # print(query_string_to_dict_parse(post_data))

    text = """
    <div class="jcse-result-box news-result">
    		<div class="jcse-news-title">
				<span style="max-width: 80px;height: 22px;font-size: 15px;padding: 0 10px;line-height: 20px;margin-right: 10px;font-family: '微软雅黑,宋体';background: #d40000;color: #ffffff;">工会要闻</span>
				<a target="_blank" href="visit/link.do?url=https%3A%2F%2Fzxfw.sdgh.org.cn%2Fqlgh%2F%23%2FnewsDetail%3Ftype%3Dimp_news%26id%3D33343786138541061&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&websiteid=370300000000000&title=%E6%B7%84%E5%8D%9A%E5%B8%82%E6%80%BB%E5%B7%A5%E4%BC%9A%E8%B0%83%E7%A0%94%E7%BB%84%E8%B5%B4%E9%97%BD%E6%B5%99%E7%9A%96%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F">淄博市总工会调研组赴闽浙皖<em>学</em><em>习</em><em>考</em><em>察</em></a></div>
    		<div class="jcse-news-abs">
    			<div class="jcse-news-abs-content">
    				
    			</div>
				<div class="jcse-news-other-info">
	        		<div class="jcse-news-url"><a target="_blank" href="visit/link.do?url=https%3A%2F%2Fzxfw.sdgh.org.cn%2Fqlgh%2F%23%2FnewsDetail%3Ftype%3Dimp_news%26id%3D33343786138541061&q=%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F%20%E8%80%83%E5%AF%9F%E5%AD%A6%E4%B9%A0&websiteid=370300000000000&title=%E6%B7%84%E5%8D%9A%E5%B8%82%E6%80%BB%E5%B7%A5%E4%BC%9A%E8%B0%83%E7%A0%94%E7%BB%84%E8%B5%B4%E9%97%BD%E6%B5%99%E7%9A%96%E5%AD%A6%E4%B9%A0%E8%80%83%E5%AF%9F">https://zxfw.sdgh.org.cn/qlgh/#/newsDetail?type=imp_news&id=33343786138541061</a></div>
	        		<span class="jcse-news-date">2024-03-28</span>
	    		</div>
    		</div>
	<div class="jcse-similarly-box" style="display:none;">
		<div class="jcse-similarly-head"><a><span>相似文章</span></a></div>
    <div class="jcse-similarly-items">
    </div>
    </div>
		</div> 
"""

    soup = BeautifulSoup(text, 'html.parser')

    # 提取标题
    title_tag = soup.find('a', title=True)
    topic = title_tag['title'] if title_tag else None

    # 提取 URL
    url_tag = title_tag['href'] if title_tag else None
    url = url_tag.split('url=')[1].split('&')[0] if url_tag else None
    url = unquote(url)

    # 提取发布日期
    date_tag = soup.find('span', class_='jcse-news-date')
    date = date_tag.text.strip() if date_tag else None
    date = date.split()[-1] if date else None
