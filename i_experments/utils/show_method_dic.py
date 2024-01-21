# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
show_method_dic	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/1/21	当前系统的年月日
14:17	当前系统的时分秒
2024	当前年份
01	当前月份（形式：07）
1月	当前月份（形式：7月）
一月	当前月份（形式：七月）
21	当天
14	当前小时
17	当前分钟
14	当前秒钟
"""
import inspect


class Show_dic:
    def __init__(self):
        pass

    @staticmethod
    def show_iter(method_dic):
        while 1:
            # 展示方法并调用
            print(method_dic)
            for i, method in enumerate(method_dic):
                print(i, " ", method)
            # 提示用户输入
            _input = input("请输入要选择的序号，只输入Q退出：").strip()
            if not _input:
                print("不能输入空值~")
                continue
            if _input.upper() == "Q":
                return "Q", "Q"
            if _input.isdecimal() and int(_input) < len(method_dic):
                if isinstance(method_dic, dict):
                    value = list(method_dic.values())[int(_input)]
                else:
                    value = list(method_dic)[int(_input)]
                return int(_input), value
