# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
digital_elisa_calculate	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/9	当前系统的年月日
9:26	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
09	当天
09	当前小时
26	当前分钟
06	当前秒钟
"""
import math


class Digital_Elisa_calculate:
    def __init__(self):
        pass

    @staticmethod
    def calculator_for_aeb(positive_beads, total_beads):
        aeb = -math.log(1 - positive_beads / total_beads)
        return aeb
