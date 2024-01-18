# -*- coding:utf-8 -*-
"""
experiment_Digital_Elisa	项目名
PyCharm	集成开发环境
redis_db	文件名
41379	用户名（指登录电脑的那个用户名）
2023/7/15	当前系统的年月日
15:42	当前系统的时分秒
2023	当前年份
07	当前月份（形式：07）
7月	当前月份（形式：7月）
七月	当前月份（形式：七月）
15	当天
15	当前小时
42	当前分钟
50	当前秒钟
"""
import os
import subprocess
# redis的根目录
redis_root_path = r"D:\OneDrive\201.python\redis-64.3.0.503"
# redis服务名称
redis_server = "redis-server.exe"
# redis服务器路径
redis_server_path = os.path.join(redis_root_path, redis_server)
print(redis_server_path)
# redis数据库名称
redis_db = "redis-cli.exe"
# redis数据库路路径
redis_db_path = os.path.join(redis_root_path, redis_db)
# redis配置文件
redis_server_conf = "redis.windows.conf"
# redis配置文件路径
redis_server_conf_path = os.path.join(redis_root_path, redis_server_conf)


re = subprocess.run([redis_db_path, "auth", "123456"])