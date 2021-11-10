# encoding: utf-8
'''
@author: huangping
@file: tablestore_db.py
@time: 2020/8/21 6:08 下午
@desc:
'''

import pandas as pd
from tablestore import OTSClient, TermQuery, BoolQuery, SearchQuery, ColumnsToGet, ColumnReturnType, Row, OTSClientError,TermsQuery

import config.tbstore_config_  as tbstore
import re

class TB_DB(object):
    def __init__(self,conf_name=None):
        if conf_name==None:
            self.config = tbstore.PCConfig['company_tag']
        else:
            self.config = tbstore.PCConfig[conf_name]
        self.end_point = self.config['end_point']
        self.access_key_id = self.config['access_key_id']
        self.access_key_secret = self.config['access_key_secret']
        self.instance_name = self.config['instance_name']
        self.final_table_name = self.config['final_table_name']
        self.index_name = self.config['index_name']
        self.ots_client = self.connection()

    def connection(self):
        ots_client = OTSClient(end_point=self.end_point, access_key_id=self.access_key_id, access_key_secret=self.access_key_secret, instance_name=self.instance_name)
        return ots_client

    '''
    精确查询：TermQuery
    '''


    def search(self, query, limit=float('inf')):
        '''
        case:情报动态
        query = {'dim':56,'main_id':12344}
        dim:类别编号
        main_id:源表里边的id
        '''
        boolQuery = None
        for item, value in query.items():
            queryList = []
            query = TermQuery(item, value)
            queryList.append(query)
            if boolQuery is not None:
                queryList.append(boolQuery)
            boolQuery = BoolQuery(must_queries=queryList)
        all_rows = []
        next_token = None
        count = 0
        while count == 0 or next_token:
            rows, next_token, total_count, is_all_succeed = self.ots_client.search(self.final_table_name,
                                                                              self.index_name,
                                                                              SearchQuery(boolQuery,
                                                                                          next_token=next_token,
                                                                                          limit=100,
                                                                                          get_total_count=True),
                                                                              columns_to_get=ColumnsToGet(
                                                                                  return_type=ColumnReturnType.ALL))

            count = count + 100
            print(count)
            print(total_count)
            print("\r" + "total_count={}/{}".format(count, total_count), end='')
            print('\n')

            for row in rows:
                all_rows.append(row)
            if count >= limit:
                break
        return all_rows

    def search_s(self, query, limit = float('inf')):
        """
        Desc: 多词精确查询
        :param query: {main_id':[12344,32432]}
        :param limit:
        :return:
        """
        boolQuery = None
        for item, value in query.items():
            queryList = []
            query = TermsQuery(item, value)
            queryList.append(query)
            if boolQuery is not None:
                queryList.append(boolQuery)
            boolQuery = BoolQuery(must_queries=queryList)
        all_rows = []
        next_token = None
        count = 0
        while count == 0 or next_token:
            rows, next_token, total_count, is_all_succeed = self.ots_client.search(self.final_table_name,
                                                                              self.index_name,
                                                                              SearchQuery(boolQuery,
                                                                                          next_token=next_token,
                                                                                          limit=100,
                                                                                          get_total_count=True),
                                                                              columns_to_get=ColumnsToGet(
                                                                                  return_type=ColumnReturnType.ALL))

            count = count + 100
            # print("\r" + "total_count={}/{}".format(count, total_count), end='')

            for row in rows:
                all_rows.append(row)
            if count >= limit:
                break
        return all_rows

    def search_combined_query(self, query, limit = float('inf')):
        """
        Desc: 范围+多词精确查询
        :param query: {main_id':[12344,32432]}
        :param limit:
        :return:
        """
        queryList = []
        # boolQuery =RangeQuery(field_name="update_time",range_from="2021-01-24 10:00:00") #1611453600000,2021-01-24 10:00:00
        # queryList.append(boolQuery)
        for item, value in query.items():
            query = TermsQuery(item, value)
            queryList.append(query)
            boolQuery = BoolQuery(must_queries=queryList)
        all_rows = []
        next_token = None
        count = 0
        while count == 0 or next_token:
            rows, next_token, total_count, is_all_succeed = self.ots_client.search(self.final_table_name,
                                                                              self.index_name,
                                                                              SearchQuery(boolQuery,
                                                                                          next_token=next_token,
                                                                                          limit=100,
                                                                                          get_total_count=True),
                                                                              columns_to_get=ColumnsToGet(
                                                                                  return_type=ColumnReturnType.ALL))

            count = count + 100
            # print("\r" + "total_count={}/{}".format(count, total_count), end='')


            for row in rows:
                all_rows.append(row)
            if count >= limit:
                break
        return all_rows

def get_tbstore_data(query,conf_name):    #获取数据
    a = TB_DB(conf_name)
    data = a.search(query)
    df_empty = pd.DataFrame()
    if len(data) == 0:
        return df_empty
    else:
        return data
        # res_data = pd.DataFrame.empty
        # for i in range(1):
        #     # print(data[i][1])
        #     df = pd.DataFrame(data[i][1])
        #     df.index = df[0]
        #     df_1 = df.drop([0,2],axis=1)
            # print(df_1)


def get_tbstore_datas(query,conf_name):
    """
    Desc: 多词精确查询
    :param query:
    :return:
    """
    a=TB_DB(conf_name)
    datas= a.search_s(query)
    df_empty=pd.DataFrame()
    if len(datas)==0:
        return df_empty
    else:
        result=[]
        for data in datas:
            df =pd.DataFrame(data[1])
            df.index = df[0]
            result.append(df[1])
        return result

import re

def deal_with_content(content):
    cgid = 0
    pattern1 = "<font color= #EF5644>(.*?)</font>"
    pattern2 = '<a href="https://www.tianyancha.com/company/(.*?)" target="_blank">(.*?)</a>'
    content_2 = re.findall(pattern1, str(content))
    if '<a href=' in content_2[0]:
        cont_name = re.findall(pattern2, str(content_2[0]))
        cgid = cont_name[0][0]
        cname = cont_name[0][1]
    else:
        cname = content_2[0]
    return cgid, cname




def get_tbstore_combined_query(query,conf_name):
    """
    Desc: 多词精确查询
    :param query:
    :return:
    """
    a=TB_DB(conf_name)
    datas= a.search_combined_query(query)
    df_empty=pd.DataFrame()
    if len(datas)==0:
        return df_empty
    else:
        result=[]
        for data in datas:
            df =pd.DataFrame(data[1])
            df.index = df[0]
            result.append(df[1])
        return result

# #情报动态
# query = {'dim':11,'main_id':266017219} #147072889,#266017219
#
# # 公司标签属性
# query = {'company_id': 198750728}  # company_show_labels为标签字段


## 股权穿透
# query = {'root_gid':3455245964}
query = {'__dim':1201}
# query = {'__uhash':"000001256362d9f1d018fdc05cf235ae-18"}

if __name__ == '__main__':
    conf_name = 'std_monitor_test'  #B端风险监控
    data = get_tbstore_data(query,conf_name)
    # data=get_tbstore_combined_query(query,conf_name)
    print(data)

