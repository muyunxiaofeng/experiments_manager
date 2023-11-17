# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
digital_elisa_file_select	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/17	当前系统的年月日
13:56	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
17	当天
13	当前小时
56	当前分钟
05	当前秒钟
"""
import os
import shutil
from pprint import pprint

import pandas as pd


class Digital_Elisa_file_select:
    def __init__(self, path=None):
        self.path = path
        self.keyword = "result"
        self.target_folder_abs_path_list = []

    def folder_handler(self):
        for root, folder_list, file_list in os.walk(self.path):
            for file in file_list:
                file_abs_path = os.path.join(root, file)
                if self.keyword in file_abs_path:
                    self.target_folder_abs_path_list.append(file_abs_path)

    def data_washing(self):
        for target_folder_abs_path in self.target_folder_abs_path_list:
            if ["xlsx", "excel", "xls"] in target_folder_abs_path:
                if target_folder_abs_path.split(".")[-1] == "xls":
                    shutil.copy(target_folder_abs_path, target_folder_abs_path + "x")  # 复制一个文件到一个文件或一个目录
                    target_folder_abs_path = target_folder_abs_path + "x"
