import datetime
import difflib
import json
import uuid

from deepdiff import DeepDiff
from requests import request

class Check(object):

    def __init__(self,url,url_no,Standard_url=False,name=False,json_data=False):
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
            self.Standard_res = request(url=Standard_url, method='get',timeout=30)

        # header = {'Authorization': 'f37ed796-41c7-45d3-b7fc-b841662fd7d1'}
        self.res = request(url=url, method='get',timeout=30)
        self.Sensitive_words()

        # print(self.res.text)

    def Sensitive_words(self):
        '''
        这个方法是检查请求里是否有,表示异常的参数
        '''
        if len(self.res.text)<10:
            print(self.res.text)
            return False

        Sensitive_list = ['"message":"Not Found"', '"code":4040', '"error_code:300000"', '"error_code:300001"',
                          '"error_code:300002"', '"error_code:300003"', '"error_code:300004"', '"error_code:300005"',
                          '"error_code:300006"', '"error_code:300007"', '"error_code:300008"', '"error_code:300009"',
                          '"error_code:300010"', '"error_code:300011"', '"error_code:300012"']
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
        diff_obj = DeepDiff(self.json_data, res_test,ignore_order=True,exclude_regex_paths = ["\['updateTimes'\]", "\['updatetime'\]"])
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

        return diff_res

        # hd = difflib.HtmlDiff()
        #
        # filename = uuid.uuid1().hex
        # report_path = f'log/{filename}'
        # if len(diff_res) == 0:  # 判断deepdiff是否发现差异项目,如果没有则认为是完全一致
        #     # with open(f'log/一致报告{filename}.html', 'w') as fo:
        #     #     fo.write(hd.make_file(new_file, old_file))
        #     #     fo.close()
        #
        #
        #     return True
        # else:
        #     if self.name:
        #         with open(f'log/{self.url_no}{self.name}差异报告.html', 'w') as fo:
        #             fo.write(hd.make_file(new_file, old_file))
        #             fo.close()
        #     else:
        #         with open(f'log/{self.url_no}差异报告.html', 'w') as fo:
        #             fo.write(hd.make_file(new_file, old_file))
        #             fo.close()
        #
        #     now = datetime.datetime.now()
        #     # print (now)
        #     otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        #
        #     if self.name:
        #         with open(f'log/420个接口预测试.txt', 'a') as f:
        #             f.write(f'{self.url_no}:{self.name}\n{otherStyleTime}:\n{self.test_url}\n{self.standard_url}\n\n')
        #     else:
        #         with open(f'log/420个接口预测试.txt', 'a') as f:
        #             f.write(f'{self.url_no}\n{otherStyleTime}:\n{self.test_url}\n{self.standard_url}\n\n')
        #
        #     return False


# 1.记录具体请求对比,每次对比存一个html
# 文件名的处理
# import uuid
# filename = uuid.uuid1().hex
#
# print(filename)
#
#
# 2.如果失败,需要记录到日志文件之中