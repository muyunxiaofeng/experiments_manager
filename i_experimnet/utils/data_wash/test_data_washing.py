# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
test_data_washing	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/9	当前系统的年月日
14:23	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
09	当天
14	当前小时
23	当前分钟
54	当前秒钟
"""
from i_experimnet.utils.data_wash.data_washing import Data_washing

from unittest import TestCase


class TestData_washing(TestCase):
    def test_iqr(self):
        li = [1, 2, 3, 4, 5, 6, 7, 8]
        dw = Data_washing(data=li)
        print(dw.iqr())
