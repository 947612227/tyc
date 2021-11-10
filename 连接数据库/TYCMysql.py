# -*- coding: UTF-8 -*-

"""
    @Description：
    @author：by ChenZhang
    @create：2021/6/29 9:43 上午

"""
import pymysql


class TYCMysql:
    def __init__(self, host, user, password, database, port="3306"):
        self.host = host
        self.user = user
        self.password = str(password)
        self.database = database
        self.port = int(port)
        self.db = self.connect_db()

    def connect_db(self):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password,
                             database=self.database,
                             port=self.port)
        return db

    def get_sql_data(self, sql):
        """
        :param sql: 需要执行的sql，禁止使用更新、删除sql
        :return: 以元组格式返回查询结果
        """
        key_word = ['insert', 'delete', 'truncate', 'drop', 'update']
        for i in key_word:
            if i in sql.lower():
                return '禁止使用更新删除语句'
        if 'where' not in sql:
            return '请尽量避免使用全量查询'
        else:
            cursor = self.db.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
        self.close_db()
        return data

    def close_db(self):
        self.db.close()
if __name__ == '__main__':
    host, user, password = 'rm-2zek5z37w8q1rf5b5.mysql.rds.aliyuncs.com', 'jindi_b_rw', 'J1ndiBxy^t'
    database = 'std-admin'
    a = TYCMysql(host, user, password, database)
    sql = '''select  
        o.org_name 客户名称,
        u.username 用户名,
        date(u.create_time) 开通日期,
        DATEDIFF(NOW(),u.create_time) + 1 目前开通天数,
        date(u.last_login_time) 最近登录日期,
        (select count(DISTINCT r.company_graph_id) from  `std-log-online`.record_search r where r.user_id = u.id)   查询企业数量,
        (select SUM(r.search_count)  from  `std-log-online`.record_search r where r.user_id = u.id)   查询企业次数
        from users u
        inner join organization o on u.org_id = o.id and (o.org_name like '%刑侦%'  or o.org_name like '%反诈%')
        inner join org_product op on op.org_id = o.id 
        inner join users uu on op.business_user_Id = uu.id and uu.org_id = 1 and uu.realname = "刘文江"
        order by 开通日期'''
    b = a.get_sql_data(sql=sql)
    print(b)