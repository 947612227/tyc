import json
import csv
from urllib.parse import parse_qs, urlparse
from urllib.parse import urlencode
from urllib.parse import unquote
#读取数据函数
from Check import Check
from send_check import send_check


def read_csv(csv_path):     #读取csv文件
    csvFile = open(csv_path, "r")
    reader = csv.reader(csvFile)
    # 组织成pytest参数化
    data_list = []
    for item in reader:
        case_no = item[0]
        url = item[1]
        data_name = item[2]

        temp = [case_no, url, data_name]
        data_list.append(temp)
    return data_list


def read_csv_dic(csv_path):     #读取csv文件到字典
    csvFile = open(csv_path, "r")
    reader = csv.DictReader(csvFile)
    data_dic_list = []

    for i in reader:
        # print(i)
        data_dic_list.append(i)
    return data_dic_list


def replace_url(url,dic):       #替换url中参数
    o = urlparse(url)
    query = parse_qs(o.query)

    # 解析并替换参数
    for key in dic:
        query[key]=dic[key]

    new_query = urlencode(query, doseq=True)
    url =o.path + '?' + new_query   #拼接url，接口地址+参数
    # print(new_query)
    # print(url)
    return url, new_query

def get_url(url):       #获取url
    # ip = "http://10.2.128.196:20064/"   #测试环境
    # ip = 'http://10.39.222.108:20064/'  # 阿里云测试环境
    # ip = "http://10.39.222.35:20064/"  #预发环境域名
    ip = "http://open.api.tianyancha.com/"  #线上环境域名

    url = ip + url   #拼接域名
    return url


#读取json文件
# def read_json(json_name, json_path = 'json/'):
#     path = json_path + json_name + '.json'
#     # print(path)
#     with open(path,'r') as f:
#         r = json.load(f)
#         # print(r)
#     return r


def json_diff(data,rich_data_path='csv/api_data/', json_file_path='json_file/'):     #接口调用返回内容 与json文件进行对比
    # 读取接口数据
    no = data[0]  # 接口id
    url = data[1]  # 接口地址
    csv_name = data[2]  # 接口数据文件名称
    print(f'接口{no}开始进行')
    if csv_name == '':      #无需替换参数时
        url = get_url(url)
        #接口返回结果 与 json文件进行对比
        check = Check(url=url, url_no=no, json_data=f'{json_file_path}{no}.json')
        diff_res = len(check.diff_json())#构造用于检查的返回值
        print(f'差异点是:{diff_res}')

        return diff_res == 0
    else:       #多参数替换
        csv_path = rich_data_path + csv_name  # 拼接接口数据文件地址
        data_dic_list = read_csv_dic(csv_path)  # 读取数据文件到字典

        # 循环接口数据
        for data_dic in data_dic_list:
            # 获取url
            url,json_name = replace_url(url, data_dic)
            url = get_url(url)

            # 拼接json文件地址
            json_name = no + '+' + unquote(json_name)  # json文件名称
            json_path = json_file_path + json_name + '.json'  # 文件地址
            # print(json_path)

            #接口返回结果 与 json文件进行对比
            check = Check(url=url, url_no=json_name, json_data=json_path)
            diff_res = len(check.diff_json())
            # assert  len(check.diff_json()) == 0
            print(f'差异点是:{check.diff_json()}')
            return diff_res == 0


def json_save(data,rich_data_path='csv/api_data/', json_file_path='json_file/'):     #接口调用返回json保存
    no = data[0]  # 接口id
    url = data[1]  # 接口地址
    csv_name = data[2]  # 接口数据文件名称

    print(f'接口{no}开始进行')
    if csv_name == '':      #无需替换参数时
        url = get_url(url)
        send_check(url, no, f'{json_file_path}{no}.json')       #调用保存json函数
    else:       #多参数替换
        csv_path = rich_data_path + csv_name  # 拼接接口数据文件地址
        data_dic_list = read_csv_dic(csv_path)  # 读取数据文件到字典

        # 循环接口数据
        for data_dic in data_dic_list:
            # 获取url
            url,json_name = replace_url(url, data_dic)
            url = get_url(url)

            # 拼接json文件地址
            json_name = no + '+' + unquote(json_name)  # json文件名称
            json_path = json_file_path + json_name + '.json'  # 文件地址

            send_check(url, json_name, json_path)   #保存接口返回到json文件


def json_server(data,rich_data_path='csv/api_data/'):
    no = data[0]  # 接口id
    url = data[1]  # 接口地址
    csv_name = data[2]  # 接口数据文件名称

    print(f'接口{no}开始进行')
    if csv_name == '':      #无需替换参数时
        url1 = get_url(url)     #获取接口url
        url2 = 'http://open.api.tianyancha.com/' + url      #标准服务url
        # 接口调用结果 与 标准服务调用结果进行对比
        check = Check(url=url1, url_no=no, Standard_url=url2)
        return check.diff_server()
    else:       #多参数替换
        csv_path = rich_data_path + csv_name  # 拼接接口数据文件地址
        data_dic_list = read_csv_dic(csv_path)  # 读取数据文件到字典

        # 循环接口数据
        for data_dic in data_dic_list:
            url, json_name = replace_url(url, data_dic)  # 获取url

            url1 = get_url(url)     #获取接口url
            url2 = 'http://open.api.tianyancha.com/' + url      #标准服务url

            # 拼接json文件地址
            json_name = no + '+' + unquote(json_name)  # json文件名称
            # unquote(json_name)
            # print(unquote(json_name))
            # 接口调用结果 与 标准服务调用结果进行对比
            check = Check(url=url1, url_no=json_name, Standard_url=url2)
            res = check.diff_server()
            return res

def loop():
    # data = read_csv('csv/api_address.csv')
    # data = read_csv('csv/经过筛选的接口结构.csv')
    data = read_csv('csv/areacode.csv')
    # data = read_csv('csv/接口-全成功.csv')
    for data1 in data:
        # res = json_save(data1)      #保存json
        # res = json_diff(data1)      #与json文件对比
        res = json_server(data1)      #与标准服务对比
        print(res)


if __name__ == '__main__':
    loop()