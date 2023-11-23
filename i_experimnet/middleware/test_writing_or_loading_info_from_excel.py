# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
test_writing_or_loading_info_from_excel	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/21	当前系统的年月日
14:37	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
21	当天
14	当前小时
37	当前分钟
00	当前秒钟
"""
from unittest import TestCase
from i_experimnet.middleware.writing_or_loading_info_from_excel import Excel_info


class TestExcel_info(TestCase):
    def test_params_add(self):
        e = Excel_info()
        e.params_add("digital_elisa_protocol", DA="0.5", DA_unit="μg/mL", CA="20", CA_unit="μg/10 mg beads",
                     Ag_incubation="60",
                     DA_incubation="0", sbg_incubation="10", incubation_unit="min")
