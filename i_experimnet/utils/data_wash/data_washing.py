# -*- coding:utf-8 -*-
"""
experiments_manager	项目名
PyCharm	集成开发环境
data_washing	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/4	当前系统的年月日
13:01	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
04	当天
13	当前小时
01	当前分钟
23	当前秒钟

对于多组数据的处理的类：
1. 离散型数值的清理
"""
import inspect

import numpy as np


class Data_washing:
    def __init__(self, data=None):
        self.origin_data = data
        self.washed_data = None
        self.washed_method = None

    def iqr(self):
        data = self.origin_data
        if type(data) = list
        data = np.array(data)

        if len(data.shape) == 0:  # if data is a scalar
            return np.percentile(data, 75) > data > np.percentile(data, 25)
        else:  # if data is an array
            data_sorted = np.sort(data)
            q25, q75 = np.percentile(data_sorted, 25), np.percentile(data_sorted, 75)
            iqr = q75 - q25
            lower, upper = q25 - 1.5 * iqr, q75 + 1.5 * iqr
            self.washed_method = inspect.currentframe().f_code.co_name
            return lower < data < upper
