# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
platform_managerment	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/2/24	当前系统的年月日
15:03	当前系统的时分秒
2024	当前年份
02	当前月份（形式：07）
2月	当前月份（形式：7月）
二月	当前月份（形式：七月）
24	当天
15	当前小时
03	当前分钟
22	当前秒钟
"""
import os.path

import pandas as pd

from i_experments.config.bin_config import platform_config as _config
from i_experments.utils.list_str_clazz import List_Str_clazz as lts


class Platform_management:
    def __init__(self):
        # 文件及路径
        self.platform_file = None
        self.platform_path = _config.platform_files

        # 选择的行名
        self.platform_row = None

        self.change_platform_dic = {
            "增加参数": self.add_para,
            "删除参数": self.del_para,
            "修改参数": self.update_para,
            "查看参数": self.select_para,
        }
        # 需要你修改的值的列表
        self.para_LTS = lts()

        # 执行
        self.platform_initializing()

        self.platform_change()

    def platform_initializing(self):
        """
        v1.0
        1. 如果没有这个文件 创建：平台名称\t参数名\t版本号    参数名用分号隔开：参数1；参数2；...参数n
        2. 如果有则读取加载到self中
        :return:
        """
        if os.path.exists(self.platform_path):
            # self.platform_file = pd.read_csv(self.platform_path, sep="\t")
            pass
        else:
            with open(self.platform_path, mode="w", encoding="utf-8") as wr:
                wr.write(f"{_config.platform_name}\t{_config.parameter_name}\t{_config.version_name}\n")
                wr.write(f"Digital_Elisa\t{';'.join(_config.de_all)}\t1.0\n")
        self.platform_file = pd.read_csv(self.platform_path, sep="\t")

    def platform_change(self):
        while 1:
            # 展示方法并调用
            print(self.platform_file)
            # 提示用户输入
            _input = input("请输入要选择的序号，只输入Q退出：").strip()
            if not _input:
                print("不能输入空值~")
                continue
            if _input.upper() == "Q":
                return
            if _input.isdecimal() and int(_input) < self.platform_file.shape[0]:
                self.para_LTS.str = self.platform_file.loc[int(_input), _config.parameter_name]
                self.platform_row = int(_input)
                self.method_function(self.change_platform_dic)
                # todo 更新所有附属表

    @staticmethod
    def method_function(method_dic):
        while 1:
            # 展示方法并调用
            for i, method in enumerate(method_dic):
                print(i, " ", method)
            # 提示用户输入
            _input = input("请输入要选择的序号，只输入Q退出：").strip()
            if not _input:
                print("不能输入空值~")
                continue
            if _input.upper() == "Q":
                return
            if _input.isdecimal() and int(_input) < len(method_dic):
                func = list(method_dic.values())[int(_input)]()
                if func.upper() == "Q":
                    return "Q"
                if not func:
                    continue

    def show_iter(self, ite=None):
        if ite is None:
            ite = self.para_LTS.to_list
        method_dic = ite
        while 1:
            # 展示方法并调用
            for i, method in enumerate(method_dic):
                print(i, " ", method)
            # 提示用户输入
            _input = input("请输入要修改的序号，-1为最后，只输入Q退出：").strip()
            if not _input:
                print("不能输入空值~")
                continue
            if _input.upper() == "Q":
                return
            if _input.isdecimal() and int(_input) < len(method_dic) or _input == "-1":
                print(_input)
                return int(_input)

    def add_para(self):
        para_index = self.show_iter()
        para_name = input("请输入参数名：")
        if para_index != -1:
            self.para_LTS.to_list.insert(para_index, para_name)
        else:
            self.para_LTS.to_list.append(para_name)
        # 更新到表
        self.renew_plate_file()
        return "Q"

    def del_para(self):
        para_index = self.show_iter()

        self.para_LTS.to_list.pop(para_index)
        # 更新到表
        self.renew_plate_file()
        return "Q"

    def update_para(self):
        para_index = self.show_iter()
        para_name = input("请输入参数名：")
        self.para_LTS.to_list[para_index] = para_name
        # 更新到表
        self.renew_plate_file()
        return "Q"

    def select_para(self):
        self.show_iter()
        return "Q"

    def renew_plate_file(self):
        old_record = self.platform_file.iloc[self.platform_row]
        # 新版本
        self.platform_file.loc[self.platform_row, _config.parameter_name] = self.para_LTS.to_str
        self.platform_file.loc[self.platform_row, _config.version_name] += 1

        # 旧版本管理
        new_df = pd.DataFrame([old_record])
        new_df.index = new_df.index + self.platform_file.index[-1] + 1  # 设置新记录的索引
        self.platform_file = pd.concat([self.platform_file, new_df])
        self.platform_file.to_csv(self.platform_path, sep="\t", index=False)
        # todo 更新所有附属表 放这比较合适
