# -*- coding: UTF-8 -*-

"""
    @Description：TableStore查询数据
    @author：by ChenZhang
    @create：2021/6/22 5:38 下午

"""
import json
from tablestore.client import OTSClient
from tablestore import TermQuery, BoolQuery, SearchQuery, RangeQuery, ColumnsToGet, ColumnReturnType, INF_MIN, INF_MAX, \
    CompositeColumnCondition, LogicalOperator, SingleColumnCondition, ComparatorType
import common

conf = common.read_yaml("conf/conf.yaml")


class TycOTS:
    def __init__(self, instance_name="std-monitor"):
        self.access_key_id = self.get_access_key_id
        self.access_key_secret = self.get_access_key_secret
        self.instance_name = instance_name
        # 舆情相关
        self.yq_end_point = conf["jindi-yq-spi"]["end_point"]
        self.yq_instance_name = conf["jindi-yq-spi"]["instance_name"]
        self.yq_index_name = conf["jindi-yq-spi"]["index_name"]
        self.yq_table_name = conf["jindi-yq-spi"]["table_name"]
        self.ots_client = self.connection()

    def connection(self):
        ots_client = OTSClient(end_point=self.get_end_point,
                               access_key_id=self.access_key_id,
                               access_key_secret=self.access_key_secret,
                               instance_name=self.get_instance_name)
        return ots_client

    def get_row(self, pk, columns_to_get=""):
        """
        :param pk 唯一主键,list
        :param columns_to_get 查询的字段,list
        :return: json格式的查询结果
        """
        pk = pk
        if len(columns_to_get) > 0:
            columns_to_get = columns_to_get
            consumed, return_row, next_token = self.ots_client.get_row(self.get_table_name, pk, columns_to_get)
            res = json.dumps(return_row.attribute_columns, indent=2, ensure_ascii=False)
            return res
        else:
            consumed, return_row, next_token = self.ots_client.get_row(self.get_table_name, pk)
            res = json.dumps(return_row.attribute_columns, indent=2, ensure_ascii=False)
            return res

    def search(self, column, value, extra_column=""):
        """
        :param column 查询的字段名称,str
        :param value 查询的字段值,str
        :param extra_column 非主键外的额外的字段,list
        :return: json格式的查询结果
        """

        """
        # 设置过滤器，增加列filter，当growth列的值不等于0.9且name列的值等于'杭州'时，则返回该行。
        cond = CompositeColumnCondition(LogicalOperator.AND)
        cond.add_sub_condition(SingleColumnCondition("growth", 0.9, ComparatorType.NOT_EQUAL))
        cond.add_sub_condition(SingleColumnCondition("name", '杭州', ComparatorType.EQUAL))
        # 需要在search函数里面增加参数cond=cond即可使用过滤器
        """

        query = TermQuery(column, value)
        if len(extra_column) > 0:
            columns_to_get = extra_column
            search_response = self.ots_client.search(self.get_table_name, self.get_index_name,
                                                     SearchQuery(query),
                                                     ColumnsToGet(column_names=columns_to_get,
                                                                  return_type=ColumnReturnType.SPECIFIED))
            rows = search_response.rows
            res = json.dumps(rows, indent=2, ensure_ascii=False)
            return res
        else:
            search_response = self.ots_client.search(self.get_table_name, self.get_index_name,
                                                     SearchQuery(query))
            rows = search_response.rows
            res = json.dumps(rows, indent=2, ensure_ascii=False)
            return res

    def search_dim(self, dim):
        """
        :param dim
        :return: 指定维度的uhash列表
        """
        columns_to_get = ['__uhash', '__gid', '__uid', '__related_gid',
                          '__dim', '__gids', '__join_gid']
        query = TermQuery('__dim', dim)
        search_response = self.ots_client.search(self.get_table_name, self.get_index_name,
                                                 SearchQuery(query),
                                                 ColumnsToGet(column_names=columns_to_get,
                                                              return_type=ColumnReturnType.SPECIFIED))
        rows = search_response.rows
        _uhashs = []
        _gid = []
        _related_gid = []
        for row in range(len(rows)):
            _uhashs.append(rows[row][0][0][1])
            _gid.append(rows[row][0][1][1])
            _related_gid.append(rows[row][0][3][1])
        return _uhashs, _gid, _related_gid

    def yuqing_search(self, emotion="", start="", end=""):
        client = OTSClient(end_point=self.yq_end_point, access_key_id=self.access_key_id,
                           access_key_secret=self.access_key_secret, instance_name=self.yq_instance_name)
        limit = RangeQuery('emt', start, end)
        query = TermQuery('emotion', emotion)
        columns_to_get = ['cids', 'collect_time', 'edt', 'emotion']
        boolQuery = BoolQuery(must_queries=[
            limit, BoolQuery(must_queries=[query])
        ])
        search_response = client.search(self.yq_table_name, self.yq_index_name,
                                        SearchQuery(boolQuery, limit=20),
                                        ColumnsToGet(column_names=columns_to_get,
                                                     return_type=ColumnReturnType.SPECIFIED))
        rows = search_response.rows
        return rows

    def yuqing_search_by_docid(self, docID=""):
        client = OTSClient(end_point=self.yq_end_point, access_key_id=self.access_key_id,
                           access_key_secret=self.access_key_secret, instance_name=self.yq_instance_name)
        primary_key = [('docid', docID)]
        consumed, return_row, next_token = client.get_row(self.yq_table_name, primary_key)
        res = json.dumps(return_row.attribute_columns, indent=2, ensure_ascii=False)
        return res

    def _get_primary_key(self, table_name):
        dt = self.ots_client.describe_table(table_name)
        return dt.table_meta.schema_of_primary_key

    @property
    def _list_table(self):
        list_table = self.ots_client.list_table()
        return list_table

    @property
    def get_end_point(self):
        return conf[self.instance_name]["end_point"]

    @property
    def get_instance_name(self):
        return conf[self.instance_name]["instance_name"]

    @property
    def get_table_name(self):
        return conf[self.instance_name]["table_name"]

    @property
    def get_index_name(self):
        return conf[self.instance_name]["index_name"]

    @property
    def get_access_key_id(self):
        return conf.get("access_key_id")

    @property
    def get_access_key_secret(self):
        return conf.get("access_key_secret")


if __name__ == "__main__":
    ots = TycOTS()
    res = ots.search(column="__dim", value="61", extra_column=["__dim", "__gids", "__main_id", "app_date"])
    print(res)
