# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
layout_config	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/10	当前系统的年月日
13:08	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
10	当天
13	当前小时
08	当前分钟
12	当前秒钟
"""


class Layout_config:
    # 手工置顶
    params_position = "position"
    params_value = "value"

    # 位置字典
    position_start_alpha = "position_start_alpha"
    position_start_digit = "position_start_digit"
    position_end_alpha = "position_end_alpha"
    position_end_digit = "position_end_digit"
    position_alpha = "position_alpha"
    position_digit = "position_digit"
    # 获取位置的字母部分
    re_alpha = "([a-z]*)\d*"
    re_digit = "[a-z]*(\d*)"
    # 布板模板
    asc_96 = 96
    asc_96_row = 8
    asc_96_col = 12
    des_96 = "96T"
    des_96_row = 12
    des_96_col = 8
    asc_12 = 12
    asc_12_row = 4
    asc_12_col = 3
    # 默认行
    default_row = 8
