# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
test_digital_elisa_file_select	文件名
41379	用户名（指登录电脑的那个用户名）
2023/12/6	当前系统的年月日
14:15	当前系统的时分秒
2023	当前年份
12	当前月份（形式：07）
12月	当前月份（形式：7月）
十二月	当前月份（形式：七月）
06	当天
14	当前小时
15	当前分钟
28	当前秒钟
"""
from unittest import TestCase
from i_experimnet.middleware.digital_elisa_file_select import Digital_Elisa_file_select


class TestDigital_Elisa_file_select(TestCase):
    # d = Digital_Elisa_file_select("F:/")
    d = Digital_Elisa_file_select()
    d.folder_list()
    print(d.folder_dataframe.to_string())

