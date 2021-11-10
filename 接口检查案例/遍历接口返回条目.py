# 宋佳
import time
import requests

def get_timestamp(starttime,endtime): #获取起止时间对应时间戳
    # 计算开始时间对应时间戳
    t =time.strptime(starttime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(t))
    starttime = int(round(timeStamp * 1000))
    # 计算结束时间对应时间戳
    t = time.strptime(endtime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(t))
    endtime = int(round(timeStamp * 1000))

    return starttime,endtime

def get_a(starttime,endtime,pagesize,pizenum): #调用接口并返回json数据
    starttime,endtime = get_timestamp(starttime,endtime) #调用-获取起止时间对应时间戳
    # print(starttime,endtime)

    #处理url
    url = 'http://10.39.222.64:20001/event/page.json'
    dimension = '9371'
    url = url + '?dims=' + dimension + '&eventStartTime=' + str(starttime) + '&eventEndTime=' + str(endtime) + '&ps=' + str(pagesize) + '&pn=' + str(pizenum)
    # url = 'http://10.39.222.64:20001/event/page.json?dims=3802&eventStartTime=1616565351000&eventEndTime=1624334726475'
    # print(url)

    r = requests.get(url = url).json() #调用接口获取返回json
    return r

def get_page_num(r,pagesize): #计算总页数
    total = r.get("data").get("total") #获取查询数据总条数
    # ps = r.get("data").get("ps")
    #print(total,type(total))

    #计算数据页数
    pnum = int(total/pagesize)
    if total%pagesize != 0:
        pnum +=1

    # print(pnum)
    return pnum

def get_assertions(res): #断言-当前仅打印
    res1 = res.get("data").get("items")
    for i in res1:
        print("gid:" + i.get("gids") + ",title:" + i.get("title"))

def get_cycle_a(starttime,endtime,pagesize): #遍历所有条目
    res = get_a(starttime,endtime,pagesize,1)  #调用-获取接口返回json
    pnum = get_page_num(res,pagesize) #调用-利用json计算数据展示页数

    for i in range(pnum): #循环遍历所有数据页
        i +=1
        res = get_a(starttime,endtime,pagesize,i)
        # print(res)
        get_assertions(res) #调用-进行断言



if __name__ == '__main__':

    starttime = '2021-06-20 00:00:00' #开始时间
    endtime = '2021-06-24 00:00:00' #结束时间
    pagesize = 10 #每页展示条数

    get_cycle_a(starttime,endtime,pagesize) #调用遍历所有条目

