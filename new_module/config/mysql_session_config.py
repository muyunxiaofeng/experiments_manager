# -*- coding:utf-8 -*-
"""
experiment_Digital_Elisa	项目名
PyCharm	集成开发环境
mysql_session_config	文件名
41379	用户名（指登录电脑的那个用户名）
2023/9/2	当前系统的年月日
19:57	当前系统的时分秒
2023	当前年份
09	当前月份（形式：07）
9月	当前月份（形式：7月）
九月	当前月份（形式：七月）
02	当天
19	当前小时
57	当前分钟
23	当前秒钟
"""
# creator = pymysql,  # 使用链接数据库的模块
maxconnections = 5 # 连接池允许的最大连接数，0和None表示不限制连接数
mincached = 2  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
maxcached = 3  # 链接池中最多闲置的链接，0和None不限制
blocking = True  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
setsession = []  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
ping = 0
host = '127.0.0.1'
port = 3306
user = 'root'
password = '123456'
database = 'blog'
charset = 'utf8mb4'