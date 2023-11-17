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

from i_experimnet.bin.merge_plate import Merge_plates
from i_experimnet.utils import alpha_calculator
from i_experimnet.config.layout_config import Layout_config
from i_experimnet.src.plate import Plate


class Layout:
    def __init__(self, plate=96):
        # 中间储存的一些信息
        self.sample_from = None
        self.sample_type = None

        # result
        self.result = Merge_plates()

        # 参数
        # 数值的模板
        self.values_plate = Plate("value", self.plate)
        # 布板类型的模板
        self.type_plate = Plate("type", self.plate)
        # 单位的模板
        self.unit_plate = Plate("unit", self.plate)
        # 样本布板
        self.sample_plate = Plate("samples", self.plate)
        self.sample_from_plate = Plate("sample_from", self.plate)
        self.sample_type_plate = Plate("sample_type", self.plate)
        # 项目
        self.items_plate = Plate("items_plate", self.plate)

        # 版型
        self.plate = plate

        # 一些字符串参数
        self._config = Layout_config()

        # 参数赋值的时候的辅助参数
        self._col = None
        self._row = None
        self.parameter = None
        # 样本储存列表
        self.sample_list = list()
        # 样本布板方向
        self.sample_direction = None
        # 样本位置的储存列表
        self.sample_position_list = list()
        # 启动函数
        self.layout()

    def layout(self):
        self.layout_init()
        self.help_layout()
        for plate in self.list_plate():
            print(plate)

    def list_plate(self):
        # return [attrs for attr in dir(self) if isinstance(getattr(self, attr), Plate)]
        return [getattr(self, attr) for attr in dir(self) if isinstance(getattr(self, attr), Plate)]

    def layout_init(self):
        """
        初始化各种板子
        :return:
        """

        pass

    def help_layout(self):
        """
        根据输入的布板信息进行
        :return:
        """
        while 1:
            print("例：", "a1-a3,a4,a5=0;b12=1000;(fg/mL);",
                  "^curve:a1-h6;^sample:a7-h7,a7-h12;{进入分散样本命名方法};",
                  "[sample_name<sample_number~6>sample_type%sample_from]sample_direction:h1-h7;")
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
                        self.set_values(sub_area, self._config.params_curve, self.type_plate.modify_plate)

                elif "^" in area_equation:
                    # 选择项目
                    # 目前的版本V1.0.0 先写在config中
                    item_dict = self.get_items_dict()
                    item = None
                    item_area = None
                    while 1:
                        # 展示方法并调用
                        for i, method in enumerate(item_dict):
                            print(i, " ", method)
                        # 提示用户输入
                        item_num = input("请输入要选择的序号，只输入Q退出：").strip()
                        if not item_num:
                            print("不能输入空值~")
                            continue
                        if item_num.upper() == "Q":
                            return
                        if item_num.isdecimal() and int(item_num) < len(item_dict):
                            item = list(item_dict.values())[int(item_num)]
                            item_area = input("请输入项目范围，例：a1-a3,a4,a5，只输入Q退出：").strip()
                            if not item_area:
                                print("不能输入空值~")
                                continue
                            if item_area.upper() == "Q":
                                return
                            else:
                                break
                    if item is not None and item_area is not None:
                        sub_area_list = item_area.split(",")
                        # 遍历列表进行处理
                        for sub_area in sub_area_list:
                            self.set_values(sub_area, item, self.items_plate.modify_plate)

                elif "{" in area_equation:
                    # 暂存样本列表
                    while 1:

                        # 提示用户输入
                        sample_input = input("请输入样本序号，只输入Q退出：").strip()
                        if not sample_input:
                            print("不能输入空值~")
                            continue
                        if sample_input.upper() == "Q":
                            print(self.sample_list)
                            break
                        elif sample_input.isdecimal():
                            self.sample_list.append(sample_input)

                elif "*" in area_equation:
                    # todo 这里是要调取布板信息的
                    pass
                elif "[" in area_equation:
                    # 将赋值部分进行处理
                    samples, area = area_equation.split(":")
                    # [] 列表化
                    sub_area_list = area.split(",")
                    # 样本处理
                    self.sample_split(samples)
                    # 遍历列表进行处理
                    for sub_area in sub_area_list:
                        self.sample_area_list(sub_area)
                        self.set_values(sub_area=sub_area, area_value=self._config.params_sample,
                                        data_frame=self.type_plate.modify_plate)

                    self.set_sample()

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
        print(data_frame)

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
        # [sample_name<sample_number~6>sample_type%sample_from:sample_direction=h1-h7]
        # 样本分拆 样本名 “<”
        sample_name_prefix, samples = samples.split("<")
        # 样本编号 ~
        samples_start, samples = samples.split("~")
        # 样本类型 >
        samples_end, samples = samples.split(">")
        # 数字化
        if samples_start and samples_end:
            samples_start = int(samples_start)
            samples_end = int(samples_end)
            self.sample_list += [sample_i for sample_i in range(samples_start, samples_end + 1)]
        new_list = list()
        for sample_name in self.sample_list:
            new_list.append(f"{sample_name_prefix}-{sample_name}")
        # 样本来源 %
        sample_type, samples = samples.split("%")
        self.sample_type = sample_type
        # 样本命名方向 ：
        sample_from, sample_direction = samples.split("]")
        self.sample_from = sample_from
        # 为了保证选择正确  需要提示下输入方向
        sample_direction_dic = self._config.sample_direction_dic
        while 1:
            # 展示方法并调用
            for i, method in enumerate(sample_direction_dic):
                print(i, " ", method)
            # 提示用户输入
            _input = input("请输入要选择的序号，只输入Q退出：").strip()
            if not _input:
                print("不能输入空值~")
                continue
            if _input.upper() == "Q":
                return
            if _input.isdecimal() and int(_input) < len(sample_direction_dic):
                self.sample_direction = list(sample_direction_dic.values())[int(_input)]
                break

        # 将sample_direction 赋值给self中的值
        if not self.sample_direction:
            self.sample_direction = sample_direction
        print(sample_direction)

    def sample_area_list(self, area):
        area_dict = self.area_split(area)
        # 修改值
        row_start = area_dict[self._config.position_start_alpha]
        row_end = area_dict[self._config.position_end_alpha]
        col_start = area_dict[self._config.position_start_digit]
        col_end = area_dict[self._config.position_end_digit]
        self.sample_position_list += getattr(self, self.sample_direction)(row_start=row_start, row_end=row_end,
                                                                          col_start=col_start, col_end=col_end)

    def set_sample(self):
        _len = len(self.sample_list)
        length = len(self.sample_position_list)
        if _len > length:
            self.sample_list = self.sample_list[0:len(self.sample_position_list)]
        elif _len < length:
            self.sample_list += ["None_name" for _ in range(length - _len)]
        for i in range(length):
            self.set_values(sub_area=self.sample_position_list[i],
                            area_value=self.sample_list[i],
                            data_frame=self.sample_plate.modify_plate
                            )

    def get_items_dict(self):
        return self._config.items_dict

    def down_right(self, row_start: int, row_end: int, col_start: int, col_end: int):
        # 获取位置信息
        position_plate = self.list_plate()[0].position_plate
        # 获取列表 想先取竖向 那就把竖向的列表化
        col_range = [i for i in range(col_start - 1, col_end)]
        # 返回值初始化
        position_list = list()
        for col_index in col_range:
            # 获取位置信息
            position_list += position_plate.iloc[row_start - 1:row_end, col_index].values.tolist()
        return position_list

    def up_left(self, row_start: int, row_end: int, col_start: int, col_end: int):
        # 获取位置信息
        position_plate = self.list_plate()[0].position_plate
        # 获取列表 想先取竖向 那就把竖向的列表化
        col_range = [i for i in range(col_start - 1, col_end)][::-1]
        # 返回值初始化
        position_list = list()
        for col_index in col_range:
            # 获取位置信息
            position_list += position_plate.iloc[row_start - 1:row_end, col_index].values.tolist()[::-1]
        return position_list

    def left_up(self, row_start: int, row_end: int, col_start: int, col_end: int):
        # 获取位置信息
        position_plate = self.list_plate()[0].position_plate
        # 获取列表 想先取竖向 那就把竖向的列表化
        row_range = [i for i in range(row_start - 1, row_end)][::-1]
        # 返回值初始化
        position_list = list()
        for row_index in row_range:
            # 获取位置信息
            position_list += position_plate.iloc[row_index, col_start - 1:col_end].values.tolist()[::-1]
        return position_list

    def right_down(self, row_start: int, row_end: int, col_start: int, col_end: int):
        # 获取位置信息
        position_plate = self.list_plate()[0].position_plate
        # 获取列表 想先取竖向 那就把竖向的列表化
        row_range = [i for i in range(row_start - 1, row_end)]
        # 返回值初始化
        position_list = list()
        for row_index in row_range:
            # 获取位置信息
            position_list += position_plate.iloc[row_index, col_start - 1:col_end].values.tolist()
        return position_list

    def up_right(self, row_start: int, row_end: int, col_start: int, col_end: int):
        # 获取位置信息
        position_plate = self.list_plate()[0].position_plate
        # 获取列表 想先取竖向 那就把竖向的列表化 right 不用反  left 反  down不用反  up反
        col_range = [i for i in range(col_start - 1, col_end)]
        # 返回值初始化
        position_list = list()
        for col_index in col_range:
            # 获取位置信息
            position_list += position_plate.iloc[row_start - 1:row_end, col_index].values.tolist()[::-1]
        return position_list

    def right_up(self, row_start: int, row_end: int, col_start: int, col_end: int):
        # 获取位置信息
        position_plate = self.list_plate()[0].position_plate
        # 获取列表 想先取竖向 那就把竖向的列表化 right 不用反  left 反  down不用反  up反
        row_range = [i for i in range(row_start - 1, row_end)][::-1]
        # 返回值初始化
        position_list = list()
        for row_index in row_range:
            # 获取位置信息
            position_list += position_plate.iloc[row_index, col_start - 1:col_end].values.tolist()
        return position_list

    def down_left(self, row_start: int, row_end: int, col_start: int, col_end: int):
        # 获取位置信息
        position_plate = self.list_plate()[0].position_plate
        # 获取列表 想先取竖向 那就把竖向的列表化 right 不用反  left 反  down不用反  up反
        col_range = [i for i in range(col_start - 1, col_end)][::-1]
        # 返回值初始化
        position_list = list()
        for col_index in col_range:
            # 获取位置信息
            position_list += position_plate.iloc[row_start - 1:row_end, col_index].values.tolist()
        return position_list

    def left_down(self, row_start: int, row_end: int, col_start: int, col_end: int):
        # 获取位置信息
        position_plate = self.list_plate()[0].position_plate
        # 获取列表 想先取竖向 那就把竖向的列表化 right 不用反  left 反  down不用反  up反
        row_range = [i for i in range(row_start - 1, row_end)]
        # 返回值初始化
        position_list = list()
        for row_index in row_range:
            # 获取位置信息
            position_list += position_plate.iloc[row_index, col_start - 1:col_end].values.tolist()[::-1]
        return position_list
