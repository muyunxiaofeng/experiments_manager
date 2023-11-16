# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
test_layout	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/7	当前系统的年月日
13:35	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
07	当天
13	当前小时
35	当前分钟
56	当前秒钟
"""
import re
from pprint import pprint
from unittest import TestCase
from i_experimnet.bin.layout import Layout


class TestLayout(TestCase):

    def test_layout_init(self):
        self.layout = Layout()
        # print(self.layout.down_right(1, 3, 1, 3))
        # print(self.layout.left_up(1, 3, 1, 3))
        # print(self.layout.right_down(1, 3, 1, 3))
        # print(self.layout.up_right(1, 3, 1, 3))
        # print(self.layout.right_up(1, 3, 1, 3))
        # print(self.layout.down_left(1, 3, 1, 3))
        # print(self.layout.left_down(1, 3, 1, 3))

        #
        # self.layout.area_split("aaaa1-abbbb5")
        # area_equation = "(fg/mL)"
        # print(re.findall("\((.*/.*)\)", area_equation))

        # self.layout.layout_init()
        # pprint(self.layout.position_plate)
        # pprint(self.layout.values_plate)
        # pprint(self.layout.modify_plate)
        # pprint(self.layout.template_plate.to_dict())
