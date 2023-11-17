# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
test_plate	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/17	当前系统的年月日
13:01	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
17	当天
13	当前小时
01	当前分钟
30	当前秒钟
"""
from unittest import TestCase
from i_experimnet.src.plate import Plate


class TestPlate(TestCase):
    def test_load_excel(self):
        p = Plate("test")
        p.load_excel(path=r"D:\OneDrive\201.python\pythonWorkSpace\experiments_manager\i_experimnet\fileslayout-V1.0.02023-11-17-12-53-09.xlsx")
        print(p)