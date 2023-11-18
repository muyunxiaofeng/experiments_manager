# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
add_info	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/17	当前系统的年月日
15:15	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
17	当天
15	当前小时
15	当前分钟
57	当前秒钟
"""
import pandas as pd

from i_experimnet.utils.method_function import method_function
from i_experimnet.middleware.writing_or_loading_info_from_excel import Excel_info


class Modify_info:
    def __init__(self):
        self.root_dict = {
            "查看/修改/新增信息": self.select_info,
            "新增一种信息": self.adding
        }

        self.welcome()

    def welcome(self):
        print("=" * 20, "欢迎进入加入信息，请选择你要加入的信息", "=" * 20)
        method_function(self.root_dict)

    def select_info(self):
        pass

    def adding(self):
        pass
