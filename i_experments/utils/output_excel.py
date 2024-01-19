# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
output_excel	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/1/18	当前系统的年月日
23:13	当前系统的时分秒
2024	当前年份
01	当前月份（形式：07）
1月	当前月份（形式：7月）
一月	当前月份（形式：七月）
18	当天
23	当前小时
13	当前分钟
54	当前秒钟
"""
import pandas as pd


class Output_excel:
    def __init__(self):
        pass

    @staticmethod
    def write_a_dic(dic, o_path):
        df = pd.DataFrame(dic)
        df.to_excel(o_path, index=True)
