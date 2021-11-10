# -*- coding: UTF-8 -*-

"""
    @Description：工具模块
    @author：by ChenZhang
    @create：2021/6/8 10:46 上午

"""

import datetime
import hashlib
import json
import time
import requests
import pandas as pd
import yaml


# 获取当前的时间戳和以前的时间戳（毫秒级）
def get_timestamp_and_previous_timestamp(day=90):
    # 获取当前时间戳
    t = time.time()  # 获取当前时间
    cur_timestamp = int(round(t * 1000))

    # 获取特定时间前的时间戳
    previous_day = datetime.datetime.now() - datetime.timedelta(days=day)
    day = time.mktime(previous_day.timetuple())
    previous_timestamp = int(round(day * 1000))
    return cur_timestamp, previous_timestamp


# 写文件函数
def write_file(path, content):
    with open(path, 'a+', encoding='utf-8', newline="") as f:
        f.write(f'{content}\n')


# 读取csv
def read_csv(path="", node=""):
    data = pd.read_csv(path, error_bad_lines=False, encoding='utf-8')
    if len(node) > 0:
        return data[node].tolist()
    else:
        return data


# 读取yaml
def read_yaml(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as data:
        return yaml.safe_load(data)


# md5加密
def md5value(key, method="小写32位"):
    input_name = hashlib.md5()
    input_name.update(key.encode("utf-8"))
    if method == "小写16位":
        return (input_name.hexdigest())[8:-8].lower()
    elif method == "小写32位":
        return (input_name.hexdigest()).lower()
    elif method == "大写16位":
        return (input_name.hexdigest())[8:-8].upper()
    else:
        return (input_name.hexdigest()).upper()


# 获取专业版会话对象
def get_std_cookie(username="tester_chen", password="888888"):
    url = "http://cstd.test63.tianyancha.com/user-security/aut/login.json"
    md5_password = md5value(password)
    headers = {
        "Content-Type": "application/json"
    }
    param = {
        "username": username,
        "password": md5_password,
        "validCode": "111111",
        "loginMode": "PWD",
        "rememberMe": True
    }
    s = requests.Session()
    s.post(url, data=json.dumps(param), headers=headers)
    return s


# 获取分组id，如果指定分组的已有数量大于900则会自动新建分组
def get_group_id(username, password, group_name="默认分组"):
    session = get_std_cookie(username, password)
    url = "http://cstd.test63.tianyancha.com/user-monitor/domain/show/group.json?_t=1623203130160"
    h = session.get(url).json()
    index = ""
    temp_index = ""
    for i in range(len(h["data"])):
        if h["data"][i]["name"] == group_name:
            index = i
        else:
            pass
    # 容错当前分组大于900
    if h["data"][index]["count"] > 900:
        temp_group_name = str(int(time.time()))
        add_group(username, password, group_name=temp_group_name)
        h1 = session.get(url).json()
        # 获取指定分组的索引
        for i in range(len(h1["data"])):
            if h1["data"][i]["name"] == temp_group_name:
                temp_index = i
            else:
                pass
        return h1["data"][temp_index]["id"], session
    else:
        return h["data"][index]["id"], session


# 新建分组
def add_group(username, password, group_name):
    session = get_std_cookie(username, password)
    headers = {"Content-Type": "application/json"}
    url = "http://cstd.test63.tianyancha.com/user-monitor/domain/operate/add/group.json?_t=1623894927283"
    param = {"name": group_name}
    h = session.post(url, data=json.dumps(param), headers=headers).json()
    return h


# 添加监控主体
def add_monitor_entity(username="1619343813自动化用户", password="888888", group_name="默认分组",
                       cgids=[], brids=[], hcgid=[]):
    url = "http://cstd.test63.tianyancha.com/user-monitor/domain/operate/add/domain.json?_t=1623168601269"
    headers = {"Content-Type": "application/json"}
    group_id, session = get_group_id(username, password, group_name)
    param = {
        "groupIds": [int(group_id)],
        "cgids": cgids,
        "brids": brids,
        "hcgids": hcgid
    }
    h = session.post(url, data=json.dumps(param), headers=headers).json()
    return h


# 勾选指定分组下的关联监控
def operate_associate():
    operate_url = "http://cstd.test63.tianyancha.com/user-monitor/domain/operate/change/associate.json?_t=1625036157539"


# 查询指定分组下的主体
def get_all_company(username, password, group_name, groupId=0, pn=1):
    get_group_id()
    list_url = f"http://cstd.test63.tianyancha.com/user-monitor/domain/show/list.json?_t=1625036158242&groupId={groupId}&pn={pn}&ps=10"
    return requests.get(list_url)


# 推送实时邮件、日报
def push_message(channel="d_emal"):
    daily_mail_url = "http://10.2.16.3:20040/push/email/day"
    daily_wechat_url = "http://10.2.16.3:20040/push/wechat/day"
    realtime_email = "http://10.2.16.3:20040/push/email/realtime"
    if channel == "d_email":
        return requests.post(daily_mail_url).text
    elif channel == "d_wechat":
        return requests.post(daily_wechat_url).text
    else:
        return requests.post(realtime_email).text


# 自定义构建动态维度数据
def generate_kafka_msg(param):
    url = "http://10.2.16.88:20001/increment/generateKafkaMsg"
    h = requests.post(url, param).json()
    return h


class Associate:
    def __init__(self, username, password="888888", group_name=""):
        self.username = username
        self.password = password
        self.group_name = group_name
        self.session = get_std_cookie(self.username, self.password)
        self.host = "http://cstd.test63.tianyancha.com/"
        self.list_uri = "user-monitor/domain/show/list.json?"
        self.operate_uri = "user-monitor/domain/operate/change/associate.json?_t=1625036157539"
        self.headers = {"Content-Type": "application/json"}

    # 查询指定分组下的主体
    def get_all_company(self, groupId=0, pn=1):
        list_url = self.host + self.list_uri
        param = f"_t=1625036158242&groupId={groupId}&pn={pn}&ps=10"
        return self.session.get(list_url + param).json()

    # 勾选指定分组下的关联监控
    def operate_associate(self):
        # 处理id
        h = self.get_all_company()
        ids = []
        if h["code"] == 2000:
            company_total = h["data"]["agg"]["aggs"]["type"][1]["value"]
            if company_total == 0:
                return "当前分组下的企业数量为空"
            elif 0 < company_total <= 10:
                # 少于等于10个则不分页
                for i in range(company_total):
                    ids.append(h["data"]["domains"][i]["id"])
            else:
                # 大于10个分页处理
                if company_total % 10 != 0:
                    pn_total = int(company_total / 10) + 1
                    for i in range(pn_total):
                        h = self.get_all_company(pn=i + 1)
                        total_count = len(h["data"]["domains"])
                        for j in range(total_count):
                            ids.append(h["data"]["domains"][j]["id"])
                else:
                    pn_total = int(company_total / 10)
                    for i in range(pn_total):
                        h = self.get_all_company(pn=i + 1)
                        total_count = len(h["data"]["domains"])
                        for j in range(total_count):
                            ids.append(h["data"]["domains"][j]["id"])
        else:
            return "⚠️：检查服务是否可用"

        # 开始操作关联监控
        operate_url = self.host + self.operate_uri
        """
            容错关联监控席位达到上限1W,故采取方案：
            1.测试环境修改上限（有一定风险将此功能随版本上到生产）
            2.处理添加关联监控达到上限后则不添加(采用)
        """
        for i in ids:
            param = {
                "ids": [i],
                "associateIds": ["1", "2", "3", "4", "5", "6"]
            }

            res = self.session.post(operate_url, data=json.dumps(param), headers=self.headers).json()
            if res["code"] == 2000:
                print("操作成功")
            else:
                # print("请检查数据", res)
                break
