# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
info_out	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/2/27	当前系统的年月日
22:55	当前系统的时分秒
2024	当前年份
02	当前月份（形式：07）
2月	当前月份（形式：7月）
二月	当前月份（形式：七月）
27	当天
22	当前小时
55	当前分钟
20	当前秒钟
"""

from i_experments.config.bin_config import de_info
from i_experments.config.bin_config import info_out_config as _config


class Info_out:
    def __init__(self):
        self.digital_elisa = de_info()

        # renew
        self.out_put_info()

    def out_put_info(self):
        self.de_out()

    def de_out(self):
        with open(_config.de_info_out_path, mode="w", encoding="utf-8") as wr:
            for info in self.digital_elisa.de_all:
                wr.write(info)
                wr.write("\n")
