# import requests
#
# _host = "http://open.api.tianyancha.com/services/v4/open/latest?categoryGuobiao=L&pageSize=20&time=2018-09-25&pageNum=1&base=北京"
# # _host = "http://10.39.222.35:20064/services"
# _header = {"Authorization": "36ded9cc-6080-4570-9f14-badd0828bf88"}
#
# A = requests.get(url = _host,headers = _header)
# print(A.json())


#coding=utf-8
import sys
test = [1,0,1,0]
def fan_(x):
    for i in range(len(x)):
        x[i],x[len(x)-i] = x[len(x)-i],x[i]
    return x
print(fan_(test))