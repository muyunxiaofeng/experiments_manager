# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
"Items	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/1/18	当前系统的年月日
22:31	当前系统的时分秒
2024	当前年份
01	当前月份（形式：07）
1月	当前月份（形式：7月）
一月	当前月份（形式：七月）
18	当天
22	当前小时
31	当前分钟
13	当前秒钟
"""
import json
import pprint
import os.path
from collections.abc import Iterable

import pandas as pd

from i_experments.config.bin_config import de_info
from i_experments.utils.excel_load import Loading_excel
from i_experments.utils.output_excel import Output_excel
from i_experments.config.bin_config import items_config as _config
from i_experments.utils.show_method_dic import Show_dic


class Items:
    def __init__(self):
        self.items_file = None
        self.version = "V1.0.1"
        print("items")
        # 输出辅助
        self.oe = Output_excel()
        # 初始化items文件
        self.items_initializing()

    def items_initializing(self):
        """
        items的界面展示方法
        v1.1：新增项目
        v1.2：根据flag确定是否重写items文件
        :return:
        """
        if not os.path.exists(_config.items_files):
            items_list = []
            print("没有可用项目")
            flag = False
        else:
            self.items_file = Loading_excel(_config.items_files).excel
            items_list = self.items_file["items"].to_list()
            print(self.items_file["items"])
            flag = True
        # v2.0 允许user新建
        while 1:
            _input = input(
                "请输入要选择的序号，输入N新建,D加序号删除，U加序号更新，输入R从头开始写入，只输入Q退出：").strip()
            if not _input:
                print("不能输入空值~")
                continue
            if _input.upper() == "Q":
                return
            if _input.upper()[0] == "D":
                if _input.upper()[1:].isdecimal() and int(_input[1:]) < len(items_list):
                    self.del_items(int(_input[1:]))
            if _input.upper()[0] == "U":
                if _input.upper()[1:].isdecimal() and int(_input[1:]) < len(items_list):
                    self.update_items(int(_input[1:]))
            if _input.upper() == "R":
                self.add_items(flag=False)
            if _input.upper() == "N":
                self.add_items(flag=True)
                self.items_file = Loading_excel(_config.items_files).excel
                items_list = self.items_file["items"].to_list()
                print(self.items_file["items"])
            if flag and _input.isdecimal() and int(_input) < len(items_list):
                select_item = items_list[int(_input)]
                print(select_item)
                item_info = self.items_file[self.items_file[_config.col_items] == select_item]
                pprint.pprint(item_info.to_string(index=False))

    def new_items(self):
        """
        公共的输入item方法
        包括新建和新增
        规范用户输入的唯一途径
        :return:
        """
        items = list()
        while 1:
            _input = input("请输入项目名称，只输入Q退出：").strip()
            if not _input:
                print("不能输入空值~")
                continue
            if _input.upper() == "Q":
                print("items:", items)
                break
            else:
                items.append(_input)
                break
        # cols = de_info.items_base
        cols = list()
        while 1:
            _input = input("请输入列名,输入D进入数据库选择，只输入Q退出：").strip()
            print("_input", _input)
            print("cols", cols)
            if not _input:
                print("不能输入空值~")
                continue
            if _input.upper() == "Q":
                cols = list(set(cols))
                print("cols:")
                pprint.pprint(cols)
                break
            if _input.upper() == "D":
                while 1:
                    cols_ref = self.format_dic()
                    _, select_cols = Show_dic.show_iter(cols_ref)
                    if select_cols == "Q":
                        break
                    cols += select_cols
                continue
            else:
                cols.append(_input)
                continue

        _ = {
            _config.col_items: items,
            _config.col_columns: [json.dumps(cols)],
            _config.col_version: [self.version]
        }
        return _

    @staticmethod
    def format_dic():
        cols_default = dict(de_info.__dict__)
        cols_dic = dict()
        for k in cols_default:
            if isinstance(cols_default[k], Iterable):
                cols_dic[k] = cols_default[k]

        return cols_dic

    def add_items(self, flag):
        """
        增加项目
        :param flag: 如果是flase 就重写
        :return:
        """
        if not os.path.exists(_config.items_files) or not flag:
            new_item = self.new_items()
            self.oe.write_a_dic(new_item, _config.items_files)
        else:
            old_items = Loading_excel(_config.items_files).excel
            new_item = self.new_items()
            # 拼接
            self.oe.add_a_record(old_items, new_item, _config.items_files)

    def del_items(self, index):
        """
        删除项目
        :return:
        """
        self.items_file = self.items_file.drop(index)
        self.oe.only_save_df(self.items_file, _config.items_files)

    def update_items(self, index):
        """
        更改项目
        :return:
        """
        items_columns_col = self.items_file[_config.col_columns]
        origin_info_df = items_columns_col.iloc[index]
        info = json.loads(origin_info_df)
        select_index, _ = Show_dic.show_iter(info)
        while 1:
            _input = input("请输入要改的值，只输入Q退出：").strip()
            if not _input:
                print("不能输入空值~")
                continue
            if _input.upper() == "Q":
                return
            else:
                info[select_index] = _input
                break
        self.items_file.loc[index, _config.col_columns] = json.dumps(info)
        print(self.items_file.loc[index, _config.col_columns])
        self.oe.only_save_df(self.items_file, _config.items_files)
