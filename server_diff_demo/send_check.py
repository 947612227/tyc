from requests import request
import json

def send_check(url,No, path): #保存接口返回json
    # 发送请求
    # header = {'Authorization': '1b43717e-2342-401d-a8ef-326f0a613f0e'}#线上包天
    # res = request(url=url,method='get',headers =header)

    res = request(url=url, method='get')
    if len(res.text)==0:return False
    # print(res.text)
    # 采取暴力方式,只要相应结果:
        # 为空/还有300000/无数据/系统异常.就认为失败
    # Sensitive_list=['300000','300001','系统异常','无数据','4000','5000','2000']
    # Sensitive_list=['"message":"Not Found"','"code":4040','"error_code:300000"','"error_code:300001"',
    #                       '"error_code:300002"','"error_code:300003"','"error_code:300004"','"error_code:300005"',
    #                       '"error_code:300006"','"error_code:300007"','"error_code:300008"','"error_code:300009"',
    #                       '"error_code:300010"','"error_code:300011"','"error_code:300012"']
    Sensitive_list = ['"message":"Not Found"','"code":4040']
    for i in Sensitive_list:
        if i in res.text:
            print(f'接口{No}击中敏感词{i}')
            print(url)
            print(res.text)
            print('\n\n')
            # with open('批量更新/更新失败.txt','a+') as f:
            #     f.write(f'接口{No},')
            #     f.write(f'击中敏感词{i}:')
            #     f.write(url)
            #     f.write(res.text)
            #     f.write('\n')
            return False

    # path = '批量更新/'+No+'_'+'.json'

    try:
        data=res.json()
        # print(data)
        with open(path, 'w+') as f:
            f.write(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))

    except Exception as e:

        print(f'遇到解析异常:{e}')

    return True
