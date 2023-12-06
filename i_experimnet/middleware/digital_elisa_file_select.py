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

from i_experimnet.config.middle_ware_config import Digital_elisa_file_select_config as _config


class Digital_Elisa_file_select:
    def __init__(self, path=None):
        if path is None:
            path = _config.default_path

        self.path = path
        self.keyword = "result"
        # 目标文件夹下的路径及绝对路径
        


