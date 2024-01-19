# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
excel_load	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/1/18	当前系统的年月日
22:48	当前系统的时分秒
2024	当前年份
01	当前月份（形式：07）
1月	当前月份（形式：7月）
一月	当前月份（形式：七月）
18	当天
22	当前小时
48	当前分钟
01	当前秒钟
"""

import pandas as pd


class Loading_excel:
    def __init__(self, excel_path):
        self.excel_path = excel_path
        # 加载并返回
        self.excel = self.load_excel()

    def load_excel(self):
        return pd.read_excel(self.excel_path)
