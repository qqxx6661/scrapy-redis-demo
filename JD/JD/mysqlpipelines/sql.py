# -*- coding: utf-8 -*-
import pymysql
import logging

# for master
db_item = pymysql.connect(host="localhost", user="root", password="root",
                          db="pricemonitor", port=3306, charset='utf8')

# for slave
# db_item = pymysql.connect(host="10.140.0.2", user="root", password="root",
#                           db="pricemonitor", port=3306, charset='utf8')

cur_item = db_item.cursor()

class Sql:

    @classmethod
    def insert_new_item(cls):
        # designed by yourself
        pass