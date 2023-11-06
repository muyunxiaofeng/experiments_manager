# -*- coding:utf-8 -*-
"""
experiment_Digital_Elisa	项目名
PyCharm	集成开发环境
layout	文件名
41379	用户名（指登录电脑的那个用户名）
2023/10/24	当前系统的年月日
17:04	当前系统的时分秒
2023	当前年份
10	当前月份（形式：07）
10月	当前月份（形式：7月）
十月	当前月份（形式：七月）
24	当天
17	当前小时
04	当前分钟
59	当前秒钟
"""
import numpy as np


class Layout:
    def __init__(self):
        self.layout = self.layout()
        pass

    def layout(self):
        while 1:
            _input = input("请输入要选择的序号，只输入Q退出：").strip()
            if not _input:
                print("不能输入空值~")
                continue
            if _input.upper() == "Q":
                return
