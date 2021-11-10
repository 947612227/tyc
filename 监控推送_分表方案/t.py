import pandas as pd

datainfo1 = pd.read_csv('维度映射表.csv',error_bad_lines=False)
# datainfo1 = pd.read_csv('压测数据文件.csv')
# print(datainfo1[datainfo1['code'] =='941'])
# a = datainfo1.loc(datainfo1['code'] =='941')
a = datainfo1[datainfo1['code']==9111]['table'].to_list()
print(a)
