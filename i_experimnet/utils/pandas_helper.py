# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
pandas_excel_handler	文件名
41379	用户名（指登录电脑的那个用户名）
2023/12/6	当前系统的年月日
23:41	当前系统的时分秒
2023	当前年份
12	当前月份（形式：07）
12月	当前月份（形式：7月）
十二月	当前月份（形式：七月）
06	当天
23	当前小时
41	当前分钟
49	当前秒钟
"""


class Pandas_helper:
    def __init__(self):
        self.new_excel_list = list()

    def format_excel(self, excel_path_list):
        for target_folder_abs_path in excel_path_list:
            if ["xlsx", "excel", "xls"] in target_folder_abs_path:
                if target_folder_abs_path.split(".")[-1] == "xls":
                    shutil.copy(target_folder_abs_path, target_folder_abs_path + "x")  # 复制一个文件到一个文件或一个目录
                    target_folder_abs_path = target_folder_abs_path + "x"
                    self.new_excel_list.append(target_folder_abs_path)
