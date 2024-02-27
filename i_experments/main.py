# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
main	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/1/18	当前系统的年月日
22:19	当前系统的时分秒
2024	当前年份
01	当前月份（形式：07）
1月	当前月份（形式：7月）
一月	当前月份（形式：七月）
18	当天
22	当前小时
19	当前分钟
59	当前秒钟
"""
import os
import sys

# 将根目录放到python解释器中
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from i_experments.bin.platform_management import Platform_management as platform_management
from i_experments.bin.Items import Items as item_select
from i_experments.bin.Organize_data import Organize_data as organize_data
from i_experments.bin.info_out import Info_out as info_out


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
            func = list(method_dic.values())[int(_input)]()


if __name__ == '__main__':
    # 方法的字典
    method = {
        "平台管理": platform_management,
        "选择项目、、会被删掉": item_select,
        "整理数据": organize_data,
        "信息输出": info_out
    }
    # 方法实现
    method_function(method_dic=method)
