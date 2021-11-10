
import pandas as pd


data = pd.read_csv('error.log',error_bad_lines=False,encoding='utf-8')
# 1.简单统计一列的次数
x = data['name'].value_counts()
print(x)


