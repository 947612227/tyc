#coding=utf-8
import sys 
#str = input()
#print(str)
a = [[1,1,0],[1,0,1],[0,0,0]]
b = []
for i in a:
    b.append([1 - value for value in i[::-1]])
print(b)
