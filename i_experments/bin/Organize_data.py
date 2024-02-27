# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
Organize_data	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/1/24	当前系统的年月日
22:05	当前系统的时分秒
2024	当前年份
01	当前月份（形式：07）
1月	当前月份（形式：7月）
一月	当前月份（形式：七月）
24	当天
22	当前小时
05	当前分钟
21	当前秒钟
"""
import os

from i_experments.bin.Items import Items
from i_experments.src.de_data import De_data
from i_experments.utils.show_method_dic import Show_dic
from i_experments.config.bin_config import organize_data_config as _config


class Organize_data:
    def __init__(self):
        self.final_path = None
        print("Organize_data")
        self.version = "Organize_data V1.0.0"
        self.items = Items(instance=True)
        self.platform_func_dic = _config.platform_func
        self.organize_guide()

    def organize_guide(self):
        # select path
        self.select_path(_config.volumes_path)
        # # select platform
        # self.items.platform_initializing()
        # # select items
        # self.items.items_initializing()
        # print(self.items.item_info)
        index, platform_name = Show_dic().show_iter(self.platform_func_dic)
        # 文件整理
        platform_name(self.final_path)

    def select_path(self, _path):
        num, value = Show_dic.show_iter(os.listdir(_path))
        if value == "Q":
            self.final_path = _path
            return
        final_path = os.path.join(_path, value)
        self.select_path(final_path)
