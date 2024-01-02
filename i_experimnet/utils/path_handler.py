# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
folder_walk	文件名
41379	用户名（指登录电脑的那个用户名）
2023/12/6	当前系统的年月日
23:29	当前系统的时分秒
2023	当前年份
12	当前月份（形式：07）
12月	当前月份（形式：7月）
十二月	当前月份（形式：七月）
06	当天
23	当前小时
29	当前分钟
36	当前秒钟
"""

import os
import re

import pandas as pd

from i_experimnet.config.utils_config import Path_handler_config as _config


class Path_handler:
    def __init__(self, root):
        self.root = root
        if root is not None:
            self.target_folder_path_name_list = list()
            self.target_folder_abs_path_list = list()
            self.folder_df = self.folder_walk(root)
        else:
            self.target_folder_path_name_list = list()
            self.target_folder_abs_path_list = list()
            self.folder_df = None

    def folder_walk(self, root):
        # 重置列表
        self.target_folder_path_name_list = list()
        self.target_folder_abs_path_list = list()
        # 遍历文件夹
        for path in os.listdir(root):
            self.target_folder_path_name_list.append(path)
            abs_path = os.path.join(self.path, path)
            self.target_folder_abs_path_list.append(abs_path)
        # 储存文件夹
        new_dic = {
            "path_name": self.target_folder_path_name_list,
            "abs_path": self.target_folder_abs_path_list
        }
        return pd.DataFrame(new_dic, columns=["path_name", "abs_path"])

    def folder_handler(self, root_path, keyword=None, files_prefix=None, sep=None):
        if keyword is None:
            keyword = _config.keyword
        if files_prefix is None:
            files_prefix = _config.filer_prefix
        if sep is None:
            sep = _config.sep
        # 重置列表
        self.target_folder_path_name_list = list()
        self.target_folder_abs_path_list = list()
        # 遍历所有给定目录
        for root, folder_list, file_list in os.walk(root_path):
            for file in file_list:
                file_abs_path = os.path.join(root, file)
                if keyword in file_abs_path and files_prefix in file_abs_path:
                    self.target_folder_path_name_list.append(file)
                    self.target_folder_abs_path_list.append(file_abs_path)
        # saving
        new_dic = {
            "path_name": self.target_folder_path_name_list,
            "abs_path": self.target_folder_abs_path_list
        }
        self.folder_df = pd.DataFrame(new_dic, columns=["path_name", "abs_path"])
        # split
        # sep_df = self.folder_df["path_name"].str.split("_")
        sep_df = self.folder_df["path_name"].apply(lambda x: re.split("[-_]", x))
        print(sep_df.head().to_string())
        print(sep_df.to_string())