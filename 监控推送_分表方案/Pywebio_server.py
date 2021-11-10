import time
import pywebio
from common import add_monitor_entity
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
from Monitor_singo_V1 import Monitoring_data_spyder, Data_conversion, \
    send_monitor_message_V2, send_monitor_message_by_main_id

# 1.查询消息
#     1.1使用最近消息接口
#     1.2使用SQL查询
# 2.根据维度code找到对应的table
# 3.组装table和main_id发送消息
#     3.1发送单条
#     3.2发送选中条
#     3.3发送全部

# 初始化
from env import test_ip, online_ip

pd.options.display.max_rows = None
df = pd.read_csv('维度映射表.csv')


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
        input('请输入维度code', name='code', type=NUMBER)
        # select('请选择维度',csv_data,name='csv_data')
    ], validate=check_code)
    # print(f'data:{data}')
    local.X = data  #是否可以删掉?
    global global_data
    global_data=data
    global_data['table'] =df[df['code']==data['code']]['table'].to_list()[0]
    print(f'global_data:{global_data}')


    # print(local)
    # time.sleep(1)
    go_app('task_1',new_window=False)
    # hold()


def task_1():
    put_text('监控设置缺省参数为:1619343813自动化用户/888888/测试分组1')
    put_text('默认展示该维度线上的前10条数据,点击"提交"自动加监控实体')

    global global_data
    print(f'global_data:{global_data}')
    print(f'task1:{local}')

    # 根据index页面传入的dim_code,初始化查询函数
    obj = Monitoring_data_spyder(type=global_data['code'], env=online_ip)

    # 根据index页面传入的dim_code,查询对应的tables

    # print(obj.get_mainid_one())

    res = obj.N_Consolidate_mainid_gids()
    print(f'获取到的N_Consolidate_mainid_gids:{res}')
    
    data_list = []
    #循环存储信息
    for i in res:
        gid = i['gid']
        main_id = i['main_id']
        uhash = i['uhash']
        # 转换实体
        obj2 = Data_conversion()
        t = obj2.switch_key(gid)
        print(f't:{t}')
        entity = t['data']
        entity_type = t['type']
        print(f'entity:{entity},entity_type:{entity_type}')
        data_list.append({'gid':gid,'main_id':main_id,'uhash':uhash,'entity':entity,'entity_type':entity_type})


    # 展示数据
    # put_table([
    #     {"gid": gid, "main_id": main_id, "entity": entity, },
    # ], header=["gid", "main_id", "entity",
    #            "table"])  # or header=[(put_markdown("*Course*"), "Course"), (put_markdown("*Score*") ,"Score")]
    #
    put_table(data_list, header=["gid", "main_id","uhash", "entity","entity_type",
               ])
    # pywebio.input.checkbox(label='1',options=['1'])
    # # 拼接发送url


    #

    account_data = input_group("监控账号设置:", [
        input('请输入账号', name='account_name'),
        input('请输入密码', name='account_pwd'),
        input('请输入分组名', name='account_group')
    ])
    username = account_data['account_name']
    password = account_data['account_pwd']
    group_name = account_data['account_group']

    if username == '':username = '1619343813自动化用户'
    if password == '':password = '888888'
    if group_name == '': group_name = '测试分组1'
    #

    # 批量添加实体
    main_ids = []


    import time

    #进度条初始化
    put_processbar('bar');
    #进度条标识
    flag = 0
    # set_processbar('bar', 1 / len(data_list))
    for i in data_list:

        gids = i["gid"]
        entity_type = i['entity_type']
        main_ids.append(i['main_id'])
        print(f'username:{username},password:{password},gid:{gids}')
    #
        if entity_type == 'companyname':
            r = add_monitor_entity(username=username, password=password, group_name=group_name, cgids=[gids])
        elif entity_type=='organization':
            r = add_monitor_entity(username=username, password=password, group_name=group_name, brids=[gids])
        elif entity_type == 'human':
            r = add_monitor_entity(username=username, password=password, group_name=group_name, hcgid=[gids])
        print(f'添加实体结果:{r}')
        flag = flag + 1
        set_processbar('bar', flag / len(data_list))
        time.sleep(0.1)

    put_code(r, 'json', 15)

    # put_buttons(['发送消息'],[lambda:send_monitor_message_V2(uhash=uhashs)])
    print(f'table:{global_data["table"]},main_ids:{main_ids}')
    put_buttons(['发送消息'], [lambda: send_monitor_message_by_main_id(table=global_data['table'],main_id=main_ids)])

    #
    # put_link('回到首页', app='task_index')
    #
    put_buttons(['返回首页'], [lambda: go_app('task_0',new_window=False)])
    hold()


start_server([index,task_1],port = '665')

# 行政许可维度的发送请求有bug