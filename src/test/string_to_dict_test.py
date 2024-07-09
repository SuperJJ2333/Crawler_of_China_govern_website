import json
import urllib.parse


def query_string_to_dict(query_string):
    # 使用 urllib.parse.parse_qs 函数解析查询字符串
    parsed_dict = urllib.parse.parse_qs(query_string, keep_blank_values=True)

    # 由于 parse_qs 返回的值是列表，需要将列表中的单个值提取出来
    result_dict = {key: value[0] for key, value in parsed_dict.items()}

    return result_dict

def query_string_to_decoded_dict(query_string):
    # URL 解码
    decoded_data = urllib.parse.unquote(query_string)

    # 解析 JSON
    data_dict = json.loads(decoded_data)

    return data_dict

def query_string_to_dict_parse(encoded_data):

    decoded_data = urllib.parse.unquote(encoded_data)
    data_dict = json.loads(decoded_data)
    return data_dict

def json_to_form_data(json_data):
    json_data = json.loads(json_data)
    # 将JSON数据转换为表单数据
    form_data = {key: str(value) for key, value in json_data.items() if value is not None and value != ""}

    return form_data


if __name__ == '__main__':
    while True:
        search_string = input("请输入查询字符串：")
        if search_string == "decode":
            search_string = input("请输入需要解码的查询字符串：")
            result_dict = query_string_to_decoded_dict(search_string)
            print(result_dict)
        elif search_string == "exit":
            break
        elif search_string == "parse":
            search_string = input("请输入需要解析的查询字符串：")
            result_dict = query_string_to_dict_parse(search_string)
            print(result_dict)
        elif search_string == "json":
            search_string = input("请输入JSON数据：")
            result_dict = json_to_form_data(search_string)
            print(result_dict)
        else:
            result_dict = query_string_to_dict(search_string)
            print(result_dict)


