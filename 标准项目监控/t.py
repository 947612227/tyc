#coding=utf-8
a_list = [[1,1,0],[1,0,1],[0,0,0]]

b_list = []
for i in a_list:
    i.reverse()
    for j in i:
        if j == 0:
            j = 1
        elif j == 1:
            j = 0
    b_list.append(i)
print(b_list)