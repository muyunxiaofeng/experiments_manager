# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
main	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/17	当前系统的年月日
15:26	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
17	当天
15	当前小时
26	当前分钟
03	当前秒钟
"""
import os
import sys

# 将根目录放到python解释器中
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from i_experimnet.bin.modify_info import Modify_info
from i_experimnet.bin.digital_elisa import Digital_Elisa
from i_experimnet.utils.method_function import method_function

methods = {
    "信息编辑": Modify_info,
    "进入数字Elisa布板": Digital_Elisa,
}

if __name__ == '__main__':
    method_function(methods)
