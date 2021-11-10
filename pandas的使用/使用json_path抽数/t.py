import json

import jsonpath
import pandas as pd

# df = pd.read_json('ttt.json')
#
# print(df.to_string())


with open('t.json','r') as data_json:
    data_json1 = json.load(data_json)
    # print(data_json1)
    gids_value = jsonpath.jsonpath(data_json1, f'$.interfaces..[fId')

print(gids_value)

for i in gids_value:
    with open('../两个表的差/res.csv', 'a')as f:
        f.write(f'{i}\n')