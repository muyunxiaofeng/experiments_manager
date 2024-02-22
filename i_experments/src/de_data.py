# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
de_data	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/1/22	当前系统的年月日
01:34	当前系统的时分秒
2024	当前年份
01	当前月份（形式：07）
1月	当前月份（形式：7月）
一月	当前月份（形式：七月）
22	当天
01	当前小时
34	当前分钟
29	当前秒钟

1.
"""
import concurrent.futures
import os
import re
import shutil

import pandas
import pandas as pd

from i_experments.config.src_config import De_data_config as _config
from i_experments.utils.threading_safe_list import ThreadSafeList


class De_data:
    def __init__(self, final_path):
        self.version = "de_data_V1.0.0"
        # path = "/Users/frozensword/Downloads/SQL必知必会/副本Excel-1-7-20231227-1522.xlsx"
        self.path = "/Volumes"
        self.final_path = final_path
        self.result_list = list()
        self.result_walk(self.final_path)
        print(self.result_list)
        # 要处理的xlsx
        self.handle_xlsx = ThreadSafeList()
        self.collect_xlsx()
        # test read xlsx
        excel = pd.read_excel(self.handle_xlsx.get()[0])
        print(excel)
        yx = excel[excel["图片编号"] == "有效图合计"]
        print(yx)
        # todo
        # yx_list = yx.to_list()
        # # print(yx_list)
        # yxl = yx.to
        # print(yxl)
        yx_dic = yx.to_dict()
        print(yx_dic)
        ygs = excel["荧光数"]
        print(ygs)
        numpy_ygs = ygs.to_numpy()
        sumygs = numpy_ygs.sum()
        print(sumygs)


    def collect_xlsx(self):
        """
        多线程的查找xlsl
        :return:
        """
        with concurrent.futures.ThreadPoolExecutor(os.cpu_count()) as executor:
            futures = {executor.submit(self.only_excel, future) for future in self.result_list}
            completed, pending = concurrent.futures.wait(futures)
            print(completed)
            print(pending)
            for future in concurrent.futures.as_completed(futures):
                print(future.result())
        print("self.handle_xlsx", self.handle_xlsx.get())

    def result_walk(self, root_path):
        """
        根据config中的result。re进行查找目标文件夹下的文件
        :param root_path:
        :return:
        """
        for root, folder_list, file_list in os.walk(root_path):
            for file in file_list:
                file_abs_path = os.path.join(root, file)
                if re.findall(_config.result_re, file_abs_path):
                    self.result_list.append(file_abs_path)

    def only_excel(self, _path):
        if _path.endswith(".xls") or _path.endswith(".xlsx"):
            self.handle_xlsx.add(_path)
            return "chengong"
