# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:50:20 2020

"""

import pandas as pd
datainfo1 = pd.read_csv('全示例回归.csv',error_bad_lines=False)
# datainfo1 = pd.read_csv('压测数据文件.csv')
datainfo1['id'] = datainfo1['id'].astype('str')

ort = pd.read_csv('id.csv',error_bad_lines=False)
ort['id'] = ort['id'].astype('str')
# print(ort)

outer = pd.merge(right=ort, left=datainfo1, on='id',how='right')
# print(outer)

outer.to_csv(r'testV1.csv', index=False, encoding='utf-8')