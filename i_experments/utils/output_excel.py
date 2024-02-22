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
        """
        给定一个dataframe格式的字典就可以打包成一个excel的方法
        :param dic: 字典
        :param o_path: 数据地址
        :return:
        """
        df = pd.DataFrame(dic)
        df.to_excel(o_path, index=False)

    @staticmethod
    def add_a_record(df1, dic2, o_path):
        """
        给原有df中加入一条数据，
        :param df1: 原有df
        :param dic2: 新数据
        :param o_path: 数据地址
        :return:
        """
        # df1 = pd.DataFrame(dic1)
        df2 = pd.DataFrame(dic2)
        df = pd.concat([df1, df2])
        df.to_excel(o_path, index=False)

    @staticmethod
    def only_save_df(df, o_path):
        df.to_excel(o_path, index=False)
