import pandas as pd

def screen_A():
    #功能
    # 1.读取爬虫结果
    # 2.如果该行包含?,则认为数据ok,并且写文件
    #     2.1否则,把该行记录到有问题的接口数据中
    file =  open('线上接口示例20210715.csv','r')

    for i in file.readlines():
        if '?'  in i:
            with open('经过筛选的接口结构.csv','a')as f:
                f.write(i)
        else:
            with open('缺结构的接口.csv', 'a')as f:
                f.write(i)

def screen_B():
    # 筛选数据文件里,为"空", ,的
    file = open('压测数据文件.csv', 'r')
    for i in file.readlines():
        t = [' ','空','无']

        if ' ' not in i or '空' or '无':
            with open('经过筛选的接口结构.csv','a')as f:
                f.write(i)
        else:
            with open('缺结构的接口.csv', 'a')as f:
                f.write(i)

screen_A()


# df = pd.read_csv('压测数据文件.csv',encoding='utf-8')
# # res = df[df["case" '空']]
# df['case']=df['case'].fillna(0)
#
# res = df[ df['case'].str.contains('空|0|无|null')]
# print(res)