import csv
import time
import allure
import pytest
import requests
import difflib
import json
from deepdiff import DeepDiff
from requests import request


#从csv中提取url/NO/*扩展数据
from tools.Check import Check,retry_check
from tools.send_message import send_text

def read_csv(csv_path):
    csvFile = open(csv_path, "r")
    reader = csv.reader(csvFile)
    # 组织成pytest参数化
    data_list = []
    for item in reader:
        case_no = item[0]

        url = item[1]

        temp = [case_no, url]
        data_list.append(temp)
    return data_list

# data = read_csv('./csv_data/k1.csv')
# data = read_csv('./csv_data/全示例回归.csv')
data = read_csv('./csv_data/线上暴露接口.csv')
del data[0]#去除表头
# print(data)

@pytest.mark.parametrize('No,url',data)
def test_reverse(No,url):
    test_res = False

    # 测试ip
    # test_ip = 'http://10.2.16.79:20064'#测试地址
    # test_ip = 'http://10.39.221.209:20064' #预发环境
    # test_ip = 'http://open.api.tianyancha.com'
    ip = 'http://open.api.tianyancha.com'

    debug = '&debug=true'#增加调试信息


    Test_url = ip + url + debug

    print(f'{No}')

    # time.sleep(1)

    #重试一次
    try:
        check = Check(Test_url,No)
        if check.Sensitive_words():
            assert check.Sensitive_words()
        else:
            res_dic = retry_check(Check, 'Sensitive_words', Test_url, No)
            test_res = res_dic['res']
            # print(f'重试结果是:{res_dic}')
            allure.attach(test_res, "接口响应：")
            assert test_res
    except BaseException as e:
        info = f'case遇到异常:{e}\n{No}:{Test_url}'
        bot = '6fbd7c64-f0ee-4397-8ff1-e1470529b991'
        #
        # # 1.发送普通文本消息

        send_text(info, bot)
        assert False


l2 = [
    [1063,'/services/open/m/bids/search?publishEndTime=2020-01-01&searchType=1,2&pageSize=20&keyword=百度&publishStartTime=2010-01-01&pageNum=1'],
    [1062,'/services/open/ipr/patents/search?searchType=1,2,3&pubDateBegin=2010-01-01&appDateBegin=2010-01-01&pageSize=20&pubDateEnd=2020-01-01&appDateEnd=2020-01-01&keyword=百度&pageNum=1&patentType=1'],
    [1061,'/services/open/ipr/tm/search?searchType=1,2&appDateBegin=2010-01-01&pageSize=20&tmClass=1&appDateEnd=2020-01-01&keyword=百度&pageNum=1&status=1'],
    [943,'/services/open/ps/news/2.0?name=北京百度网讯科技有限公司&pageSize=20&startTime=20191020&id=22822&endTime=20191022&pageNum=1&tags=债务抵押,经营业务']
 ]

@pytest.mark.parametrize('No,url',l2)
def test_exception(No,url):
    test_res = False

    # 测试ip

    ip = 'http://open.api.tianyancha.com'
    # ip = 'http://10.39.222.108:20064'
    # ip = 'http://open.api.test.tianyancha.com'
    # ip = 'http://open.api.pre.tianyancha.com'
    debug = '&debug=true'#增加调试信息

    Test_url = ip + url + debug

    print(f'{No}')

    # time.sleep(1)


    try:
        check = Check(Test_url,No)
        if check.Sensitive_words():
            assert check.Sensitive_words()
        else:
            print('进入else')
            res_dic = retry_check(Check, 'Sensitive_words', Test_url, No)
            test_res = res_dic['res']

            allure.attach(test_res, "接口响应：")
            # print(f'重试结果是:{res_dic}')
            assert test_res
    except BaseException as e:
        info = f'case遇到异常:{e}\n{No}:{Test_url}'
        bot = '6fbd7c64-f0ee-4397-8ff1-e1470529b991'
        #
        # # 1.发送普通文本消息

        send_text(info, bot)
        assert False

        #1034/1035是报告接口不涉及


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_v2.py'])
