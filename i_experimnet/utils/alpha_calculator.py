# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
alpha_calculator	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/11	当前系统的年月日
13:33	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
11	当天
13	当前小时
33	当前分钟
18	当前秒钟
"""
import re
import string


def alpha_calculator(alpha, power=0, value=0):
    # 将输入的字符转化为小写
    alpha = alpha.lower()
    test_alpha = re.findall("[a-z]*", alpha)[0]
    if alpha != test_alpha:
        print("包含其他非字母字符")
        raise Exception
    if len(alpha) == 1:
        value += (string.ascii_lowercase.index(alpha) + 1) * pow(26, power)

    else:
        beta = alpha[-1]
        gamma = alpha[:-1]

        value += (string.ascii_lowercase.index(beta) + 1) * pow(26, power)
        value = alpha_calculator(alpha=gamma, power=power + 1, value=value)
    return value

