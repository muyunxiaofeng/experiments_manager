# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
loading_info_from_excel	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/17	当前系统的年月日
15:17	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
17	当天
15	当前小时
17	当前分钟
01	当前秒钟
"""
import os.path
import shutil
from datetime import datetime

import pandas as pd
from openpyxl import workbook

from i_experimnet.config.info_config import Info_config as _config


class Excel_info:
    def __init__(self):
        # 参数的dataframe
        self.params_df = None
        # 储存跟库的字典及dataframe
        self.root_dict = None
        self.root = None
        # 加载/初始化根表
        self.rooting()

    def rooting(self):
        if not os.path.exists(_config.root_file):
            if not os.path.exists(_config.root_path + _config.info):
                os.makedirs(_config.root_path + _config.info)
            wb = workbook.Workbook()
            wb.save(_config.root_file)
        # 初始化加载目录的根表
        self.root = pd.read_excel(_config.root_file, index_col=0)
        # 如果是空的就新建一个出来
        if self.root.empty:
            self.root = pd.DataFrame(columns=['items', 'path'])
            return
        # 便于查询转化为dictionary
        self.root_dict = self.root.to_dict()
        return self.root

    def __root_add(self, items, path):
        """
        向根表中加入项目名称的私有方法
        :param items: 项目名
        :param path: 项目储存的路径
        :return: None
        """
        if not os.path.exists(_config.root_file):
            os.makedirs(_config.root_file)
        # 刷新根表
        self.root = pd.read_excel(_config.root_file, index_col=0)
        # 构建新数据行的字典
        new_dict = {
            "items": [items], "path": [path]
        }
        # 末尾追加项目
        if self.root.empty:
            self.root = pd.DataFrame(new_dict, columns=['items', 'path'])
        else:
            # 创建一个新的行数据
            new_data = pd.DataFrame(new_dict, columns=['items', 'path'])
            # 使用append()函数将新数据添加到DataFrame的末尾
            self.root = pd.concat([self.root, new_data], ignore_index=True)
        # 项目去重
        self.root.drop_duplicates(inplace=True)
        # 打印项目根表
        print(self.root)
        # 储存根表
        self.root.to_excel(_config.root_file)
        # 加载字典方便实例中使用
        self.root_dict = self.root.to_dict()

    def params_add(self, item, *args, **kwargs):
        """
        添加不定个数的项目类型
        比如
        protocol DA = 0.5  DA_unit = μg/mL CA = 20  CA_unit = μg/10 mg beads beads_add = 7 add_unit = μL
        e.params_add("protocol", DA="0.5 μg/mL")  # {'DA': '0.5 μg/mL'}
        :param item: 项目名
        :param args: 列表参数
        :param kwargs: 字典参数
        :return: 无
        """
        # 拼接新生成表的路径
        new_path = "".join([_config.root_path, _config.info, f"{item}.xlsx"])
        # 当前时间，并准备进行备份
        now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        back_path = "".join(
            [_config.root_path, _config.info, _config.backup, f"{now}-{item}.xlsx"])

        print(kwargs)
        # 输入的字符转化为字符串
        for kwarg in kwargs:
            kwargs[kwarg] = f"{kwargs[kwarg]}"
        # 如果已经存在在目录列表中
        # 查找'item'的行号
        row_number = self.root[self.root['items'] == item]
        if row_number.empty:
            # 如果没有表就新建一个
            # 新建一个空表
            self.params_df = pd.DataFrame(columns=list(kwargs.keys()))
            # 一个新的数据
            new_data = pd.DataFrame([list(kwargs.values())], columns=list(kwargs.keys()))
            # 拼接数据
            self.params_df = pd.concat([self.params_df, new_data], ignore_index=True)
            # 新建数据表
            self.__root_add(item, new_path)
        else:
            # 如果已经存在了
            # 获取储存过的路径
            path = row_number.loc[0, "path"]

            # 打开历史存储的参数
            self.params_df = pd.read_excel(path, index_col=0)

            # 撰写新的 data 优先遵从列表导入
            if args:
                new_data = pd.DataFrame(args, columns=self.params_df.columns)
            else:
                new_data = pd.DataFrame([list(kwargs.values())], columns=self.params_df.columns)
            # 合并新旧数据
            self.params_df = pd.concat([self.params_df, new_data], ignore_index=True)
            # 备份旧数据
            shutil.copy2(new_path, back_path)

        # 去重
        self.params_df.drop_duplicates(inplace=True, keep="first")
        # 打印新表
        print(self.params_df.to_string())
        # 保存
        self.params_df.to_excel(new_path)
        print(new_data)
        return new_data

    def params_select(self, item):
        """
        根据根表查询一个列表 进行选择项目 并查询该项目对应的表
        :param item: 查询的表
        :return:
        """
        # 如果已经存在在目录列表中
        # 查找'item'的行号
        row_number = self.root[self.root['items'] == item]
        if row_number.empty:
            return
        else:
            # 如果已经存在了
            # 获取储存过的路径
            path = row_number.loc[0, "path"]
            # 打开历史存储的参数
            self.params_df = pd.read_excel(path, index_col=0)
            return self.params_df
