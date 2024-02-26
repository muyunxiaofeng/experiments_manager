# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
list_str_clazz	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/2/24	当前系统的年月日
17:58	当前系统的时分秒
2024	当前年份
02	当前月份（形式：07）
2月	当前月份（形式：7月）
二月	当前月份（形式：七月）
24	当天
17	当前小时
58	当前分钟
19	当前秒钟
"""


class List_Str_clazz:
    def __init__(self, li=None, st=None):
        """
        列表字符；转换类
        :param li:
        :param st:
        """
        self.sep = ";"
        self.list = li
        self.str = st

    @property
    def to_str(self):
        self.str = self.sep.join(self.list)
        return self.str

    @property
    def to_list(self):
        self.list = self.str.split(self.sep)
        return self.list
