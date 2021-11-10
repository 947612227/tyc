# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:50:20 2020

"""

import pandas as pd
datainfo1 = pd.read_csv('res.csv',error_bad_lines=False)

datainfo2 = pd.read_csv('线上暴露接口.csv',error_bad_lines=False)

datainfo1 = datainfo1.append(datainfo2)
datainfo1 = datainfo1.append(datainfo2)
res = datainfo1.drop_duplicates(subset=['id'],keep=False)

res.to_csv(r'差集2.csv', index=False, encoding='utf-8')