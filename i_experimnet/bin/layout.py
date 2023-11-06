# -*- coding:utf-8 -*-
"""
experiment_Digital_Elisa	项目名
PyCharm	集成开发环境
layout	文件名
41379	用户名（指登录电脑的那个用户名）
2023/10/24	当前系统的年月日
17:04	当前系统的时分秒
2023	当前年份
10	当前月份（形式：07）
10月	当前月份（形式：7月）
十月	当前月份（形式：七月）
24	当天
17	当前小时
04	当前分钟
59	当前秒钟
"""
import math
import string
import numpy as np
import pandas as pd

from i_experimnet.utils import some_count


class Layout:
    def __init__(self, plate=96):
        self.plate = plate
        self.layout = self.layout()
        pass

    def layout_init(self):
        match self.plate:
            case 96:
                row = 8
                col = 12
            case "96T":
                row = 12
                col = 8
            case 12:
                row = 4
                col = 3
            case _:
                row = 8
                col = math.ceil(self.plate / 8)
        row_num = [some_count.row(index) for index in range(row)]
        col_num = list(range(1, col + 1))


def layout(self):
    self.help_layout()


@staticmethod
def help_layout():
    while 1:
        print("例：", "a1a3,a4,a5=0;b12=1000;(fg/mL)")
        _input = input("请输入位置信息，用区域间用分号隔开，只输入Q退出：").strip()
        if not _input:
            print("不能输入空值~")
            continue

        if _input.upper() == "Q":
            return

        area_list = _input.split(";")

        return
