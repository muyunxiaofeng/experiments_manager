# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
advance_para_manager	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/2/24	当前系统的年月日
15:00	当前系统的时分秒
2024	当前年份
02	当前月份（形式：07）
2月	当前月份（形式：7月）
二月	当前月份（形式：七月）
24	当天
15	当前小时
00	当前分钟
28	当前秒钟
"""


class Advanced_parameters_manager:
    def __init__(self, parameter):
        self.parameter = parameter


    def add_para(self, flag, file_path):
        """
        增加para
        :param flag: 如果是flase 就重写
        :return:
        """
        if not os.path.exists(file_path) or not flag:
            with open(file_path, mode="w", encoding="utf_8") as wr:
                wr.write(self.parameter)
        else:
            pass

