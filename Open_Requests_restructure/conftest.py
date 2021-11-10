#!/usr/bin/python
# encoding=utf-8

""" Can only be modified by the administrator. Only fixtures are provided.
"""
import os
import time
import pytest
import requests
import json
import urllib3



_project_dir = os.path.dirname(os.path.abspath(__file__))
urllib3.disable_warnings()


def get_token(app_id = "cli_a18033b79138d013",app_secret = "2XRmsDPRSKqK92uN3boDGekgaqSIG36s"):
    """获取应用token，需要用app_id和app_secret，主要是上传图片需要用到token"""
    url = r"https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    headers = {"Content-Type": "text/plain"}
    Body = {
    "app_id":app_id,
    "app_secret":app_secret
    }
    r = requests.post(url, headers=headers, json=Body)
    return json.loads(r.text)['tenant_access_token']

def get_chat_id():
    url = r'https://open.feishu.cn/open-apis/chat/v4/list'
    headers = {'Authorization': "Bearer " + get_token(),"Content-Type": "application/json; charset=utf-8"}
    r = requests.post(url, headers=headers)
    return r.json()['data']['groups'][0]['chat_id']

def upload_image(image_path):
    """上传图片"""
    with open(image_path, 'rb') as f:
        image = f.read()
    resp = requests.post(
        url='https://open.feishu.cn/open-apis/image/v4/put/',
        headers={'Authorization': "Bearer "+get_token()},
        files={
            "image": image
        },
        data={
            "image_type": "message"
        },
        stream=True)
    resp.raise_for_status()
    content = resp.json()
    if content.get("code") == 0:
        return content['data']['image_key']
    else:
        return Exception("Call Api Error, errorCode is %s" % content["code"])

def send_text(Text,bot):
    """发送普通消息"""
    url = f"https://open.feishu.cn/open-apis/bot/v2/hook/{bot}"
    headers = {"Content-Type": "text/plain"}
    data = {
        "msg_type": "text",
        "content": {
            "text": Text
        }
    }
    r = requests.post(url, headers=headers, json=data,verify=False)
    return r.text

def send_img(path,bot):
    """发送图片消息"""
    url = f"https://open.feishu.cn/open-apis/bot/v2/hook/{bot}"
    headers = {"Content-Type": "text/plain"}
    data = {
        "msg_type":"image",
        "content":{
            "image_key": upload_image(path)
        }
    }
    r = requests.post(url, headers=headers, json=data,verify=False)
    return r.text

def send_markdown(text,img_path,bot):
    """发送富文本消息"""
    url = f"https://open.feishu.cn/open-apis/bot/v2/hook/{bot}"


    img = upload_image(img_path)
    chat_id = get_chat_id()

    headers = {"Content-Type": "text/plain"}
    data = {
    "chat_id":chat_id,
    "msg_type": "interactive",
    "card":{
      "elements":[
         {
            "tag":"img",
            "title":{
               "tag":"plain_text",
               "content":text
            },
            "img_key":img,
            "mode": "fit_horizontal",
            "alt":{
               "tag":"plain_text",
               "content":"Hover图片后的tips提示，不需要可以传空"
            }
         }
      ]
   }
}
    r = requests.post(url, headers=headers, json=data,verify=False)
    return r.text

def send_card(Text,bot):
    """发送卡片消息"""
    url = f"https://open.feishu.cn/open-apis/bot/v2/hook/{bot}"
    headers = {"Content-Type": "text/plain"}
    data = {
    "msg_type": "interactive",
    "card": Text
    }
    r = requests.post(url, headers=headers, json=data,verify=False)
    return r.text


def get_times():
    # 获取当前时间戳
    t = time.time()  # 获取当前时间
    localtime = time.strftime("%Y-%m-%d %H:%M:%S.%s", time.localtime())
    return localtime

@pytest.fixture(scope="session", autouse=True)
def _project_cache(request):
    request.config.cache.set("project_dir", _project_dir)

# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     print('------------------------------------')
#
#     # 获取钩子方法的调用结果
#     out = yield
#     print('用例执行结果', out)
#
#     # 3\. 从钩子方法的调用结果中获取测试报告
#     report = out.get_result()
#
#     print('测试报告：%s' % report)
#     print('步骤：%s' % report.when)
#
#     nodeid = report.nodeid.encode('utf-8').decode('utf-8')
#     print('nodeid：%s' % nodeid)
#     # 如果失败在这里拼装消息&发送
#     # print('description:%s' % str(item.function.__doc__))
#     report.description = str(item.function.__doc__)
#     print(('运行结果: %s' % report.outcome))
#     if report.outcome !='passed':
#         print('发送消息')
#         temp = report.nodeid.encode('utf-8').decode('utf-8')
#         # temp = report.description.encode('utf-8').decode('utf-8')
#         text = f'NPO导流页面监控\n时间:{get_times()}\ncase失败:\n{temp}'
#         img_path = 'index.png'
#         # bot = '6fbd7c64-f0ee-4397-8ff1-e1470529b991'#测试群组
#         bot = '2935f6de-9c7a-4f43-8170-addca9dcb2ef'
#         # send_msg_text(text)
#
#         # send_markdown(text, img_path, bot)#发送消息
#
#     # else:
#     #     send_msg_text(f'时间:{get_times()}\nNPO导流页面监控,运转正常')


from _pytest import runner
def pytest_collection_modifyitems(items):
    for item in items:
        # item.name = item.neme.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('utf-8')

# Auto import fixtures
_fixtures_dir = os.path.join(_project_dir, "fixtures")
for root, _, files in os.walk(_fixtures_dir):
    for file in files:
        if os.path.isfile(os.path.join(root, file)):
            if file.startswith("fixture_") and file.endswith(".py"):
                _fixture_name, _ = os.path.splitext(file)
                try:
                    exec(f"from fixtures.{_fixture_name} import *")
                except:
                    pass
                try:
                    exec(f"from .fixtures.{_fixture_name} import *")
                except:
                    pass


if __name__ == '__main__':

    # send_msg_text(f'时间:NPO导流页面监控,运转正常')
    bot = '2935f6de-9c7a-4f43-8170-addca9dcb2ef'
    # bot = 'b2b2106c-64f3-4f44-bcf2-4fac2adcac0c'
    img_path = 'index.png'
    text = '测试多行\n文本'
    send_markdown(text,img_path,bot)