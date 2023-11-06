# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
some_count	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/6	当前系统的年月日
16:35	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
06	当天
16	当前小时
35	当前分钟
28	当前秒钟
"""
import string


def row(num, outline=""):
    if num == 0:
        raise Exception

        # print(len(string.ascii_lowercase)) # 26
    div, mod = divmod(num - 1, len(string.ascii_lowercase))

    outline += string.ascii_lowercase[mod]
    while div > 26:
        row(div, outline)
    else:
        if div != 0:
            outline += string.ascii_lowercase[div - 1]
    return outline[::-1]
