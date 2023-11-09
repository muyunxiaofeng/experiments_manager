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

from i_experimnet.utils import plate_number
from i_experimnet.src.bean.json_bean import Json_Bean


class Layout:
    def __init__(self, plate=96):
        self.unit = None
        self.plate = plate
        self.template_plate = []
        self.current_plate = []

    def layout_init(self):
        """
        根据不同版型进行布板的初始化
        :return:
        """
        # 根据不同的版型选择不同的布板位置
        match self.plate:
            case 96:
                row = 8
                col = 12
            case "96T":
                row = 12
                col = 8
            case 12:
                row = 4
                col = 3
            case _:
                row = 8
                col = math.ceil(self.plate / 8)
        # 根据不同的布板位置生成【行坐标】和【纵坐标】
        row_num = [some_count.upper_row(index) for index in range(1, row + 1)]
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
        self.template_plate.loc()
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

    def layout(self):
        self.help_layout()

    def help_layout(self):
        """
        根据输入的布板信息进行
        :return:
        """
        while 1:
            print("例：", "a1-a3,a4,a5=0;b12=1000;(fg/mL);^curve=a1-h6;^sample=a7-h7,a7-h12")
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
                        self.set_value(sub_area, area_value)

                elif "^" in area_equation:
                    if "curve" in area_equation.lower():
                        # todo curve
                        pass
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
            position_start_alpha = re.findall("([a-z]*)\d*", position_start.lower())[0]
            # 获取数字部分
            position_start_digit = re.findall("[a-z]*(\d*)", position_start)[0]
            # 获取字母部分
            position_end_alpha = re.findall("([a-z]*)\d*", position_end.lower())[0]
            # 获取数字部分
            position_end_digit = re.findall("[a-z]*(\d*)", position_end)[0]
            return {
                "position_start_alpha": position_start_alpha,
                "position_start_digit": position_start_digit,
                "position_end_alpha": position_end_alpha,
                "position_end_digit": position_end_digit
            }
        else:
            # 获取字母部分
            position_alpha = re.findall("([a-z]*)\d*", area.lower())[0]
            # 获取数字部分
            position_digit = re.findall("[a-z]*(\d*)", area.lower())[0]
            return {
                "position_alpha": position_alpha,
                "position_digit": position_digit
            }

    def set_value(self, sub_area, area_value):
        self.modify_plate = self.current_plate.copy()
        self.modify_plate = pd.DataFrame()
        # 分割区域
        area_dict = self.area_split(sub_area)
        if len(area_dict) == 2:
            # 单点赋值
            # 呈现结果赋值
            self.current_plate.loc[area_dict["position_alpha"], area_dict["position_digit"]] = area_value
            # 获取位置信息
            coordinates = self.template_plate.loc[area_dict["position_alpha"], area_dict["position_digit"]]
            # 构建 json
            # 获取 modify 的值
            mj = self.modify_plate.loc[area_dict["position_alpha"], area_dict["position_digit"]]
            # 无论是不是空值都扔进去
            jb = Json_Bean(mj)
            # 赋值位置信息和值
            jb.input_para(var_name="position", var_value=coordinates)
            jb.input_para(var_value="value", var_name=area_value)
            # 将处理后的值赋回去
            self.modify_plate.loc[area_dict["position_alpha"], area_dict["position_digit"]] = jb.json_bean()

        else:
            # 区域赋值
            pass
