import time
from 监控消息测试工具.common import add_monitor_entity
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.session import go_app, hold
from pywebio import start_server
from pywebio.output import *
from pywebio.input import input_group, TEXT, PASSWORD, actions, select, NUMBER,input
from pywebio.output import put_code, put_text
from pywebio.session import local
import pandas as pd
from 监控消息测试工具.Monitor_singo_V1 import Monitoring_data_spyder, Data_conversion, singo_send_monitor_message


# 初始化
pd.options.display.max_rows = None
df = pd.read_csv('维度映射表_backup.csv')


global_data={}

def check_code(data):
    code = int(data['code'])
    print(code)
    code_check = code in df.code.values
    if code_check==False:
        # print('code not in df.code.values')
        return ('code','该维度可能未收录')
#===================================


def index():
    put_text('设置参数')
    # put_file('待处理数据.csv','待处理数据.csv','下载维度清单')


    o = output("===============目前支持的维度列表===============")
    put_scrollable(o, height=300, keep_bottom=True)

    o.append(df)
    # while 1:
    #     o.append(time.time())
    #     time.sleep(0.5)


    data = input_group("监控动态数据查询:", [
        select('线上 or 测试?', ['线上', '测试'], value='线上', name='env'),
        input('请输入维度code', name='code', type=NUMBER)
        # select('请选择维度',csv_data,name='csv_data')
    ], validate=check_code)
    # print(f'data:{data}')
    local.X = data
    global global_data
    global_data=data
    # print(local)
    # time.sleep(1)
    go_app('task_1',new_window=False)
    # hold()


def task_1():
    global global_data
    print(global_data)
    print(f'task1:{local}')
    if global_data['env'] == '线上':
        print('进入线上逻辑')
        obj = Monitoring_data_spyder(type=global_data['code'], env='10.39.222.64:20001')

    else:
        obj = Monitoring_data_spyder(type=global_data['code'])

    # print(obj.get_mainid_one())
    res = (obj.Consolidate_mainid_gids())
    main_id = res[0]
    gid = res[1]
    print(f'main_id:{main_id},gid:{gid}')
    obj2 = Data_conversion()
    t = obj2.switch_key(gid)
    entity = t['data']
    entity_type = t['type']

    print(f'entity:{entity},entity_type:{entity_type}')

    # 根据code查询table,这里应该增加异常处理
    t = df['code'] == int(global_data['code'])
    print(f'df[t]:{df[t]}')
    table = df[t]['table'].tolist()[0]
    print(f'table内容是:{table}')

    # When ``tdata`` is list of dict
    put_table([
        {"gid": gid, "main_id": main_id, "entity": entity, "table": table},
    ], header=["gid", "main_id", "entity",
               "table"])  # or header=[(put_markdown("*Course*"), "Course"), (put_markdown("*Score*") ,"Score")]

    # 拼接发送url
    if global_data['env'] == '线上':
        send_obj = singo_send_monitor_message(ip='10.39.222.64:20001')

    else:
        send_obj = singo_send_monitor_message()

    send_url = send_obj.code_cgid(table, main_id)

    put_link(f'消息发送链接:{send_url}', send_url)

    account_data = input_group("监控账号设置:", [
        input('请输入账号', name='account_name'),
        input('请输入密码', name='account_pwd')
        # select('请选择维度',csv_data,name='csv_data')
    ])
    username = account_data['account_name']
    password = account_data['account_pwd']

    if username == '':username = '王杨'
    if password == '':password = '888888'

    gids = gid

    print(f'username:{username},password:{password},gid:{gids}')

    if entity_type == 'companyname':
        r = add_monitor_entity(username=username, password=password, group_name='默认分组', cgids=[gids])
    elif entity_type=='organization':
        r = add_monitor_entity(username=username, password=password, group_name='默认分组', brids=[gids])
    elif entity_type == 'human':
        r = add_monitor_entity(username=username, password=password, group_name='默认分组', hcgid=[gids])


    put_code(r, 'json', 15)

    # put_buttons(['发送消息'],[lambda:singo_send_monitor_message()])

    # put_link('回到首页', app='task_index')

    put_buttons(['返回首页'], [lambda: go_app('task_0',new_window=False)])
    hold()


start_server([index,task_1],port='665')