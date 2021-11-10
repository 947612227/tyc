# 查询地址:线上线下
# 输入查询维度名称
# 显示相关信息
# 执行查询
# 生成文件,并且提供下载
#
# 发送消息

import json
from pywebio.output import *
from pywebio.input import input_group, TEXT, PASSWORD, actions, select, NUMBER,input
from pywebio.output import put_code, put_text
import jsonpath
import requests
import pandas as pd
from 学习pywebio.Monitor_singo_V1 import Monitoring_data_spyder, Data_conversion, singo_send_monitor_message

df = pd.read_csv('待处理数据.csv')

def check_code(data):
    code = int(data['code'])
    print(code)
    code_check = code in df.code.values
    if code_check==False:
        # print('code not in df.code.values')
        return ('code','该维度可能未收录')

# 以上是功能函数
# =====================
put_file('待处理数据.csv', b'hello world!', '下载维度清单')
data = input_group("监控动态数据查询:",[
    select('线上 or 测试?', ['线上', '测试'],value='测试',name='env'),
    input('请输入维度code', name='code',type=NUMBER)
    # select('请选择维度',csv_data,name='csv_data')
],validate=check_code)



if data['env']=='线上':
    obj = Monitoring_data_spyder(type=data['code'],env='10.39.222.64:20001')

else:
    obj = Monitoring_data_spyder(type=data['code'])

# print(obj.get_mainid_one())
res = (obj.Consolidate_mainid_gids())
main_id = res[0]
gid = res[1]
obj2 = Data_conversion()
entity = obj2.switch_key(gid)

#根据code查询table,这里应该增加异常处理
t = df['code']==int(data['code'])
print(f'df[t]:{df[t]}')
table = df[t]['table'].tolist()[0]
print(table)

# When ``tdata`` is list of dict
put_table([
    {"gid":gid, "main_id":main_id,"entity":entity,"table":table },
], header=["gid", "main_id","entity","table"])  # or header=[(put_markdown("*Course*"), "Course"), (put_markdown("*Score*") ,"Score")]

# 拼接发送url
if data['env']=='线上':
    send_obj= singo_send_monitor_message(ip='10.39.222.64:20001')

else:
    send_obj= singo_send_monitor_message()

send_url = send_obj.code_cgid(table,main_id)

put_link(f'消息发送链接:{send_url}',send_url)


# 废纸篓
# ==========================
# put_text(data['env'],data['csv_data'])
# df = pd.read_csv('待处理数据.csv')
# print(df.to_dict())

# ss:把csv按照行进行存储
# res_zip = []
# for i in zip(df['code'],df['name'],df['table']):
#     res_zip.append(list(i))

# print(res_zip)
# Set table header

# put_table(res_zip, header=['显示维度code', '维度名称', '维度table'])

# 显示维度code,维度名称,维度table