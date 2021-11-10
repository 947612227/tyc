import datetime
import random

import allure
import jsonschema
import pytest
import requests
import json
import time


# 调用 专业版-高级搜索-不同企业类型 接口
# requests.packages.urllib3.disable_warnings()
# url : 'http://cstd.test63.tianyancha.com/cloud-search-company/company/screen.json'
# data : {
#     'companyTypeOr': 2,
#     'comCategoryOr': 1,
#     'ps': 20,
#     'pn': 1
# }
# headers : {
#     'Cookie': ''
# }
#
# req : requests.post(url:url, data:data, headers:headers, verify:False).json()['data']['items']
# print(req)
# # req_len : len(req)
# # for i in range(req_len):
# #     print(req[i]['name'])


# # 接口测试临时脚本
# host = 'http://10.2.128.196:20064'
# url = '/services/v3/open/investtree'
# params = {
#     'keyword': '北京百度网讯科技有限公司',
#     'appDateBegin': '2010-01-01',
#     'appDateEnd': '2021-01-01',
#     'tmClass': '29',
#     'status': 1,
#     'pageNum': 1,
#     'pageSize': 20,
# }
# req = requests.get(url=host + url, params=params).json()
# print(json.dumps(req, indent=2, ensure_ascii=False))
# print('items=', len(req['result']['items']))
# print('total=', req['result']['total'])

# 本地联调曌哥的飞书告警服务
# req = requests.post(
#     url='http://10.2.16.83:10031/alarm/api',
#     json={
#         "apiId": 353,
#         "text": "这是一条测试信息",
#         "level": "L2"
#     },
#     headers={
#         "Content-Type": "application/json"
#     })
# print(req.text)

# 测试接口超时响应
# url = 'http://open.api.tianyancha.com/services/v3/open/investtree'
# params = {
#     'flag': 4,
#     'dir': 'down',
#     'keyword': '北京百度网讯科技有限公司',
# }
# try:
#     headers = {'Authorization': '3d3e7ba1-9da9-4189-9b2a-2b8bd7f6c74d'}
#     req = requests.get(url=url, params=params, headers=headers, timeout=1).json()
#     print(req)
# except Exception as e:
#     print(e)

# head first python练习代码
# odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
#         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
#         41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
# for i in range(5):
#     right_this_minute = datetime.datetime.today().minute
#     if right_this_minute in odds:
#         print('This minute seems a little add.')
#     else:
#         print('Not an odd minute.')
#     wait_time = random.randint(1, 60)
#     time.sleep(wait_time)

# jsonschema实践
# import yaml
#
#
# class TestDemo:
#     def setup_method(self):
#         with open('/Users/tyc/PycharmProjects/Open_Requests/tmp/api_date.yaml') as f:
#             self.date = yaml.safe_load(f)
#
#     def test_one(self):
#         result = requests.get('http://open.api.tianyancha.com/services/open/ic/snapshot?keyword=北京百度网讯科技有限公司')
#         allure.attach(json.dumps(result.json(), indent=2, ensure_ascii=False), allure.attachment_type.JSON)
#         schema_1045 = self.date['schema_1045']
#         jsonschema.validate(result.json(), schema_1045)
#
#     def test_two(self):
#         res1 = requests.get('http://open.api.tianyancha.com/services/open/ic/baseinfo/normal?keyword=北京百度网讯科技有限公司')
#         print(res1.json())
#         allure.attach(json.dumps(res1.json(), indent=2, ensure_ascii=False), allure.attachment_type.JSON)
#         schema_1116 = self.date['schema_1116']
#         jsonschema.validate(res1.json(), schema_1116)
