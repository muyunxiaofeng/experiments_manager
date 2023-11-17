# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
digital_elisa	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/9	当前系统的年月日
9:24	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
09	当天
09	当前小时
24	当前分钟
15	当前秒钟
"""
from i_experimnet.src.layout import Layout


class Digital_Elisa(Layout):
    def __init__(self):
        super().__init__()
        # protocol
        self.protocol_plate = Plate("protocol", self.plate)
        self.CA_plate = Plate("CA", self.plate)
        self.DA_plate = Plate("DA", self.plate)
