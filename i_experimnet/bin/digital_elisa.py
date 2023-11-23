# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
digital_elisa	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/9	当前系统的年月日
9:24	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
09	当天
09	当前小时
24	当前分钟
15	当前秒钟
"""
from i_experimnet.src.layout import Layout
from i_experimnet.middleware.writing_or_loading_info_from_excel import Excel_info


class Digital_Elisa(Layout):
    def __init__(self):
        # 常规引导布板
        super().__init__()
        # protocol
        # self.protocol_plate = Plate("protocol", self.plate)
        # 加载储存过的表格
        self.saving_list = Excel_info()
        # 特殊引导布板
        self.guidance()

    def show_saving_dataframe(self):
        if self.saving_list.rooting() is None:
            return
        else:
            return self.saving_list.root

    def guidance(self):
        if self.show_saving_dataframe() is None:
            self.new_params()
        else:
            self.select_params()

    def new_params(self):
        kwargs = dict()
        last_param = None
        while 1:

            # 提示用户输入
            param = input("请输入需要新增的表的名称，只输入Q退出：").strip()
            if not param:
                print("不能输入空值~")
                continue
            if param.upper() == "Q":
                param = last_param
                break
            last_param = param
        while 1:

            # 展示方法并调用
            for i, method in enumerate(kwargs):
                print(i, " ", method)
            # 提示用户输入列名
            arg = input("需要的分类，只输入Q退出：").strip()
            if not arg:
                print("不能输入空值~")
                continue
            if arg.upper() == "Q":
                break
            else:
                # 提示客户输入值
                value = input(arg + ":").strip()
                if not value:
                    print("不能输入空值~")
                    continue
                else:
                    kwargs[arg] = value

        self.saving_list.params_add(item=param, **kwargs)

    def select_params(self):
        while 1:
            root_dataframe = self.saving_list.root
            print(root_dataframe["items"])

            # 提示用户输入
            _input = input("请输入要选择的序号，只输入Q退出：").strip()
            if not _input:
                print("不能输入空值~")
                continue
            if _input.upper() == "Q":
                return
            if _input.isdecimal() and int(_input) < root_dataframe.shape[0]:
                select_item = root_dataframe.loc[int(_input), "items"]
                print(select_item)
                self.saving_list.params_select(s)
