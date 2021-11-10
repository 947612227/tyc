import datetime
import difflib
import json
import uuid
from deepdiff import DeepDiff
from requests import request
from tools import feishu
# from Open_Requests_restructure.tools import feishu


class Check(object):

    def __init__(self,url,url_no,Standard_url=False,name=False,json_data=False,timeout=10):
        #如果传入json_data那么，就会读取文件到类的 实例属性
        # 如果传了name，。。。
        # Standard_url如果传了，那么init里会按照入参调用这个服务，并且记录结果（Standard_res）
        # 正常情况，init方法会把响应结果存成self.res

        # print(url_no,json_data,url)

        if json_data:
            self.json_data_path = json_data
            def read_json(path):
                with open(path, 'r') as f:
                    r = json.load(f)
                return r
            self.json_data = read_json(json_data)

        if name:
            self.name = name
        self.url_no = url_no
        self.test_url = url
        if Standard_url!=False:

            self.standard_url=Standard_url

        # header = {'Authorization': '2c344090-55c1-4253-a86d-b5c724c35654'}
            self.Standard_res = request(url=Standard_url, method='get',timeout=timeout)

        # header = {'Authorization': 'f37ed796-41c7-45d3-b7fc-b841662fd7d1'}

        # header = {"Authorization": "05ec08ec-b7c3-487c-a150-cb8ce6c02626"}#新预发测试

        header = {"Authorization": "36ded9cc-6080-4570-9f14-badd0828bf88"}#线上

        self.res = request(url=url, method='get',timeout=10,headers = header)

        self.response_time = self.res.elapsed.total_seconds()
        # self.Sensitive_words()

        print(self.res.text)

    def Sensitive_words(self):
        '''
        这个方法是检查请求里是否有,表示异常的参数
        '''
        if len(self.res.text)<10:
            print(self.res.text)
            return False

        Sensitive_list = ['"message":"Not Found"', '"code":4040', '"error_code:300000"', '"error_code":300001','"error_code":300000'
                          '"error_code":300002', '"error_code":300003', '"error_code":300004', '"error_code":300005',
                          '"error_code":300006', '"error_code":300007', '"error_code":300008', '"error_code":300009',
                          '"error_code":300010', '"error_code":300011', '"error_code":300012','无数据']
        for i in Sensitive_list:
            if i in self.res.text:
                print(f'接口{self.url_no}击中敏感词{i}')
                print(self.test_url)
                print(self.res.text)
                print('\n\n')
                return False
        # for i in Sensitive_list:
        #     if i in self.res.text:
        #         with open(res_path,'a+') as f:
        #             f.write('\n')
        #             f.write(f'{i}:,')
        #             f.write(self.url_no)
        #             f.write(',')
        #             f.write(self.res.text)
        #             f.write('\n')
        #         return False

        return True

    # def write_res(self):
    #     standard_name='标准服务.json'
    #
    #     with open(f'{test_name}', 'w') as f:
    #         f.write(f'被测服务:\n')
    #         f.write(f'请求:\n{self.res.request.url}\n')
    #         f.write(f'参数：{self.test_url}')
    #         f.write('\n')
    #         f.write('以下是报文内容:\n')
    #         f.write(json.dumps(self.res.request.body, indent=2, sort_keys=True, ensure_ascii=False))
    #         f.write('\n')
    #         f.write(json.dumps(res_test, indent=2, sort_keys=True, ensure_ascii=False))
    #         f.write('\n')
    #         f.write(f'找到的差异点是：{diff_res}')

    def diff_json(self):
        # 尝试进行json()
        try:
            res_test = self.res.json()
        except BaseException as e:
            print(f'接口：' + self.url_no +'结果json()出现异常')
            res_test = self.res
            return False
        # 对相应文件全文进行对比
        diff_obj = DeepDiff(self.json_data, res_test,ignore_order=True)
        diff_res = diff_obj.pretty()  # 对结果进行字符串转化

        # 构造结果文件
        # 构造可视化html
        test_name='json_result/' + self.url_no + '_对比结果.json'
        # standard_name='标准服务.json'

        with open(f'{test_name}', 'w') as f:
            # 打印被测服务信息
            f.write(f'被测服务:\n')
            f.write(f'请求:\n{self.res.request.url}\n')
            f.write(f'参数：{self.test_url}')
            f.write('\n\n\n')
            # 打印diff结果
            f.write(f'找到的差异点是：\n{diff_res}\n\n')
            # 打印被测接口返回json
            f.write('被测接口调用结果:\n')
            # f.write(json.dumps(self.res.request.body, indent=2, sort_keys=True, ensure_ascii=False))
            # f.write('\n')
            f.write(json.dumps(res_test, indent=2, sort_keys=True, ensure_ascii=False))
            f.write('\n')


        with open(test_name, 'r') as f:
            new_file = f.readlines()
            f.close()

        with open(self.json_data_path, 'r') as f:
            old_file = f.readlines()
            f.close()


        if len(diff_res) > 0:
            hd = difflib.HtmlDiff()

            with open(f'log/{self.url_no}差异报告.html', 'w') as fo:
                fo.write(hd.make_file(new_file,old_file))
                fo.close()

        return diff_res

    def diff_server(self):
        # 尝试进行json()
        try:
            res_test = self.res.json()
            res_Sta= self.Standard_res.json()
        except BaseException as e:
            print(f'接口：' + self.url_no + '结果json()出现异常')

            res_test = self.res
            res_Sta= self.Standard_res
            return False

        # print(res_Sta, res_test)
        # 对相应文件全文进行对比
        # diff_obj = DeepDiff(res_Sta, res_test, ignore_order=True)
        diff_obj = DeepDiff(res_Sta, res_test, ignore_order=True,exclude_regex_paths = ["\['updateTimes'\]", "\['updatetime'\]"])
        diff_res = diff_obj.pretty()  # 对结果进行字符串转化

        # 构造可视化html
        test_name='server_result/' + self.url_no + '_被测服务.json'
        standard_name='server_result/' + self.url_no + '_标准服务.json'

        with open(f'{test_name}', 'w') as f:
            #打印被测服务信息
            f.write(f'被测服务:\n')
            f.write(f'请求:\n{self.res.request.url}\n')
            f.write(f'参数：{self.test_url}')
            f.write('\n\n\n')
            #打印diff结果
            f.write(f'找到的差异点是：\n{diff_res}\n\n')
            #打印被测接口返回json
            f.write('被测接口调用结果:\n')
            # f.write(json.dumps(self.res.request.body, indent=2, sort_keys=True, ensure_ascii=False))
            # f.write('\n')
            f.write(json.dumps(res_test, indent=2, sort_keys=True, ensure_ascii=False))
            f.write('\n')



        with open(f'{standard_name}', 'w') as f:
            # 打印标准服务信息
            f.write(f'标准服务:\n')
            f.write(f'请求:\n{self.Standard_res.request.url}\n')
            f.write(f'参数：{self.standard_url}')
            f.write('\n\n\n')
            # 打印标准接口返回json
            f.write('标准接口调用结果:\n')
            # f.write(json.dumps(self.Standard_res.request.body, indent=2, sort_keys=True, ensure_ascii=False))
            # f.write('\n')
            f.write(json.dumps(res_Sta, indent=2, sort_keys=True, ensure_ascii=False))

        with open(test_name, 'r') as f:
            new_file = f.readlines()
            f.close()

        old_file = ''
        with open(standard_name, 'r') as f:
            old_file = f.readlines()
            f.close()

        if len(diff_res) > 0:
            hd = difflib.HtmlDiff()

            with open(f'log/{self.url_no}差异报告.html', 'w') as fo:
                fo.write(hd.make_file(new_file,old_file))
                fo.close()

        # return diff_res

        return len(diff_res)==0

