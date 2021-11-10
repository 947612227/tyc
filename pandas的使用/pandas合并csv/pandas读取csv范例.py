import pandas as pd

data = pd.read_csv('pd_test.csv',error_bad_lines=False,encoding='utf-8')

# print(data['uuid'])
# print(data)
# keys_with_entity = data['涉及实体字段'].tolist()
# table = data['table'].tolist()
# code = data['维度code']
# send_keys =['范围切割字段']
# dimension_name = ['维度名']
a = data.to_dict()
print(a)
# print(res[3])

