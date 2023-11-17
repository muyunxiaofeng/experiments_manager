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
    params_curve = "curve"
    params_sample = "sample"

    # 位置字典
    position_start_alpha = "position_start_alpha"
    position_start_digit = "position_start_digit"
    position_end_alpha = "position_end_alpha"
    position_end_digit = "position_end_digit"
    position_alpha = "position_alpha"
    position_digit = "position_digit"
    # 获取位置的字母部分
    re_alpha = "([A-Z]*)\d*"
    re_digit = "[A-Z]*(\d*)"
    # 全选
    all = "ALL"
    # direction
    sample_direction_dic = {
        "竖向点样，横向延伸，A1-H1，A2-H2": self._config.down_right,
        "横向点样，竖向延伸，A1-A12，B1-B12": self._config.right_down,
        "反向使用，竖向点样，横向延伸，H12-A12，H11-A11": self._config.up_left,
        "反向使用，横向点样，竖向延伸，H12-H1，G12-G1": self._config.left_up,
        "侧向使用，横向点样，竖向延伸，H1-A1，H2-A2": self._config.up_right,
        "侧向使用，竖向点样，横向延伸，H1-H12，G1-G12": self._config.right_up,
        "反向侧向使用，横向点样，竖向延伸，A12-H12，A11-H11": self._config.down_left,
        "反向侧向使用，竖向点样，横向延伸，A12-A1，B12-B1": self._config.left_down,
    }

    # "竖向点样，横向延伸，A1-H1，A2-H2": "down_right",
    down_right = "down_right"
    # "横向点样，竖向延伸，A1-A12，B1-B12": "right_down",
    right_down = "right_down"
    # "反向使用，竖向点样，横向延伸，H12-A12，H11-A11": "up_left",
    up_left = "up_left"
    # "反向使用，横向点样，竖向延伸，H12-H1，G12-G1": "left_up",
    left_up = "left_up"
    # "侧向使用，横向点样，竖向延伸，H1-A1，H2-A2": "up_right",
    up_right = "up_right"
    # "侧向使用，竖向点样，横向延伸，H1-H12，G1-G12": "right_up",
    right_up = "right_up"
    # "反向侧向使用，横向点样，竖向延伸，A12-H12，A11-H11": "down_left",
    down_left = "down_left"
    # "反向侧向使用，竖向点样，横向延伸，A12-A1，B12-B1": "left_down",
    left_down = "left_down"

    # items
    items_dict = {
        "p-Tau 217": "p-Tau 217",
        "Amyloid Beta 1-40": "Amyloid Beta 1-40",
        "Amyloid Beta 1-42": "Amyloid Beta 1-42"

    }
