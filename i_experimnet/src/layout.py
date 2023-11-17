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

from datetime import datetime

from i_experimnet.src.merge_plate import Merge_plates
from i_experimnet.utils import alpha_calculator
from i_experimnet.config.layout_config import Layout_config
from i_experimnet.src.plate import Plate


class Layout:
    def __init__(self, plate=96):

        self.layout_version = "V1.0.0"
        # 中间储存的一些信息
        self.sample_from = None
        self.sample_type = None
        self.unit = None
        # result
        self.result = Merge_plates()
        # 版型
        self.plate = plate

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
        # 语句储存
        self.input_path = self._config.input_txt_path + r"\input-" + datetime.now().strftime(
            "%Y-%m-%d-%H-%M-%S") + "-" + self.layout_version + ".txt"
        # 启动函数
        self.layout()

    def layout(self):
        """
        调用的主流程
        :return:
        """
        # 初始化
        self.layout_init()
        # 输入
        self.help_layout()
        # 展示
        for plate in self.list_plate():
            print(plate)
        # 合并
        self.result.merge_list = self.list_plate()
        self.result.merging()
        # 保存
        self.layout_saving()

    def list_plate(self):
        """
        将所有属于Plate的实例以列表形式返回，便于merge
        :return:
        """
        # return [attrs for attr in dir(self) if isinstance(getattr(self, attr), Plate)]
        return [getattr(self, attr) for attr in dir(self) if isinstance(getattr(self, attr), Plate)]

    def layout_init(self):
        """
        初始化各种板子
        :return:
        """

        pass

    def layout_saving(self):
        """
        储存布板信息到本地
        V1.0.0 完成excel的储存
        :return:
        """
        # 储存到excel
        path = self._config.excel_saving_path
        prefix = r"\layout-"
        now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        suffix = ".xlsx"
        self.result.mp.modify_plate.to_excel(path + prefix + self.layout_version + "-" + now + suffix)

    def input_saving(self, _input):
        """
        为方便复用 储存为txt
        :param _input:
        :return:
        """
        with open(self.input_path, mode="a", encoding="utf-8") as wr:
            wr.write(_input)
            wr.write("\n")

    def help_layout(self):
        """
        根据输入的布板信息进行自动化梳理
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
            self.input_saving(_input)
            # 根据键入的内容分成不同的等式列表
            area_equation_list = _input.split(";")
            # 遍历等式进行分拣
            for area_equation in area_equation_list:
                # 单位unit 处理
                if "(" in area_equation:
                    unit, area = area_equation.split(":")
                    self.unit = re.findall("\((.*/.*)\)", area)
                    for sub_area in area.split(","):
                        self.set_values(sub_area=sub_area, area_value=self.unit,
                                        data_frame=self.unit_plate.modify_plate)
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
                            self.input_saving(item)
                            item_area = input("请输入项目范围，例：a1-a3,a4,a5，只输入Q退出：").strip().upper()
                            if not item_area:
                                print("不能输入空值~")
                                continue
                            if item_area.upper() == "Q":
                                return
                            else:
                                self.input_saving(item_area)
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
                            self.input_saving(sample_input)

                elif "*" in area_equation:
                    # todo 这里是要调取布板信息的
                    self.set_protocol()
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
                        self.set_values(sub_area=sub_area, area_value=self.sample_from,
                                        data_frame=self.sample_from_plate.modify_plate)
                        self.set_values(sub_area=sub_area, area_value=self.sample_type,
                                        data_frame=self.sample_type_plate.modify_plate)

                    self.set_sample()

    def set_values(self, sub_area, area_value, data_frame: Plate):
        """
        根据给定的区域和值进行赋值，并储存到给定的dataframe中
        :param sub_area: 选定的区域
        :param area_value: 该区域的值
        :param data_frame: 需要储存的dataframe 一般为modify——plate
        :return: None
        """
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
        """
        根据给定区域来分割，如果是A1这种单点区域则返回的字典坐标相同，如果是区域，则起始位置和终止位置的坐标会排序后给出
        :param area: 给定的区域
        :return: 输入区域的坐标索引int格式 可以用iloc来实现
        """
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
        """
        将键入的样本分割不同的信息，分别储存，并存在self.sample_list中
        :param samples: 样本输入信息
        :return:
        """
        # [sample_name<sample_number~6>sample_type%sample_from]sample_direction:h1-h7]
        prep_list = ["<", ">", "~", "%"]
        if not all(prep in samples for prep in prep_list):
            raise "输入有问题"
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
        self.sample_list = new_list
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
                self.input_saving(self.sample_direction)
                break

        # 将sample_direction 赋值给self中的值
        if not self.sample_direction:
            self.sample_direction = sample_direction
            self.input_saving(self.sample_direction)
        print(sample_direction)

    def sample_area_list(self, area):
        """
        将给定的区域根据“”方向“”进行列表化，储存在self.sample_position_list
        :param area: 给定的区域
        :return:
        """
        area_dict = self.area_split(area)
        # 修改值
        row_start = area_dict[self._config.position_start_alpha]
        row_end = area_dict[self._config.position_end_alpha]
        col_start = area_dict[self._config.position_start_digit]
        col_end = area_dict[self._config.position_end_digit]
        self.sample_position_list += getattr(self, self.sample_direction)(row_start=row_start, row_end=row_end,
                                                                          col_start=col_start, col_end=col_end)

    def set_sample(self):
        """
        根据已经序列化的self.sample_list和self.sample_position_list 进行赋值
        :return:
        """
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

    def set_protocol(self):
        """
        需要重写
        :return:
        """
        print(self.layout_version)
        return "None"

    def get_items_dict(self):
        return self._config.items_dict

    def down_right(self, row_start: int, row_end: int, col_start: int, col_end: int):
        """
        根据不同方向进行序列化
        "竖向点样，横向延伸，A1-H1，A2-H2": down_right,
        "横向点样，竖向延伸，A1-A12，B1-B12": right_down,
        "反向使用，竖向点样，横向延伸，H12-A12，H11-A11": up_left,
        "反向使用，横向点样，竖向延伸，H12-H1，G12-G1": left_up,
        "侧向使用，横向点样，竖向延伸，H1-A1，H2-A2": up_right,
        "侧向使用，竖向点样，横向延伸，H1-H12，G1-G12": right_up,
        "反向侧向使用，横向点样，竖向延伸，A12-H12，A11-H11": down_left,
        "反向侧向使用，竖向点样，横向延伸，A12-A1，B12-B1": left_down,
        :param row_start: 起始行
        :param row_end: 终止行
        :param col_start: 起始列
        :param col_end: 终止列
        :return: 序列化列表
        """
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
        """
        根据不同方向进行序列化
        "竖向点样，横向延伸，A1-H1，A2-H2": down_right,
        "横向点样，竖向延伸，A1-A12，B1-B12": right_down,
        "反向使用，竖向点样，横向延伸，H12-A12，H11-A11": up_left,
        "反向使用，横向点样，竖向延伸，H12-H1，G12-G1": left_up,
        "侧向使用，横向点样，竖向延伸，H1-A1，H2-A2": up_right,
        "侧向使用，竖向点样，横向延伸，H1-H12，G1-G12": right_up,
        "反向侧向使用，横向点样，竖向延伸，A12-H12，A11-H11": down_left,
        "反向侧向使用，竖向点样，横向延伸，A12-A1，B12-B1": left_down,
        :param row_start: 起始行
        :param row_end: 终止行
        :param col_start: 起始列
        :param col_end: 终止列
        :return: 序列化列表
        """
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
        """
        根据不同方向进行序列化
        "竖向点样，横向延伸，A1-H1，A2-H2": down_right,
        "横向点样，竖向延伸，A1-A12，B1-B12": right_down,
        "反向使用，竖向点样，横向延伸，H12-A12，H11-A11": up_left,
        "反向使用，横向点样，竖向延伸，H12-H1，G12-G1": left_up,
        "侧向使用，横向点样，竖向延伸，H1-A1，H2-A2": up_right,
        "侧向使用，竖向点样，横向延伸，H1-H12，G1-G12": right_up,
        "反向侧向使用，横向点样，竖向延伸，A12-H12，A11-H11": down_left,
        "反向侧向使用，竖向点样，横向延伸，A12-A1，B12-B1": left_down,
        :param row_start: 起始行
        :param row_end: 终止行
        :param col_start: 起始列
        :param col_end: 终止列
        :return: 序列化列表
        """
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
        """
        根据不同方向进行序列化
        "竖向点样，横向延伸，A1-H1，A2-H2": down_right,
        "横向点样，竖向延伸，A1-A12，B1-B12": right_down,
        "反向使用，竖向点样，横向延伸，H12-A12，H11-A11": up_left,
        "反向使用，横向点样，竖向延伸，H12-H1，G12-G1": left_up,
        "侧向使用，横向点样，竖向延伸，H1-A1，H2-A2": up_right,
        "侧向使用，竖向点样，横向延伸，H1-H12，G1-G12": right_up,
        "反向侧向使用，横向点样，竖向延伸，A12-H12，A11-H11": down_left,
        "反向侧向使用，竖向点样，横向延伸，A12-A1，B12-B1": left_down,
        :param row_start: 起始行
        :param row_end: 终止行
        :param col_start: 起始列
        :param col_end: 终止列
        :return: 序列化列表
        """
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
        """
        根据不同方向进行序列化
        "竖向点样，横向延伸，A1-H1，A2-H2": down_right,
        "横向点样，竖向延伸，A1-A12，B1-B12": right_down,
        "反向使用，竖向点样，横向延伸，H12-A12，H11-A11": up_left,
        "反向使用，横向点样，竖向延伸，H12-H1，G12-G1": left_up,
        "侧向使用，横向点样，竖向延伸，H1-A1，H2-A2": up_right,
        "侧向使用，竖向点样，横向延伸，H1-H12，G1-G12": right_up,
        "反向侧向使用，横向点样，竖向延伸，A12-H12，A11-H11": down_left,
        "反向侧向使用，竖向点样，横向延伸，A12-A1，B12-B1": left_down,
        :param row_start: 起始行
        :param row_end: 终止行
        :param col_start: 起始列
        :param col_end: 终止列
        :return: 序列化列表
        """
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
        """
        根据不同方向进行序列化
        "竖向点样，横向延伸，A1-H1，A2-H2": down_right,
        "横向点样，竖向延伸，A1-A12，B1-B12": right_down,
        "反向使用，竖向点样，横向延伸，H12-A12，H11-A11": up_left,
        "反向使用，横向点样，竖向延伸，H12-H1，G12-G1": left_up,
        "侧向使用，横向点样，竖向延伸，H1-A1，H2-A2": up_right,
        "侧向使用，竖向点样，横向延伸，H1-H12，G1-G12": right_up,
        "反向侧向使用，横向点样，竖向延伸，A12-H12，A11-H11": down_left,
        "反向侧向使用，竖向点样，横向延伸，A12-A1，B12-B1": left_down,
        :param row_start: 起始行
        :param row_end: 终止行
        :param col_start: 起始列
        :param col_end: 终止列
        :return: 序列化列表
        """
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
        """
        根据不同方向进行序列化
        "竖向点样，横向延伸，A1-H1，A2-H2": down_right,
        "横向点样，竖向延伸，A1-A12，B1-B12": right_down,
        "反向使用，竖向点样，横向延伸，H12-A12，H11-A11": up_left,
        "反向使用，横向点样，竖向延伸，H12-H1，G12-G1": left_up,
        "侧向使用，横向点样，竖向延伸，H1-A1，H2-A2": up_right,
        "侧向使用，竖向点样，横向延伸，H1-H12，G1-G12": right_up,
        "反向侧向使用，横向点样，竖向延伸，A12-H12，A11-H11": down_left,
        "反向侧向使用，竖向点样，横向延伸，A12-A1，B12-B1": left_down,
        :param row_start: 起始行
        :param row_end: 终止行
        :param col_start: 起始列
        :param col_end: 终止列
        :return: 序列化列表
        """
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
        """
        根据不同方向进行序列化
        "竖向点样，横向延伸，A1-H1，A2-H2": down_right,
        "横向点样，竖向延伸，A1-A12，B1-B12": right_down,
        "反向使用，竖向点样，横向延伸，H12-A12，H11-A11": up_left,
        "反向使用，横向点样，竖向延伸，H12-H1，G12-G1": left_up,
        "侧向使用，横向点样，竖向延伸，H1-A1，H2-A2": up_right,
        "侧向使用，竖向点样，横向延伸，H1-H12，G1-G12": right_up,
        "反向侧向使用，横向点样，竖向延伸，A12-H12，A11-H11": down_left,
        "反向侧向使用，竖向点样，横向延伸，A12-A1，B12-B1": left_down,
        :param row_start: 起始行
        :param row_end: 终止行
        :param col_start: 起始列
        :param col_end: 终止列
        :return: 序列化列表
        """
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
