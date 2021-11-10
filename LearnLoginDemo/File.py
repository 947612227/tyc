# -*- coding: utf-8 -*-
# @Time : 2021/6/24 7:56 下午
# @Author : snnnnnn
import csv


def reg_write_csv(username, password):
    # 注册数据写入data文件
    path = 'data_login.csv'
    '''
    a+:    打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    newline=''： 去掉多余空行
    csv标准库中的writerow在写入文件时会加入’\r\n’作为换行符
    当写文件时newline=None，csv先是将’a\r\nb\r\n’写入内存，再写入文件时，universal newlines mode工作，换行符’\n’被翻译为’\r\n’；
    当写文件时newline=’’，程序写入’a\r\nb\r\n’；
    '''
    with open(path, 'a+', newline='', encoding='utf-8') as file:
        reg_write_csv = csv.writer(file)
        data_row = [username, password]
        reg_write_csv.writerow(data_row)
    print(f'这里打印出来的是啥{data_row}')


# 读取data里的数据
def read_all_data(path='data_login.csv'):
    res = {}
    with open(path, 'r', encoding='utf-8') as file:
        read = csv.reader(file)
        for row in read:
            res[row[0]] = row[1]
            # {'李三':'123456'}
            print(res)
        return res
