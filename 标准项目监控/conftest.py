#!/usr/bin/python
# encoding=utf-8

""" Can only be modified by the administrator. Only fixtures are provided.
"""
import json
import os
import time

import pytest

# Initial
import requests

_project_dir = os.path.dirname(os.path.abspath(__file__))

def send_msg_text(msg_text):
    # web_hook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/b2b2106c-64f3-4f44-bcf2-4fac2adcac0c"#自测推送地址
    web_hook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/2935f6de-9c7a-4f43-8170-addca9dcb2ef'  # 自动化群组
    data = {
        "msg_type": "text",
        "content": {
            "text": msg_text
        }
    }
    requests.post(url=web_hook_url, data=json.dumps(data))

def get_times():
    # 获取当前时间戳
    t = time.time()  # 获取当前时间
    localtime = time.strftime("%Y-%m-%d %H:%M:%S.%s", time.localtime())
    return localtime

@pytest.fixture(scope="session", autouse=True)
def _project_cache(request):
    request.config.cache.set("project_dir", _project_dir)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    print('------------------------------------')

    # 获取钩子方法的调用结果
    out = yield
    print('用例执行结果', out)

    # 3\. 从钩子方法的调用结果中获取测试报告
    report = out.get_result()

    print('测试报告：%s' % report)
    print('步骤：%s' % report.when)
    nodeid = report.nodeid.encode('utf-8').decode('unicode_escape')
    print('nodeid：%s' % nodeid)

    # 如果失败在这里拼装消息&发送
    # print('description:%s' % str(item.function.__doc__))
    print(('运行结果: %s' % report.outcome))
    if report.outcome !='passed':
        print('发送消息')
        temp = report.nodeid.encode('utf-8').decode('unicode_escape')
        send_msg_text(f'时间:{get_times()}\ncase失败:\n{temp}')


from _pytest import runner
def pytest_collection_modifyitems(items):
    for item in items:
        # item.name = item.neme.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')

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
    s = '''编辑文案:12
    第二行:889
    第三行:确认'''
    send_msg_text(s)