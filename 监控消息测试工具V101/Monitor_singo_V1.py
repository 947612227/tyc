from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import urlencode
import pandas as pd
import jsonpath
import requests

# 待完善:
# 1.自动生成时间戳,陈章函数解决
# 2.支持获取第N个数据
# from 监控消息测试工具 import env
# from 监控消息测试工具.common import get_timestamp_and_previous_timestamp
import env
from common import get_timestamp_and_previous_timestamp


class Monitoring_data_spyder():#调用搜索接口获取一个数据
    # 获取main_id,gid的类
    def __init__(self, type,env):
        type = str(type)
        eventEndTime,eventStartTime=get_timestamp_and_previous_timestamp()
        print(eventStartTime,eventEndTime)
        self.url = f'http://{env}/event/page.json?dims={type}&eventStartTime={eventStartTime}&eventEndTime={eventEndTime}&ps=100'
        self.data = requests.get(self.url)
        self.data_json = self.data.json()
        print(f'输出的url是:{self.url}')

    def get_mainid_one(self):
        var = '__main_id'
        main_id_value = jsonpath.jsonpath(self.data_json, f'$..data.items[0].{var}')
        return main_id_value

    def get_gids_one(self):
        var = 'gids'
        gids_value = jsonpath.jsonpath(self.data_json, f'$..data.items[0].{var}')

        res = gids_value[0].split(';')
        # print(f'git分割{res},{res[0]}')
        return res[0]

    def get_n_info(self):
        '''获取相应结果里所有的gid/main_id/uhash'''
        pass
    def Consolidate_mainid_gids(self):
        id = self.get_mainid_one()
        gid = self.get_gids_one()

        if id == False: return '没有,数据'

        # return f'{id[0]},{gid}'
        #main_id用来发消息,gid用来关注实体
        return id[0],gid

    def N_Consolidate_mainid_gids(self):
        Consolidate = []
        for i in range(50):
            print(f'i:{i}')
            try:
                gids_value = jsonpath.jsonpath(self.data_json, f'$..data.items[{i}].gids')
                # print(gids_value)
                screen_gid = gids_value[0].split(';')[0]

                main_id_value = jsonpath.jsonpath(self.data_json, f'$..data.items[{i}].__main_id')[0]

                uhash = jsonpath.jsonpath(self.data_json,f'$..data.items[{i}].__uhash')[0]
                print(f'uhash:{uhash}')

                Consolidate.append({'gid':screen_gid,'main_id':main_id_value,'uhash':uhash})
            except BaseException as e:
                print(e)
                return Consolidate

        return Consolidate

# obj = Monitoring_data_spyder(type='34')
# # print(obj.get_mainid_one())
# print(obj.get_gids_one())

# 数据转换类
class Data_conversion():
    url817 = env.url817
    # url817 = 'http://open.api.tianyancha.com/services/open/ic/baseinfo/2.0?id='
    # url_organization = 'http://cstd.test63.tianyancha.com/organization/'
    url_organization = env.url_organization

    url_human = env.url_human

    def gid_to_companyname(self, gid):
        gid = str(gid)
        data = requests.get(self.url817 + gid)
        data_json = data.json()

        companyname = jsonpath.jsonpath(data_json, f'$.result.name')
        # print(companyname)
        return str(companyname[0])

    def gid_to_organization(self, gid):
        gid = str(gid)
        data = requests.get(self.url_organization + gid)

        return data.text

    def gid_to_human_name(self, gid):
        gid = str(gid)
        data = requests.get(self.url_human + gid)
        data_json = data.json()

        hname = jsonpath.jsonpath(data_json, f'$.hname')
        cname = jsonpath.jsonpath(data_json, f'$.cname')
        # print(companyname)
        return f'{hname}-{cname}'

    def switch_key(self,gid):
        if 'b' in str(gid):
            organization = self.gid_to_organization(gid)
            return {'data':organization,'type':'organization'}
        elif '-c' in str(gid):
            name = self.gid_to_human_name(gid)
            return {'data':name,'type':'human'}
        else:
            try:
                companyname = self.gid_to_companyname(gid)
                return {'data':companyname,'type':'companyname'}
            except TypeError as e:
                print(f'{e},遇到类型错误,接收到了:{gid},type:{type(gid)}')


class singo_send_monitor_message:
    def __init__(self,ip):
        self.ip = f'http://{ip}'
    #
    def code_cgid(self, table, main_id):

        url = f'{self.ip}/history/byTableAndRids?table={table}&rids={main_id}&syncType=2'

        r = requests.get(url)
        return f'{url}'

# class send_monitor_message_V2:
#     def __init__(self,uhash):
#         self.url = f'http://{env.test_ip}/history/syncEvent?source=event_v7&target=event_v6_test&uhashes={uhash}-9121'
#
#     def send_for_uhash(self):
#         r = requests.get(self.url)
#         return f'{r}'



def send_monitor_message_V2(uhash):
    s = ''
    for i in uhash:
        s = s + ',' + i

    print(s)
    url = f'http://{env.test_ip}/history/syncEvent?source=event_v7&target=event_v6_test&uhashes={s}'
    # r = requests.get(url)
    r = requests.post(url)
    print(f'url:{url},\nsend_monitor_message_V2:{r}')
    return f'{r}'

if __name__ == '__main__':
    online_ip = '10.39.222.64:20001'
    # obj = Monitoring_data_spyder(type='34',env=online_ip)
    # print(obj.get_mainid_one())
    # res = (obj.Consolidate_mainid_gids())
    # print(res[1])
    # gid = res[1]
    # obj2 = Data_conversion()
    # value = obj2.switch_key(gid)
    # print(value)

    # N_res = obj.N_Consolidate_mainid_gids()
    # print(N_res)

    send_monitor_message_V2(['adf5ce5cdd635085f9940dc0572c269f'])


