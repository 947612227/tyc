import requests
import json

"""
    脚本介绍：
    1.给定接口url、params，可以得到如下内容：
      ①获取 <测试环境、线上环境> 返回的json报文。
      ②获取 <测试环境、线上环境> 返回的json报文中，所有字段名称。
    2.给定接口id，可以得到如下内容：
      ①获取 <接口平台详情页> 返回字段说明中，所有字段名称
"""

id = '1126'
api_id = '980机构成员'
url = '/services/open/ic/baseinfo/invoiceWithBank'
params = {
    'id': 22822,
    'name': '北京百度网讯科技有限公司',
    'keyword': '北京百度网讯科技有限公司',
    'pageNum': 1,
    'pageSize': 20,
}

# -------------提取<测试环境>接口返回json内容中，所有字段的名称----------------
test_request = requests.get(url='http://10.39.222.35:20064' + url, params=params).json()  # 请求接口
test_file_path = '/Users/tyc/PycharmProjects/TYC-requests/tmp/api_interface/test_diff/test_key.txt'  # 文件路径
with open(test_file_path, 'w') as test_file:  # 打开文件，写权限
    test_file.write(json.dumps(test_request, indent=1, sort_keys=True, ensure_ascii=False))  # 格式化json内容并写入文件
test_key_list = []  # 定义列表
with open(test_file_path, 'r') as test_file:  # 打开文件，读权限
    for test_key in test_file:  # 遍历文件内容
        if test_key.find('": ') >= 0:  # 判断是否找到指定内容，是则返回索引值，否则返回-1
            test_key_list.append(test_key.split('"')[1])  # 将匹配的行以"符号切割，取索引值1的内容，并添加到列表里
            test_key_list = list(set(test_key_list))  # set转为集合起到去重作用，list再转回列表
            test_key_list.sort()  # sort对列表内容排序
with open(test_file_path, 'w') as test_file:  # 打开文件，写权限
    for test_key in test_key_list:  # 遍历列表内容
        test_file.write(test_key + '\n')  # 逐一写入文件同时换行

# # -------------提取<线上环境>接口返回json内容中，所有字段的名称----------------
# open_request = requests.get(url='http://open.api.tianyancha.com' + url, params=params).json()  # 请求接口
# open_file_path = '/Users/tyc/PycharmProjects/Open_Requests/tmp/api_interface/test_diff/open_key.txt'  # 文件路径
# with open(open_file_path, 'w') as open_file:  # 打开文件，写权限
#     open_file.write(json.dumps(open_request, indent=1, sort_keys=True, ensure_ascii=False))  # 格式化json内容并写入文件
# open_key_list = []  # 定义列表
# with open(open_file_path, 'r') as open_file:  # 打开文件，读权限
#     for open_key in open_file:  # 遍历文件内容
#         if open_key.find('": ') >= 0:  # 判断是否找到指定内容，是则返回索引值，否则返回-1
#             open_key_list.append(open_key.split('"')[1])  # 将匹配的行以"符号切割，取索引值1的内容，并添加到列表里
#             open_key_list = list(set(open_key_list))  # set转为集合起到去重作用，list再转回列表
#             open_key_list.sort()  # sort对列表内容排序
# with open(open_file_path, 'w') as open_file:  # 打开文件，写权限
#     for open_key in open_key_list:  # 遍历列表内容
#         open_file.write(open_key + '\n')  # 逐一写入文件同时换行

# # -------------提取<接口平台详情页>返回字段说明中，所有字段的名称----------------
platform_url = f'http://open.test63.tianyancha.com/open-admin/interface/uni.json?id={id}'  # 平台页面接口
platform_request = requests.get(url=platform_url).json()['data']['returnParam']  # 请求接口，提取 returnParam 返回内容
platform_file_path = '/Users/tyc/PycharmProjects/TYC-requests/tmp/api_interface/test_diff/platform_key.txt'  # 文件路径
request_loads = json.loads(platform_request)  # json.loads将 returnParam 返回的json内容转换成字典类型
request_dumps = json.dumps(request_loads, indent=1, sort_keys=True, ensure_ascii=False)  # 格式化json内容
with open(platform_file_path, 'w') as platform_file:  # 打开文件，写权限
    platform_file.write(request_dumps)  # 将格式化json内容写入文件
platform_key_list = []  # 定义列表
with open(platform_file_path, 'r') as platform_file:  # 打开文件，读权限
    for platform_key in platform_file:  # 遍历文件内容
        if platform_key.find('"name": "') >= 0:  # 判断是否找到指定内容，是则返回索引值，否则返回-1
            platform_key_list.append(platform_key.split('"')[3])  # 将匹配的行以"符号切割，取索引值3的内容，并添加到列表里
            platform_key_list = list(set(platform_key_list))
            platform_key_list.sort()  # sort对列表内容排序
with open(platform_file_path, 'w') as platform_file:  # 打开文件，写权限
    for platform_key in platform_key_list:  # 遍历列表内容
        if platform_key == '_child':  # 如果遍历内容等于指定的值，就pass
            pass
        else:
            platform_file.write(platform_key + '\n')  # 否则就把内容写到文件里

# # -------------获取<测试环境、线上环境>接口返回的json内容----------------
# try:  # 获取测试环境返回内容
#     test_request = requests.get(url='http://10.2.128.196:20064' + url, params=params).json()  # 请求接口
#     test_file_path = '/Users/tyc/PycharmProjects/Open_Requests/tmp/api_interface/test_diff/test_result.json'  # 文件路径
#     with open(test_file_path, 'w') as test_file:  # 打开文件，写权限
#         test_file.write(json.dumps(test_request, indent=2, sort_keys=True, ensure_ascii=False))  # 写入格式化好的json内容
# except Exception as e:  # 有异常打印下面内容
#     print('Error：测试环境返回不是json内容，请检查！！')
#
# try:  # 获取线上返回内容
#     open_request = requests.get(url='http://open.api.tianyancha.com' + url, params=params).json()  # 请求接口
#     open_file_path = '/Users/tyc/PycharmProjects/Open_Requests/tmp/api_interface/test_diff/open_result.json'  # 文件路径
#     with open(open_file_path, 'w') as open_file:  # 打开文件，写权限
#         open_file.write(json.dumps(open_request, indent=2, sort_keys=True, ensure_ascii=False))  # 写入格式化好的json内容
# except Exception as e:  # 有异常打印下面内容
#     print('Error：线上环境返回不是json内容，请检查！！')
