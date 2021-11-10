# 使用python操作ElasticSearch
from elasticsearch import Elasticsearch
# 连接ES
es = Elasticsearch([{'host':'10.101.12.19','port':9200}], timeout=3600)
# 若需验证
# es = Elasticsearch(['10.101.12.19'], http_auth=('xiao', '123456'), timeout=3600)