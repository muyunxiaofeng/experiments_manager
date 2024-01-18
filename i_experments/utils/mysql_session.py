# -*- coding:utf-8 -*-
"""
experiment_Digital_Elisa	项目名
PyCharm	集成开发环境
mysql_session	文件名
41379	用户名（指登录电脑的那个用户名）
2023/9/2	当前系统的年月日
19:45	当前系统的时分秒
2023	当前年份
09	当前月份（形式：07）
9月	当前月份（形式：7月）
九月	当前月份（形式：七月）
02	当天
19	当前小时
45	当前分钟
19	当前秒钟
"""
import traceback

import pymysql
from dbutils.pooled_db import PooledDB
from homework_stage4.config import mysql_session_config as _config

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=_config.maxconnections,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=_config.mincached,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=_config.maxcached,  # 链接池中最多闲置的链接，0和None不限制
    blocking=_config.blocking,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    setsession=_config.setsession,  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=_config.ping,
    host=_config.host,
    port=_config.port,
    user=_config.user,
    password=_config.password,
    database=_config.database,
    charset=_config.charset,
)


class Mysql_session:
    def __init__(self):
        self.connect = POOL.connection()
        # pymysql.cursors.DictCursor 字典化回参
        self.cursor = self.connect.cursor(pymysql.cursors.DictCursor)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connect.close()

    def exec(self, sql, **kwargs):
        """
        实现增删改的功能
        :param sql: sql语句
        :param kwargs: 参数
        :return: 无
        """
        try:
            # print(sql, kwargs)
            self.cursor.execute(sql, kwargs)
        except Exception as e:
            print("修改失败，请联系客服~")
            self.connect.rollback()
            print(e)
            print(traceback.format_exc())
        else:
            self.connect.commit()
            # print("修改成功！")

    def fetch_one(self, sql, **kwargs):
        """
        查询功能
        :param sql:
        :param kwargs:
        :return:
        """
        try:
            # print(sql, kwargs)
            self.cursor.execute(sql, kwargs)
            result = self.cursor.fetchone()

        except Exception as e:
            print("查询失败，请联系客服~")
            self.connect.rollback()
            print(e)
            print(traceback.format_exc())
        else:
            # print("查询成功！")
            return result

    def fetch_all(self, sql, **kwargs):
        try:
            # print(sql, kwargs)
            self.cursor.execute(sql, kwargs)
            result = self.cursor.fetchall()
        except Exception as e:
            print("查询失败，请联系客服~")
            self.connect.rollback()
            print(e)
            print(traceback.format_exc())
        else:
            # print("查询成功！")
            return result


