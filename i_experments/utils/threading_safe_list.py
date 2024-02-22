# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
threading_safe_list	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/1/26	当前系统的年月日
20:39	当前系统的时分秒
2024	当前年份
01	当前月份（形式：07）
1月	当前月份（形式：7月）
一月	当前月份（形式：七月）
26	当天
20	当前小时
39	当前分钟
35	当前秒钟
"""
import threading
import queue


class ThreadSafeList:
    def __init__(self):
        self.lock = threading.Lock()
        self.list = []

    def add(self, item):
        with self.lock:
            self.list.append(item)

    def get(self):
        with self.lock:
            return self.list[:]
