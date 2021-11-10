import csv
import pytest
#读取数据函数
from send_check import send_check
from Check import Check


def read_csv(csv_path):     #读取csv文件
    csvFile = open(csv_path, "r")
    reader = csv.reader(csvFile)
    # 组织成pytest参数化
    data_list = []
    for item in reader:
        case_no = item[0]
        url = item[1]
        name = item[2]

        temp = [case_no, url, name]
        data_list.append(temp)
    return data_list


def get_url(url):       #获取url
    # ip = "http://10.2.128.196:20064/"   #测试环境
    ip = 'http://10.39.222.108:20064'  # 阿里云测试环境
    # ip = "http://10.39.222.35:20064/"  #预发环境域名
    # ip = "http://open.api.tianyancha.com/"  #线上环境域名

    url = ip + url   #拼接域名
    return url

data_list = read_csv('./test_api/testV1.csv')
# data_list = read_csv('./test_api/areacode.csv')
# data_list = read_csv('./test_api/id_api.csv')

# @pytest.mark.parametrize('data,',data_list)
# def test_json_save(data, json_file_path='json_file/'):     #接口调用返回json保存
#     no = data[0]  # 接口id
#     url = data[1]  # 接口地址
#     json_name = data[2]  # 接口数据文件名称
#
#     print(f'接口{no}开始进行')
#     url = get_url(url)
#     result = send_check(url, no, f'{json_file_path}{json_name}.json')       #调用保存json函数
#
#     assert result


# @pytest.mark.parametrize('data,',data_list)
# def test_json_diff(data, json_file_path='areacode/'):     #接口调用返回内容 与json文件进行对比
#     no = data[0]  # 接口id
#     url = data[1]  # 接口地址
#     json_name = data[2]  # 接口数据文件名称
#
#     url = get_url(url)
#     print(f'\n被测服务url：{url}')
#
#     check = Check(url=url, url_no=json_name, json_data=f'{json_file_path}{json_name}.json')
#     diff_res = check.diff_json()
#     print(f'差异点是:{diff_res}')
#
#     assert diff_res== ''


@pytest.mark.parametrize('data,',data_list)
def test_json_server(data):
    no = data[0]  # 接口id
    url = data[1]  # 接口地址
    json_name = no + data[2]  # 接口数据文件名称

    print(f'接口{no}开始进行')
    url1 = get_url(url)  # 获取接口url
    url2 = 'http://open.api.tianyancha.com' + url  # 标准服务url

    print(f'被测服务url：{url1}')
    print(f'标准服务url：{url2}')
    # 接口调用结果 与 标准服务调用结果进行对比
    check = Check(url=url1, url_no=json_name, Standard_url=url2)
    diff_res = check.diff_server()
    print(f'差异点是:{diff_res}')

    assert diff_res==''



# @pytest.mark.parametrize('data,',data_list)
# def test_url_json(data):
#     print(data)
#     # res = json_server(data,rich_data_path='./csv/api_data/')
#     res = json_diff(data)
#     # print (f'执行结果{res}')
#     # assert res
#     pytest.assume(res)

# @pytest.mark.parametrize('data,',data_list)
# def test_url_json(data):
#     print(data)
#     dir = os.getcwd()
#     print('8'*30)
#     print(dir)
#     res = json_diff(data,rich_data_path='./csv/api_data/',)
#     # print (f'执行结果{res}')
#     assert res



if __name__ == '__main__':
    pytest.main(['-v','-s','--html=report.html','--self-contained-html'])

    # 'pytest -n auto --html=report.html --self-contained-html test_case.py'