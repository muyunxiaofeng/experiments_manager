# -*- coding:utf-8 -*-
"""
experiment_Digital_Elisa	项目名
PyCharm	集成开发环境
layout	文件名
41379	用户名（指登录电脑的那个用户名）
2023/10/24	当前系统的年月日
17:04	当前系统的时分秒
2023	当前年份
10	当前月份（形式：07）
10月	当前月份（形式：7月）
十月	当前月份（形式：七月）
24	当天
17	当前小时
04	当前分钟
59	当前秒钟
layout_init 初始化布板方法

"""
import math
import re
import string
import numpy as np
import pandas as pd

from i_experimnet.utils import plate_number, alpha_calculator
from i_experimnet.config.layout_config import Layout_config
from i_experimnet.src.bean.json_bean import Json_Bean


class Layout:
    def __init__(self, plate=96):
        # 一些字符串参数

        self.modify_plate = None
        self._config = Layout_config()
        self.unit = None
        self.plate = plate
        self.template_plate = []
        self.current_plate = []
        # 参数赋值的时候的辅助参数
        self._col = None
        self._row = None
        self.parameter = None

    def layout(self):
        self.help_layout()

    def layout_init(self):
        """
        根据不同版型进行布板的初始化
        :return:
        """
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
        # 根据不同的布板位置生成【行坐标】和【纵坐标】
        row_num = [plate_number.upper_row(index) for index in range(1, row + 1)]
        col_num = list(range(1, col + 1))
        # 生成空行——row和位置行——row——position
        for row_i in row_num:
            _row = [None for _ in col_num]
            _row_position = [row_i + f"{col_i}" for col_i in col_num]
            # 加入到本行
            self.current_plate.append(_row)
            self.template_plate.append(_row_position)
        # 转化成dataframe
        self.current_plate = pd.DataFrame(self.current_plate, index=row_num, columns=col_num)
        self.template_plate = pd.DataFrame(self.template_plate, index=row_num, columns=col_num)
        """
        初始化结果
             1   2   3   4   5   6   7   8   9    10   11   12
        A  A1  A2  A3  A4  A5  A6  A7  A8  A9  A10  A11  A12
        B  B1  B2  B3  B4  B5  B6  B7  B8  B9  B10  B11  B12
        C  C1  C2  C3  C4  C5  C6  C7  C8  C9  C10  C11  C12
        D  D1  D2  D3  D4  D5  D6  D7  D8  D9  D10  D11  D12
        E  E1  E2  E3  E4  E5  E6  E7  E8  E9  E10  E11  E12
        F  F1  F2  F3  F4  F5  F6  F7  F8  F9  F10  F11  F12
        G  G1  G2  G3  G4  G5  G6  G7  G8  G9  G10  G11  G12
        H  H1  H2  H3  H4  H5  H6  H7  H8  H9  H10  H11  H12
        
        
        Ran 1 test in 0.026s
        
        OK
             1     2     3     4     5     6     7     8     9     10    11    12
        A  None  None  None  None  None  None  None  None  None  None  None  None
        B  None  None  None  None  None  None  None  None  None  None  None  None
        C  None  None  None  None  None  None  None  None  None  None  None  None
        D  None  None  None  None  None  None  None  None  None  None  None  None
        E  None  None  None  None  None  None  None  None  None  None  None  None
        F  None  None  None  None  None  None  None  None  None  None  None  None
        G  None  None  None  None  None  None  None  None  None  None  None  None
        H  None  None  None  None  None  None  None  None  None  None  None  None
                
        """

    def help_layout(self):
        """
        根据输入的布板信息进行
        :return:
        """
        while 1:
            print("例：", "a1-a3,a4,a5=0;b12=1000;(fg/mL);^curve=a1-h6;^sample=a7-h7,a7-h12;{1}=a1-h2")
            _input = input("请输入位置信息，用区域间用分号隔开，只输入Q退出：").strip()
            if not _input:
                print("不能输入空值~")
                continue

            if _input.upper() == "Q":
                return
            # 根据键入的内容分成不同的等式列表
            area_equation_list = _input.split(";")
            # 遍历等式进行分拣
            for area_equation in area_equation_list:
                # 单位unit 处理
                if "(" in area_equation:
                    self.unit = re.findall("\((.*/.*)\)", area_equation)
                    # todo 进行所有试验孔的单位分配  但是现在可能没有处理完布板信息 所以要在最后 放置一个end_layout 完成这个功能
                # 布板信息的基础内容
                # 等式左边为区域 区域列表  右侧为  值  不含单位
                elif "=" in area_equation:
                    # 将赋值部分进行处理
                    area, area_value = area_equation.split("=")
                    # [] 列表化
                    sub_area_list = area.split(",")
                    # 遍历列表进行处理
                    for sub_area in sub_area_list:
                        self.set_value_position(sub_area, area_value)

                elif "^" in area_equation:
                    if "curve" in area_equation.lower():
                        # 将赋值部分进行处理
                        area, area_value = area_equation.split("=")
                        # [] 列表化
                        sub_area_list = area.split(",")
                        # 遍历列表进行处理
                        for sub_area in sub_area_list:
                            self.set_area_to_many_values(sub_area, area_value, parameter=self._config.params_curve)
                        # todo curve
                    elif "sample" in area_equation.lower():
                        # todo sample
                        pass
                elif "{" in area_equation:
                    # todo 这里是要调取布板信息的
                    pass

            return

    def area_split(self, area):
        if "-" in area:
            position_start, position_end = area.split("-")
            print(position_start)
            # 获取字母部分
            position_start_alpha = re.findall(self._config.re_alpha, position_start.lower())[0]
            # 获取数字部分
            position_start_digit = re.findall(self._config.re_digit, position_start)[0]
            # 获取字母部分
            position_end_alpha = re.findall(self._config.re_alpha, position_end.lower())[0]
            # 获取数字部分
            position_end_digit = re.findall(self._config.re_digit, position_end)[0]
            return {
                self._config.position_start_alpha: position_start_alpha,
                self._config.position_start_digit: int(position_start_digit),
                self._config.position_end_alpha: position_end_alpha,
                self._config.position_end_digit: int(position_end_digit)
            }
        else:
            # 获取字母部分
            position_alpha = re.findall(self._config.re_alpha, area.lower())[0]
            # 获取数字部分
            position_digit = re.findall(self._config.re_digit, area.lower())[0]
            return {
                self._config.position_alpha: position_alpha,
                self._config.position_digit: int(position_digit)
            }

    def set_value_position(self, sub_area, area_value):
        """
        多个范围对应一个值
        :param sub_area:
        :param area_value:
        :return:
        """
        self.modify_plate = self.current_plate.copy()
        # 分割区域
        area_dict = self.area_split(sub_area)
        if len(area_dict) == 2:
            # 单点赋值
            # 呈现结果赋值
            self.current_plate.loc[
                area_dict[self._config.position_alpha], area_dict[self._config.position_digit]] = area_value
            # 获取位置信息
            # todo 将参数字典抽出来放在 config 中
            coordinates = self.template_plate.loc[
                area_dict[self._config.position_alpha], area_dict[self._config.position_digit]]
            params_dict = {
                self._config.params_position: coordinates,
                self._config.params_value: area_value
            }
            self.change_modify_plate(row=area_dict[self._config.position_alpha],
                                     col=area_dict[self._config.position_digit],
                                     params_dict=params_dict)
        else:
            # # 区域赋值
            # if area_dict[self._config.position_start_alpha] == area_dict[self._config.position_end_alpha]:
            #     if area_dict[self._config.position_start_digit] == area_dict[self._config.position_end_digit]:
            #         # 神经病级别的单点赋值而已 所以代码同单点赋值
            #         # 呈现结果赋值
            #         self.current_plate.loc[
            #             area_dict[self._config.position_start_alpha],
            #             area_dict[self._config.position_start_digit]] = area_value
            #         # 获取位置信息
            #         coordinates = self.template_plate.loc[
            #             area_dict[self._config.position_start_alpha],
            #             area_dict[self._config.position_start_digit]]
            #         params_dict = {
            #             self._config.params_position: coordinates,
            #             self._config.params_value: area_value
            #         }
            #         # 真实布板的赋值
            #         self.change_modify_plate(
            #             row=area_dict[self._config.position_start_alpha],
            #             col=area_dict[self._config.position_start_digit],
            #             params_dict=params_dict
            #         )
            #     else:
            #         # 对一行进行赋值  获取的是列号
            #         # 行相同字母不同
            #         # 先要判定大小
            #         if self._config.position_start_digit > self._config.position_end_digit:
            #             # 如果是反的 则调换位置
            #             self._config.position_start_digit, self._config.position_end_digit = \
            #                 self._config.position_end_digit, self._config.position_start_digit
            #
            #         # 赋值
            #         self.current_plate.loc[
            #             area_dict[self._config.position_start_alpha],
            #             area_dict[self._config.position_start_digit:self._config.position_end_digit]] = area_value
            #         # 构造参数字典的参数字典
            #         kw = {
            #             self._config.params_position: self.param_position,
            #             self._config.params_value: self.param_value
            #         }
            #         self.batch_change_modify_plate(
            #             row_start=area_dict[self._config.position_start_alpha],
            #             row_end=area_dict[self._config.position_end_alpha],
            #             col_start=area_dict[self._config.position_start_digit],
            #             col_end=area_dict[self._config.position_end_digit],
            #             para=area_value,
            #             **kw
            #         )
            # else:
            # 先要判定大小
            if self._config.position_start_digit > self._config.position_end_digit:
                # 如果是反的 则调换位置
                self._config.position_start_digit, self._config.position_end_digit = \
                    self._config.position_end_digit, self._config.position_start_digit

            # 赋值
            self.current_plate.loc[
                area_dict[self._config.position_start_alpha],
                area_dict[self._config.position_start_digit:self._config.position_end_digit]] = area_value
            # 构造参数字典的参数字典
            kw = {
                self._config.params_position: self.param_position,
                self._config.params_value: self.param_value
            }
            self.batch_change_modify_plate(
                row_start=area_dict[self._config.position_start_alpha],
                row_end=area_dict[self._config.position_end_alpha],
                col_start=area_dict[self._config.position_start_digit],
                col_end=area_dict[self._config.position_end_digit],
                para=area_value,
                **kw
            )

    def set_area_to_many_values(self, sub_area, area_values, parameter):
        """
        根据输入的参数输入参数可以将参数修改
        :param sub_area:
        :param area_values:
        :param parameter:
        :return:
        """
        self.modify_plate = self.current_plate.copy()
        # 分割区域
        area_dict = self.area_split(sub_area)
        value_dict = self.area_split(area_values)

        # 先要判定大小
        if self._config.position_start_digit > self._config.position_end_digit:
            # 如果是反的 则调换位置
            self._config.position_start_digit, self._config.position_end_digit = \
                self._config.position_end_digit, self._config.position_start_digit
        # 让前缀相等
        if value_dict[self._config.position_start_alpha] != value_dict[self._config.position_end_alpha]:
            value_dict[self._config.position_end_alpha] = value_dict[self._config.position_start_alpha]
        # 生成名称列表
        if value_dict[self._config.position_start_digit] < value_dict[self._config.position_end_digit]:
            param_values_list = [f"{value_dict[self._config.position_start_alpha]} - {num}" for num in
                                 range(self._config.position_start_digit, self._config.position_end_digit + 1)]
        else:
            param_values_list = [f"{value_dict[self._config.position_start_alpha]} - {num}" for num in
                                 range(self._config.position_start_digit, self._config.position_end_digit + 1, -1)]
        # 将字母转化为数字
        row_start = alpha_calculator.alpha_calculator(area_dict[self._config.position_start_alpha])
        row_end = alpha_calculator.alpha_calculator(area_dict[self._config.position_end_alpha])
        col_start = area_dict[self._config.position_start_digit]
        col_end = area_dict[self._config.position_end_digit]
        # 比较大小反向则倒置
        if row_start > row_end:
            row_start, row_end = row_end, row_start
        if col_start > col_end:
            col_start, col_end = col_end, col_start
        index = 0
        for _col in range(col_start, col_end + 1):
            for _row in range(row_start, row_end + 1):
                self._row = _row
                self._col = _col
                # 构造参数字典的参数字典
                para_dict = {
                    parameter: self.param_value
                }
                self.batch_change_modify_plate(
                    row_start=_row,
                    row_end=_row,
                    col_start=_col,
                    col_end=_col,
                    para=param_values_list[index],
                    parameter=self.param_value
                    # **para_dict
                )

    def change_modify_plate(self, row, col, params_dict: dict, **kwargs):
        # 构建 json,
        # 获取 modify 的值
        mj = self.modify_plate.loc[row, col]
        # 无论是不是空值都扔进去
        jb = Json_Bean(mj)
        # 赋值位置信息和值
        for param in params_dict:
            jb.input_para(var_name=param, var_value=params_dict[param])

        # 将处理后的值赋回去
        self.modify_plate.loc[row, col] = jb.json_bean()

    def batch_change_modify_plate(self, row_start, row_end, col_start, col_end, para, **kwargs):
        # 将字母转化为数字
        row_start = alpha_calculator.alpha_calculator(row_start)
        row_end = alpha_calculator.alpha_calculator(row_end)
        # 比较大小反向则倒置
        if row_start > row_end:
            row_start, row_end = row_end, row_start
        if col_start > col_end:
            col_start, col_end = col_end, col_start
        for _col in range(col_start, col_end + 1):
            for _row in range(row_start, row_end + 1):
                self._row = _row
                self._col = _col
                self.parameter = para
                params_dict = dict()
                print(kwargs)
                for kwarg in kwargs:
                    # {kwarg => self._config.params_position
                    # kwargs[kwarg] => self.param_position >>>()
                    params_dict[kwarg] = kwargs[kwarg]()

                # 逐个修改参数
                self.change_modify_plate(
                    row=_row, col=_col,
                    params_dict=params_dict
                )

    """
    参数方法的分界线
    
    """

    def param_position(self):
        """
        返回这个点的坐标值
        :return:
        """
        return self.template_plate.loc[self._row, self._col]

    def param_value(self):
        """
        返回这个点的值
        :return:
        """
        return self.parameter
