import json

from pywebio import start_server
from pywebio.output import *
from pywebio.input import input_group, TEXT, PASSWORD, actions, select, NUMBER, checkbox
from pywebio.output import put_code, put_text
import jsonpath
import requests
import pandas as pd

# df = pd.read_csv('待处理数据.csv')
# print(df.code.values)
# print(999 in df.code.values)
#
# def check_code(code):
#     code = int(code)
#     return code in df.code.values
# import pandas as pd
#
# df1 = pd.DataFrame([[1, 1000, 23241], [1111, 2, 4], [5, 23, 25]], columns=['a', 'b', 'c'])
# list1 = [1, 5]
# df2 = df1[df1['a'].isin(list1)]
# df3 = df1[~df1['a'].isin(list1)]
# print('*'*30)
# print(df2)
# print('*'*30)
# print(df3)a

# df = pd.read_csv('待处理数据.csv')
# # a = df['code']==1102
# pd.options.display.max_rows = None
#
# print(pd.DataFrame(df))
# a = df[a]
# print(a)
#
# table = a['table']
# print(table.tolist())
# from pywebio.session import go_app, hold
#
# from pywebio.session import local
# def task_1():
#     put_text('task_1')
#     put_buttons(['Go task 2'], [lambda: go_app('task_2')])
#     hold()
#
# def task_2():
#     put_text('task_2')
#     put_buttons(['Go task 1'], [lambda: go_app('task_1')])
#     hold()
#
# def index():
#     put_link('Go task 1', app='task_1')  #  使用app参数指定任务名
#     put_link('Go task 2', app='task_2')
#
# # 等价于 start_server({'index': index, 'task_1': task_1, 'task_2': task_2})
# start_server([index, task_1, task_2],port='665')


# checkbox('ttt',['s1','s2'])

# t = {"code":2000,"state":"ok","message":None,"data":{"GongshangChangeService":1}}
# d ={'a':10}
# put_code(t,'json',30)
# put_table('表格输出',t)

# input('Input your age',value='2222')

# pywebio.session.hold()

d = {'a':111,'b':222}
c,d = d
print(type(c))