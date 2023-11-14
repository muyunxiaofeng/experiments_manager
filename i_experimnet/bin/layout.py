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

import re

from i_experimnet.utils import alpha_calculator
from i_experimnet.config.layout_config import Layout_config
from i_experimnet.src.plate import Plate


class Layout:
    def __init__(self, plate=96):
        # result
        self.result = Merge_plate()

        # 参数
        self.unit_plate = None
        self.values_plate = None
        self.plate_list = [
            self.unit_plate,
            self.values_plate,
            self.modify_plate,
        ]
        # 版型
        self.plate = plate

        # 一些字符串参数
        self._config = Layout_config()

        # 参数赋值的时候的辅助参数
        self._col = None
        self._row = None
        self.parameter = None

        # 启动函数
        self.layout()

    def layout(self):
        self.layout_init()
        self.help_layout()

    def layout_init(self):
        """
        初始化各种板子
        :return:
        """

        # 数值的模板
        self.values_plate = Plate("value", self.plate)
        # 单位的模板
        self.unit_plate = Plate("unit", self.plate)

    def help_layout(self):
        """
        根据输入的布板信息进行
        :return:
        """
        while 1:
            print("例：", "a1-a3,a4,a5=0;b12=1000;(fg/mL);",
                  "^curve=a1-h6;^sample=a7-h7,a7-h12;{1}=a1-h2;",
                  "[sample_name<sample_number~6>sample_type%sample_from:h1-h7]")
            _input = input("请输入位置信息，用区域间用分号隔开，只输入Q退出：").strip()
            if not _input:
                print("不能输入空值~")
                continue
            if _input.upper() == "Q":
                return
            # 转成大写
            _input = _input.upper()
            # 根据键入的内容分成不同的等式列表
            area_equation_list = _input.split(";")
            # 遍历等式进行分拣
            for area_equation in area_equation_list:
                # 单位unit 处理
                if "(" in area_equation:
                    pass
                    # self.unit = re.findall("\((.*/.*)\)", area_equation)
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
                        self.set_values(sub_area, area_value, self.values_plate.modify_plate)
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

    def set_values(self, sub_area, area_value, data_frame: Plate):
        if sub_area == self._config.all:
            row_start = 0
            row_end = data_frame.row
            col_start = 0
            col_end = data_frame.col
        else:
            # 构建区域字典
            area_dict = self.area_split(sub_area)
            # 修改值
            row_start = area_dict[self._config.position_start_alpha]
            row_end = area_dict[self._config.position_end_alpha]
            col_start = area_dict[self._config.position_start_digit]
            col_end = area_dict[self._config.position_end_digit]
        # 修改
        data_frame.iloc[row_start - 1:row_end, col_start - 1:col_end] = area_value

    def area_split(self, area):
        if "-" in area:
            position_start, position_end = area.split("-")
            # 获取字母部分
            position_start_alpha = re.findall(self._config.re_alpha, position_start.upper())[0].strip()
            # 获取数字部分
            position_start_digit = re.findall(self._config.re_digit, position_start)[0].strip()
            # 获取字母部分
            position_end_alpha = re.findall(self._config.re_alpha, position_end.upper())[0].strip()
            # 获取数字部分
            position_end_digit = re.findall(self._config.re_digit, position_end)[0].strip()
            # 转化为数字
            position_start_alpha = alpha_calculator.alpha_calculator(position_start_alpha)
            position_end_alpha = alpha_calculator.alpha_calculator(position_end_alpha)
            # pea永远大于psa
            if position_start_alpha > position_end_alpha:
                position_start_alpha, position_end_alpha = position_end_alpha, position_start_alpha
            return {
                self._config.position_start_alpha: position_start_alpha,
                self._config.position_start_digit: int(position_start_digit),
                self._config.position_end_alpha: position_end_alpha,
                self._config.position_end_digit: int(position_end_digit)
            }
        else:
            # 获取字母部分
            position_start_alpha = re.findall(self._config.re_alpha, area.upper())[0].strip()
            # 获取数字部分
            position_start_digit = re.findall(self._config.re_digit, area.upper())[0].strip()
            # 转化
            position_start_alpha = alpha_calculator.alpha_calculator(position_start_alpha)
            return {
                self._config.position_start_alpha: position_start_alpha,
                self._config.position_start_digit: int(position_start_digit),
                self._config.position_end_alpha: position_start_alpha,
                self._config.position_end_digit: int(position_start_digit)
            }

    def sample_split(self, samples):
        # sample_name<sample_number~6>sample_type%sample_from
        # 样本分拆 样本名 “<”
        sample_name_prefix, samples = samples.split("<")
        # 样本编号 ~
        samples_start, samples = samples.split("~")
        # 样本类型 >
        samples_end, samples = samples.split(">")
        # 数字化
        samples_start = int(samples_start)
        samples_end = int(samples_end)
        # 样本来源 %
        sample_type, sample_from = samples.split("%")
