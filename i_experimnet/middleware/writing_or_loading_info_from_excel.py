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
import shutil

import pandas as pd

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
        # 初始化加载目录的根表
        self.root = pd.read_excel(_config.root_file, index_col=0)
        # 如果是空的就新建一个出来
        if self.root.empty:
            self.root = pd.DataFrame(columns=['items', 'path'])
        # 便于查询转化为dictionary
        self.root_dict = self.root.to_dict()

    def __root_add(self, items, path):
        """
        向根表中加入项目名称的私有方法
        :param items: 项目名
        :param path: 项目储存的路径
        :return: None
        """
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
        self.root.drop_duplicates()
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
        if item in list(self.root_dict.keys()):
            self.params_df = pd.read_excel(self.root_dict[item], index_col=0)
            new_data = pd.DataFrame(list(kwargs.values()), columns=self.params_df.columns)
            self.params_df = pd.concat([self.params_df, new_data], ignore_index=True)
            self.__root_add(item, new_path)
            shutil.copy2(new_path, back_path)
        else:
            if args:
                self.params_df = pd.DataFrame(args, columns=list(kwargs.keys()))
            else:
                self.params_df = pd.DataFrame(list(kwargs.values()), columns=list(kwargs.keys()))
        print(self.params_df)
        self.params_df.to_excel(new_path)

    def params_select(self, item):
        pass
