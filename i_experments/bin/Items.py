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
import os.path

import pandas as pd

from i_experments.utils.excel_load import Loading_excel
from i_experments.utils.output_excel import Output_excel
from i_experments.config.bin_config import items_config as _config


class Items:
    def __init__(self):
        print("items")
        # 输出辅助
        self.oe = Output_excel()
        # 初始化items文件
        self.items_initializing()

    def items_initializing(self):
        if not os.path.exists(_config.items_files):
            self.create_items()
        else:
            items_file = Loading_excel(_config.items_files)

            print(items_file.excel["items"])

    def create_items(self):
        items = []
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
                continue
        cols = []
        while 1:
            _input = input("请输入列名，只输入Q退出：").strip()
            if not _input:
                print("不能输入空值~")
                continue
            if _input.upper() == "Q":
                print("cols:", cols)
                break
            else:
                cols.append(_input)
                continue
        col = _config.items_base + cols
        _ = {
            "items": items,
            "columns": [json.dumps(col)]
        }
        print(_)
        self.oe.write_a_dic(_, _config.items_files)
