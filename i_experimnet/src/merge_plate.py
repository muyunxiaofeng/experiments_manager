# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
merge_plate	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/14	当前系统的年月日
16:04	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
14	当天
16	当前小时
04	当前分钟
18	当前秒钟
"""

from i_experimnet.src.bean.json_bean import Json_Bean
from i_experimnet.src.plate import Plate


class Merge_plates:
    def __init__(self, merge_list=None):
        # 初始化
        self.mp = Plate("finally")
        # 合并列表
        self.merge_list = merge_list
        if merge_list:
            self.merge_init(merge_list[0])
            self.merging()
        print(self.mp)

    def merge_init(self, plate: Plate):
        # 获取合并板的规格
        self.mp.plate = plate.plate
        # 进行初始化
        self.mp.make_plate()
        # 赋值
        self.mp.modify_plate.iloc[:, :] = "{}"
        print(self.mp)

    def merging(self):

        for _row in range(self.mp.row):
            for _col in range(self.mp.col):
                for plate in self.merge_list:
                    if _col == 0 and _row == 0:
                        print(plate)
                    # 获取值
                    v = plate.modify_plate.iloc[_row, _col]
                    # 获取引用
                    k = plate.plate_name
                    # 获取之前的json
                    _json = self.mp.modify_plate.iloc[_row, _col]
                    # 构建json_bean
                    jb = Json_Bean(_json)
                    # 插入参数
                    if isinstance(v, json):
                        jb.load_json_bean(v)
                    else:
                        jb.input_para(var_name=k, var_value=v)

                    self.mp.modify_plate.iloc[_row, _col] = jb.json_bean()

    def re_merging(self, path):
        """
        提供一个
        :param path:
        :return:
        """
        # 加载
        self.mp.load_excel(path)

        for _row in range(self.mp.row):
            for _col in range(self.mp.col):
                for plate in self.merge_list:
                    if _col == 0 and _row == 0:
                        print(plate)
                    # 获取值
                    v = plate.modify_plate.iloc[_row, _col]
                    # 获取引用
                    k = plate.plate_name
                    # 获取之前的json
                    _json = self.mp.modify_plate.iloc[_row, _col]
                    # 构建json_bean
                    jb = Json_Bean(_json)
                    # 插入参数  这里会将所有None不赋值
                    jb.repair_para(var_name=k, var_value=v)

                    self.mp.modify_plate.iloc[_row, _col] = jb.json_bean()
