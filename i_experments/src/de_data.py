# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
de_data	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/1/22	当前系统的年月日
01:34	当前系统的时分秒
2024	当前年份
01	当前月份（形式：07）
1月	当前月份（形式：7月）
一月	当前月份（形式：七月）
22	当天
01	当前小时
34	当前分钟
29	当前秒钟

1.
"""
import os
import re
import shutil

from i_experments.config.src_config import De_data_cornfig as _config


class De_data:
    def __init__(self):
        self.version = "de_data_V1.0.0"
        # path = "/Users/frozensword/Downloads/SQL必知必会/副本Excel-1-7-20231227-1522.xlsx"
        self.path = "/Volumes"



    @staticmethod
    def xls_to_xlsx(xls_path):
        if xls_path.endswith(".xls"):
            new_path = xls_path + "x"
            shutil.copy(xls_path, new_path)
            return new_path
        return xls_path

    @staticmethod
    def find_result(folder_path):
        re_list = re.findall(_config.result_re, folder_path)[0]
        return re_list

    @staticmethod
    def result_walk(root_path):
        for root, folder_list, file_list in os.walk(root_path):
            for file in file_list:
                file_abs_path = os.path.join(root, file)
                print(file)
                print(file_abs_path)


if __name__ == '__main__':
    # path = "/Volumes/找幻影/2023-12-20 183554 实验1w5455/W54-7/result-20231220-1843"
    path = "/Volumes"
    # path = "/"
    # path = "/Users/frozensword/Downloads/SQL必知必会/副本Excel-1-7-20231227-1522.xlsx"
    # path = "/Users/frozensword/Downloads/SQL必知必会"
    # print(os.listdir(path))
    # print(De_data.find_result(folder_path=path))
    De_data.result_walk(root_path=path)
