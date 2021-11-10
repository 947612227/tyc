from time import sleep
import requests
import logging
from logging import handlers
from urllib import parse
import json
import re

class BaseApi:
    # 测试域名
    _host = ""
    # 接口地址
    _url = ""
    # 接口参数
    _params = {}
    # 接口头信息
    _header = {}
    # 接口名称
    _api_name = ""
    # 日志路径
    _file_path = ""
    # 默认请求超时时间
    _default_timeout = 5
    #使用正则获取接口id
    # _api_id = searchObj = re.search(r'\d+\.?\d*', _api_name).group(0)


    # 封装log日志
    def log_error_statistics(self, content):
        # 实例化记录器，命名刘淼，设置记录日志级别为DEBUG
        logger = logging.getLogger("王杨")
        logger.setLevel(level=logging.INFO)


        formatter = logging.Formatter(
            fmt='%(asctime)s,%(levelname)s,%(message)s', datefmt='%Y%m%d%H%M%S'
        )

        # 实例化处理器，用于输出到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # 实例化处理器，用于输出到文件
        # _file_path = ""
        _file_path = '/home/work/wangyang/res/log_error_statistics_test.log'
        file_handler = logging.FileHandler(_file_path)
        file_handler.setFormatter(formatter)

        # 实例化分割器，用于分割日志文件
        time_file_handler = handlers.TimedRotatingFileHandler(
            filename=_file_path,
            when='D',
            interval=1,
            backupCount=2
        )
        time_file_handler.setFormatter(formatter)
        logger.addHandler(time_file_handler)

        # 需要输出的日志内容
        logger.info(content)
        logger.handlers.clear()

    # 封装发送接口请求
    # def api_send(self):
    #     try:
    #         r = requests.get(
    #             url=self._host + self._url,
    #             params=self._params,
    #             headers=self._header,
    #             # timeout=10
    #         )
    #         return r.json()
    #     except Exception as e:
    #         if 'Read timed out' in str(e):
    #             self.log_output(self._api_name + '：请求超时')
    #             # todo：增加return r = {'error_code': 500}
    #         else:
    #             self.log_output(e)

    # def feishu_retry_alert(self, msg_text):
    #     # 用于重试场景下,想飞书发送消息
    #     # 暂时只接受一个text文本内容
    #     # web_hook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/b2b2106c-64f3-4f44-bcf2-4fac2adcac0c"#内测消息群
    #     web_hook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/cee761e0-6b20-428b-aec5-c0913d2291d9"#B端L3
    #     data = {
    #         "msg_type": "text",
    #         "content": {
    #             "text": msg_text
    #         }
    #     }
    #     requests.post(url=web_hook_url, data=json.dumps(data))

    def feishu_retry_alert(self,msg_text):

        _api_id = searchObj = re.search(r'\d+\.?\d*', self._api_name).group(0)
        feishu_req = requests.post(
            # url='http://alarm.tyc.local/alarm/api',  # 大群报警
            # url = 'http://alarm.test.tyc.io/alarm/api',
            url='http://10.2.128.184:10031/alarm/api',  # 小范围报警（王杨/刘淼的小群）,测试群组
            json={
                "apiId": _api_id,
                "text":
                    msg_text,

                "level": "L3",
            },
            headers={
                "Content-Type": "application/json"
            })
        print(feishu_req.json())



    # 封装失败接口请求10次
    def api_send(self):
        # res列表，存放10次请求结果的error_code值
        res = []
        response_time_list = []
        try:
            r = requests.get(
                url=self._host + self._url,
                params=self._params,
                headers=self._header,
                timeout=self._default_timeout
            )

            #用于验证日志器
            # log_info = f'{self._api_name},进入测试'
            # self.log_error_statistics(log_info)

            # def judge_status():#判断接口是否可以调通

            # 状态码不等于0，进入10次循环
            # if r.json()['error_code'] != 0:  # 这个条件需要优化,扩大范围.目标是所有非正常情况
            # if '"error_code":mock失败触发消息' not in r.text:  # 这个条件需要优化,扩大范围.目标是所有非正常情况
            if '"error_code":0' not in r.text:#这个条件需要优化,扩大范围.目标是所有非正常情况
                for i in range(10):
                    sleep(1)
                    r_ten = requests.get(url=self._host + self._url, params=self._params, headers=self._header,timeout=self._default_timeout)
                    res.append(r_ten.json()['error_code'])
                    response_time = r_ten.elapsed.total_seconds()
                    response_time_list.append(response_time)
                    #这里要增加写入文件

                    info = (f'当前接口:{self._api_name}\n{self._host + self._url},\n正在进行第{i+1}次重试,\n本次响应时间:{response_time}')
                    print(info)
                    #这里发送消息
                    # self.feishu_retry_alert(info)
                    # 更换发大群的函数

                print(res)
                # res列表结果中，状态码0的次数大于8，返回自己构造的成功代码
                if res.count(0) == 10:
                    info = f'\n接口:{self._api_name}\n重试100%通过'
                    # self.feishu_retry_alert(info)
                    print(info)

                #这里需要优化,目标是体现重试程度
                elif res.count(0) >= 8:#只有正常的情况才会计入res变量中,所有count即可
                    ok_json = {'error_code': 0}

                    def func1(response_time_list):
                        s = ''
                        Cumulative = 0
                        for i in response_time_list:
                            Cumulative = Cumulative + i
                            # print(i)
                            s = s + str(i) + '\n'

                        # info = (f'平均时间(s):{Cumulative / len(response_time_list)} \n每次调用时间(s):\n{s}')#20210815
                        info = (f'平均时间(s):{Cumulative / len(response_time_list)} \n')#20210815

                        print(info)
                        return info

                    #在这里组织重试消息
                    # info = f'接口监控重试报警\n接口:{self._api_name}\n{self._host + self._url},\n成功率:{res.count(0)}/10,\nresponse_time_list(单位:秒):\n{response_time_list}'
                    # info = f'接口监控重试消息\n接口:{self._api_name}\n{self._host + self._url},\n成功率:{res.count(0)}/10,\n{func1(response_time_list)}\nPS:本消息为触发重试逻辑,且成功率>=80%'
                    info = f'\n接口:{self._api_name}\n{self._host + self._url},通过重试\n成功率:{res.count(0)}/10'


                    #增加重试N次响应时间

                    #这里发送消息
                    self.feishu_retry_alert(info)

                    return ok_json
                else:
                    # 10次请求依然不成功，返回失败json
                    log_info = f'{self._api_name},重试成功率小于80%'
                    self.log_error_statistics(log_info)

                    # info = f'!!!失败报警!!!\n接口重试失败!!!\n接口:{self._api_name}\n{self._host + self._url},\n成功率:{res.count(0)}/10'
                    info = f'!!!失败报警!!!\n接口重试失败!!!\n接口:{self._api_name}\n{self._host + self._url},\n成功率:{res.count(0)}/10\nPS:成功率小于80%'
                    self.feishu_retry_alert(info)
                    return r.json()
            else:#这里是,一次调用成功的情况
                print(res)
                return r.json()
        except Exception as e:
            #这里如何进行消息输出?解答:写日志,feishu_alert()通过日志发送消息
            print('*' * 30)
            print(str(e))
            print('*' * 30)
            print('timed out' in str(e))
            print(str(e))

            if 'timed out' in str(e):
                log_info = f'{self._api_name},请求超时(5s)或其他异常'
                res_t = []
                response_time_list_t = []
                for i in range(10):
                    try:
                        r = requests.get(
                            url=self._host + self._url,
                            params=self._params,
                            headers=self._header,
                            timeout=self._default_timeout
                        )

                        res_t.append(r.json()['error_code'])
                        response_time = r.elapsed.total_seconds()
                        response_time_list_t.append(response_time)
                    except BaseException as e:
                        print(e)
                if res.count(0) >=8:
                    info = f'\n接口:{self._api_name}\n重试通过'
                    # self.feishu_retry_alert(info)
                    print(info)
                else:
                    # 10次请求依然不成功，返回失败json
                    log_info = f'{self._api_name},重试成功率小于80%'

                    # info = f'!!!失败报警!!!\n接口重试失败!!!\n接口:{self._api_name}\n{self._host + self._url},\n成功率:{res.count(0)}/10'
                    info = f'!!!失败报警!!!\n接口重试失败!!!\n接口:{self._api_name}\n{self._host + self._url},\n成功率:{res.count(0)}/10\nPS:成功率小于80%'

                    print(info)
                    self.feishu_retry_alert(info)
                    return r.json()


                # self.log_error_statistics(log_info)
                # # 这里发送消息
                # # info = (f'!!!当前接口超时异常!!!\n_api_name:{self._api_name} \ntimed out\n:{self._host + self._url}')
                # info = (f'!!!当前接口超时异常!!!\n_api_name:{self._api_name} \ntimed out\n:{self._host + self._url}\nPS:报错原因是:\n1.接口返回超时\n2.接口响应超过5s')
                #
                #
                # self.feishu_retry_alert(info)
                # # print(info)
                # #需要更丰富的数据
                # self.log_output(self._api_name + '：超时异常')
                # # todo：增加return r = {'error_code': 500}

            # self.log_output(e)


    def feishu_alert(self, api_id, text, traceId):
        # 将_params里面的key、value转换为list类型
        key = list(self._params.keys())
        value = list(self._params.values())
        # 以列表长度为范围，获取范围内每个接口的key和value
        case = ""
        for key_count in range(0, len(key)):
            # parse.quote对汉字进行URL编码
            case += parse.quote(str(key[key_count])) + "=" + parse.quote(str(value[key_count])) + '&'
        result = self._host + self._url + "?" + case.strip('&$')
        try:
            feishu_req = requests.post(
                url='http://alarm.tyc.local/alarm/api',  # 大群报警
                # url='http://10.2.128.184:10031/alarm/api',  # 小范围报警（王杨/刘淼的小群）
                json={
                    "apiId": api_id,
                    "text": "\n【traceId】\n" + traceId +
                            "\n【接口URL】\n" + result +
                            "\n【返回JSON内容】\n" + text +
                            "\n【参数】\n" + str(self._params) ,
                    "level": "L2"
                },
                headers={
                    "Content-Type": "application/json"
                })
            print(feishu_req.json())
            return feishu_req.json()
        except Exception as e:
            self.log_output('触发飞书提醒失败：%s' % type(e))



    # 封装log日志
    def log_output(self, content):
        # 实例化记录器，命名刘淼，设置记录日志级别为DEBUG
        logger = logging.getLogger("刘淼")
        logger.setLevel(level=logging.INFO)

        # 实例化格式化器
        formatter = logging.Formatter(
            '%(name)s - %(asctime)s - %(levelname)s: %(message)s'
        )

        # 实例化处理器，用于输出到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # 实例化处理器，用于输出到文件
        # _file_path = ""
        _file_path = self._file_path
        file_handler = logging.FileHandler(_file_path)
        file_handler.setFormatter(formatter)

        # 实例化分割器，用于分割日志文件
        time_file_handler = handlers.TimedRotatingFileHandler(
            filename=_file_path,
            when='M',
            interval=1,
            backupCount=1
        )
        time_file_handler.setFormatter(formatter)
        logger.addHandler(time_file_handler)

        # 需要输出的日志内容
        logger.info(content)
        logger.handlers.clear()


if __name__ == '__main__':
    obj = BaseApi()
    # obj.log_error_statistics('121212')
    obj._api_name='817测试接口'
    info = f'!!!当前接口超时异常!!!\n_api_name:817 \ntimed out\n:测试更改消息发送方式'
    obj.feishu_retry_alert(info)
