import pytest
from datetime import datetime
from typing import List


# 参数化过程中，将中文字符保留
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


ti = datetime.now()

"""
@pytest.hookimpl钩子函数，可以获取到测试用例不同执行阶段的结果
:param item:测试用例对象
:param call:测试用例的测试步骤
            先执行when='setup'
            后执行when='call'
            最后执行when='teardown'
"""


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport():
    print('------------------------------------')

    # 获取钩子方法的调用结果
    out = yield
    print('用例执行结果', out)

    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    print('测试报告：%s' % report)
    print('步骤：%s' % report.when)
    print('nodeid：%s' % report.nodeid)
    print('运行结果: %s' % report.outcome)

    # 当前用例名
    case_name = report.nodeid.split('::')[-1]
    print('用例名称：{}'.format(case_name))

    # 如果失败在这里拼装消息&发送
    if report.outcome != 'passed':
        print('发送报警消息，失败时间:{}'.format(ti))
