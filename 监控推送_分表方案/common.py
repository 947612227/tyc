# -*- coding: UTF-8 -*-

"""
    @Description：工具模块
    warning: 添加主题的接口还是有问题 401
    @author：by ChenZhang
    @create：2021/6/8 10:46 上午

"""

# 获取当前的时间戳和以前的时间戳（毫秒级）
import datetime
import hashlib
import json
import time
import requests
import pandas as pd
from faker import Faker


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
    password = md5value(password)
    headers = {
        "Content-Type": "application/json"
    }
    param = {
        "username": f"{username}",
        "password": f"{password}",
        "validCode": "111111",
        "loginMode": "PWD",
        "rememberMe": True
    }
    s = requests.Session()
    s.post(url, data=json.dumps(param), headers=headers)
    return s


# 获取分组id
def get_group_id(username, password, group_name="默认分组"):
    session = get_std_cookie(username, password)
    url = "http://cstd.test63.tianyancha.com/user-monitor/domain/show/group.json?_t=1623203130160"
    h = session.get(url).json()
    index = ""
    # 获取指定分组的索引
    for i in range(len(h["data"])):
        if h["data"][i]["name"] == group_name:
            index = i
        else:
            pass

    return h["data"][index]["id"], session


# 添加监控主体
def add_monitor_entity(username, password, group_name="intelnational", cgids=[4740590994], brids=[], hcgid=[]):
    url = "http://cstd.test63.tianyancha.com/user-monitor/domain/operate/add/domain.json?_t=1623168601269"
    headers = {
        "Content-Type": "application/json"
    }
    group_id, session = get_group_id(username, password, group_name)
    param = {
        "groupIds": [int(group_id)],
        "cgids": cgids,
        "brids": brids,
        "hcgids": hcgid
    }
    h = session.post(url, data=json.dumps(param), headers=headers).json()
    return h


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


def create_same_phone_data(gids):
    """
    这个是INSERT类型的消息
    data.gids 表示插入的数据中的企业id
    如有有一个就表示  [] -> [g1]，如果有多个，就表示 [] -> [g1,g2]
    """
    param = {
        "data": [{
            "id": "59319263",
            "email": "271128342@qq.com",
            "gids": f"{gids}",
            "same_count": "1",
            "deleted": "0",
            "update_time": "2021-06-02 17:08:27",
            "create_time": "2021-06-02 17:08:27"
        }],
        "database": "prism",
        "es": 1622624907000,
        "id": 229,
        "isDdl": None,
        "mysqlType": {
            "id": "bigint(20) unsigned",
            "email": "varchar(120)",
            "gids": "text",
            "same_count": "int(10)",
            "deleted": "tinyint(3) unsigned",
            "update_time": "datetime",
            "create_time": "datetime"
        },
        "old": None,
        "pkNames": ["id"],
        "sql": "",
        "sqlType": {
            "id": -5,
            "email": 12,
            "gids": 2005,
            "same_count": 4,
            "deleted": -6,
            "update_time": 93,
            "create_time": 93
        },
        "table": "company_same_email",
        "ts": 1622624907560,
        "type": "INSERT"
    }
    h = generate_kafka_msg(param)
    if h["code"] == 2000:
        return True
    else:
        return False


# 创建关联动态的数据
def create_associated_message(obj="北京太合音乐文化发展有限公司", obj_id="22822", associate="北京太合音乐文化发展有限公司", associate_id="934605"):
    param = {
        "data": [
            {
                "id": "146938801",
                "company_graph_id": f"{associate_id}",
                "company_name": f"{associate}",
                "company_name_alias": "",
                "shareholder_graph_id": f"{obj_id}",
                "shareholder_name": f"{obj}",
                "shareholder_name_alias": "",
                "shareholder_type": "2",
                "amount": "51.0",
                "capital": "[{\"amomon\": \"51万人民币\", \"paymet\": \"货币\", \"time\": \"2050-11-02\"}]",
                "capitalActl": "[]",
                "percent": "0.51",
                "source": "0",
                "create_time": "2021-05-26 10:56:20",
                "update_time": "2021-05-26 10:56:20",
                "deleted": "0"
            }
        ],
        "database": "prism1",
        "es": 1622026029000,
        "id": 12183663,
        "isDdl": False,
        "mysqlType": "",
        "old": [
            {
                "percent": "0.02",
                "update_time": "2021-05-26 11:39:19"
            }
        ],
        "pkNames": [
            "id"
        ],
        "sql": "",
        "sqlType": "",
        "table": "equity_ratio",
        "ts": 1622026029249,
        "type": "UPDATE"
    }
    h = generate_kafka_msg(param)
    if h["code"] == 2000:
        return True
    else:
        return False

if __name__ == '__main__':
    # pass
    # day = get_timestamp_and_previous_timestamp()
    # print(day)
    # r = add_monitor_entity(username='tester_chen',password='888888',group_name='默认分组',cgids=['3094744756'])
    # print(r)
    fake = Faker("zh_CN")
    a = fake.file_name(category="image", extension="png")
    print(a)