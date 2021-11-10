# -*- coding: UTF-8 -*-

"""
    @Description：
    @author：by ChenZhang
    @create：2021/8/11 9:18 上午

"""
import redis


class TYCRedis:
    def __init__(self, host, password, db, port=6379, key=""):
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.key = key
        self.client = self.connection()

    def connection(self):
        pool = redis.ConnectionPool(host=self.host, port=self.port,
                                    password=self.password,
                                    db=self.db, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        return r

    @property
    def get_value(self):
        res = self.client.get(self.key)
        if res is None:
            return f"key:{self.key} 不存在"
        else:
            return res

    @property
    def delete_key(self):
        res = self.client.delete(self.key)
        if res == 1:
            return f"key:{self.key} 已删除"
        else:
            return "warn：删除异常"
