# 关于可变入参
import requests


def temp(first,**kwargs):
    print(kwargs)
#
# # 用法1
# temp(first = 5, second = 100,three = 1000)
#
# # 用法2
# my_dict = {"name":"wangyuanwai","age":32}
#
# temp(**my_dict)

# # 关于反射
# class A():
#     def __init__(self,**kwargs):
#         print(kwargs)
#     def func1(self):
#         print('进入func1逻辑')
#
# obj = A(first = 5, second = 100,three = 1000)
# f1 = getattr(obj,'func1')
# f1()



# def retry_check(obj,func_str,*kwargs):
#     pass
#
# retry_check(1,2,3,4,4,4)

# 关于示例重新初始化
# class A():
#     def __init__(self,**kwargs):
#         print(kwargs)
#     def func1(self):
#         print('进入func1逻辑')
#
# obj = A(first = 5, second = 100,three = 1000)
#
# obj = A(first = 9, second = 100)


def feishu_retry_alert(api_id,msg_text):#调用曌哥写好的接口

    feishu_req = requests.post(
        # url='http://alarm.tyc.local/alarm/api',  # 大群报警
        # url = 'http://alarm.test.tyc.io/alarm/api'
        url='http://10.2.128.184:10031/alarm/api',  # 小范围报警（王杨/刘淼的小群）,测试群组
        json={
            "apiId": api_id,
            "text":
                msg_text,

            "level": "L3"
        },
        headers={
            "Content-Type": "application/json"
        })
    print(feishu_req.json())

feishu_retry_alert('1011','测试数据')