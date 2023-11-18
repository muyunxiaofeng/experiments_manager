# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
method_function	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/17	当前系统的年月日
15:37	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
17	当天
15	当前小时
37	当前分钟
04	当前秒钟
"""


def method_function(method_dic):
    while 1:
        # 展示方法并调用
        for i, method in enumerate(method_dic):
            print(i, " ", method)
        # 提示用户输入
        _input = input("请输入要选择的序号，只输入Q退出：").strip()
        if not _input:
            print("不能输入空值~")
            continue
        if _input.upper() == "Q":
            return
        if _input.isdecimal() and int(_input) < len(method_dic):
            return list(method_dic.values())[int(_input)]()
