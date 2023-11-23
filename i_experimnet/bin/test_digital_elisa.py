# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
test_digital_elisa	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/9	当前系统的年月日
13:32	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
09	当天
13	当前小时
32	当前分钟
36	当前秒钟
"""
from unittest import TestCase
from pprint import pprint
from i_experimnet.bin import digital_elisa


# class TestDigital_Elisa(TestCase):
#     def test_folder_handler(self):
#         de = digital_elisa.Digital_Elisa(path=r"F:\W20231108")
#         de.folder_handler()
#         pprint(de.target_folder_abs_path_list)


class TestDigital_Elisa(TestCase):
    def test_guidance(self):
        d = digital_elisa.Digital_Elisa()
