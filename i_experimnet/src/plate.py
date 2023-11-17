# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
plate	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/14	当前系统的年月日
14:08	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
14	当天
14	当前小时
08	当前分钟
50	当前秒钟
"""
import math
from pprint import pprint

import pandas as pd

from i_experimnet.config import plate_config
from i_experimnet.utils import plate_number, alpha_calculator


class Plate:
    def __init__(self, name, plate=96):
        # 配置文件加载
        self._config = plate_config.Plate_config()
        # 命名
        self.plate_name = name
        # 版型
        self.plate = plate
        # 板的行列
        self.col = None
        self.row = None
        # 位置模板
        self.position_plate = []
        # 空板
        self.empty_plate = []

        # 制作空白板
        self.make_plate()
        # 结果储存的位置
        self.modify_plate = self.empty_plate.copy()

    def make_plate(self):
        """
        根据不同版型进行布板的初始化
        :return:
        """
        # 位置模板
        self.position_plate = []
        # 空板
        self.empty_plate = []
        # 根据不同的版型选择不同的布板位置
        match self.plate:
            case self._config.asc_96:
                row = self._config.asc_96_row
                col = self._config.asc_96_col
            case self._config.des_96:
                row = self._config.des_96_row
                col = self._config.des_96_col
            case self._config.asc_12:
                row = self._config.asc_12_row
                col = self._config.asc_12_col
            case _:
                row = self._config.default_row
                col = math.ceil(self.plate / self._config.default_row)
        # 同步
        self.row = row
        self.col = col
        # 根据不同的布板位置生成【行坐标】和【纵坐标】
        row_num = [plate_number.upper_row(index) for index in range(1, row + 1)]
        col_num = list(range(1, col + 1))
        # 生成空行——row和位置行——row——position
        for row_i in row_num:
            _row = [None for _ in col_num]
            _row_position = [row_i + f"{col_i}" for col_i in col_num]
            # 加入到本行
            self.empty_plate.append(_row)
            self.position_plate.append(_row_position)
        # 转化成dataframe
        self.empty_plate = pd.DataFrame(self.empty_plate, index=row_num, columns=col_num)
        self.position_plate = pd.DataFrame(self.position_plate, index=row_num, columns=col_num)

    def __str__(self):
        print()
        print("=" * 20, self.plate_name, "=" * 20)
        pprint(self.modify_plate)
        return "Plate class"

    def load_excel(self, path):
        self.modify_plate = pd.read_excel(path, index_col=0)
