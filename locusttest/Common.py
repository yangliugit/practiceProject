# -*- coding:utf-8 -*-
import linecache
import random
from MySqlConn import Mysql


# 通过文件随机获取测试号
def random_read_phone(file_name):
    RANDOM_I = random.randrange(1, 1000)
    phone = linecache.getline(file_name, RANDOM_I)
    return phone


# 通过文件循环获取测试号
def cycle_read_phone(file_name):
    pass


# 通过mysql创建测试表
def create_table(table_name):
    pass


# 通过Mysql创建测试数据
def insert_data(table_name, data):
    pass


# 通过Mysql随机取数
def get_cycle_data_from_db(table_name, col_name):
    db = Mysql()
    query_sql = "select " + col_name + " from " + table_name + " where status = %s order by rand() limit 1"
    # update_sql = "update " + table_name + " set status = 1 where " + col_name + " = %s"  # 取数完更新状态的sql
    result = db.getOne(query_sql, [0])
    # db.update(update_sql, [result[col_name]])  # 更新状态
    db.dispose()
    return result[col_name]


# if __name__ == '__main__':
#     # random_read_phone("F:/trans/locusttest/phoneNum.txt")
#     print get_cycle_data_from_db("locust_data.wzf_phone", "phone")