#传入obj,obj里的检查方法名字,和入参
def retry_check(obj,func_str,*key):
    # 思路:接收一个对象名字
    # check = obj(**key)
    #
    # f1 = getattr(check, func_str)
    # res = f1()
    retry_count = 10
    flag = 0
    success_res = ''
    fail_res = ''
    response_time_list = []

    # ====================
    # 以上是变量初始化部分

    #用于处理10次时间格式的函数
    def func1(response_time_list):
        s = ''
        Cumulative = 0
        for i in response_time_list:
            Cumulative = Cumulative + i
            # print(i)
            s = s + str(i) + '\n'
        res = Cumulative / len(response_time_list)
        res = round(res,4)
        info = (f'平均时间(s):{res} \n')
        print(info)
        return info


    for i in range(retry_count):


        check = obj(*key)   #为检查方法实例重新灌入参数(相当于重新请求)
        response_obj = check.res #从check类的属性中,抽出requests响应对象
        response_time = check.response_time#从check类的属性中提取本次请求时间
        response_time_list.append(response_time)#向重试计时器添加一条计时

        check_func_obj = getattr(check, func_str)#根据入参调用一个检查函数
        res = check_func_obj()  #接受检查函数的返回值


        # ======================
        # 以上是变量定义和初始化部分
        print(f'当前第{i+1}次重试,结果为:{res}')
        if res:
            flag += 1
            success_res = response_obj
        else:
            fail_res = response_obj

    test_url, no = key
    if flag == 10:
        print(f'no:{no},重试100%成功')

    elif flag >=8:
       #获取消息需要的参数

        try:
            traceId = success_res.json()['debugInfo']['test_url']
        except :
            traceId = ' '

       #组装消息
        print(f'no:{no}')
        # info = {'res': True, 'info': f'{no}接口重试成功率大于80%.{traceId}'}
        # info = f'接口监控重试消息\nURL:{test_url}\n成功率:{flag}/{retry_count}\ntraceId:{traceId},\n{func1(response_time_list)}\n响应:{success_res.json()}\nPS:本消息为触发重试逻辑,且成功率>=80%'

        info = f'重试成功\n成功率:{flag}/{retry_count}'
        check_res = {'res': True, 'info':info}
        feishu.feishu_retry_alert(api_id=no,msg_text=info)
        return check_res #返回信息给pytest做assert
    else:
        #如果失败,取最近一次失败的
        # traceId(提取),url(有),res_json(提取),params(有),info
        try:
            print(f"失败的响应值:{fail_res.json()}")
            traceId = fail_res.json()['debugInfo']['test_url']

        except :
            traceId = ' '

        info = f'!!!重试失败\nURL:{test_url}\n成功率:{flag}/{retry_count}\ntraceId:{traceId},\n{func1(response_time_list)}\n响应:{fail_res.json()}\nPS:本消息为触发重试逻辑,且失败了大于20%!!!'
        check_res = {'res': False, 'info':info}
        feishu.feishu_retry_alert(api_id=no,msg_text=info)
        return check_res #返回信息给pytest做assert

if __name__ == '__main__':
    feishu.feishu_retry_alert(api_id=748,msg_text='text')
