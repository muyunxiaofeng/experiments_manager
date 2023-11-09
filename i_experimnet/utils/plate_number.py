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
import math
import string


def upper_row(num, outline=""):
    """
    一个26进制的字母排序 等同于excel的列名 列名都用的大写字母
    :param num: 列的个数
    :param outline: 输出的列名的倒置
    :return: 输出的列名
    """
    # 不存在小于1的列
    if num <= 0:
        raise Exception
    else:
        num = math.ceil(num)
    # 本位为mod  下一位的计算div递归给自己
    div, mod = divmod(num - 1, len(string.ascii_uppercase))
    # 本位计算出的数值储存在outline中
    outline += string.ascii_uppercase[mod]
    # 计算下一位
    while div > 26:
        upper_row(div, outline)
    else:
        if div != 0:
            outline += string.ascii_uppercase[div - 1]
    return outline[::-1]


def lower_row(num, outline=""):
    """
    一个26进制的字母排序 等同于excel的列名 列名都用的小写字母
    :param num: 列的个数
    :param outline: 输出的列名的倒置
    :return: 输出的列名
    """
    # 不存在小于1的列
    if num <= 0:
        raise Exception
    else:
        num = math.ceil(num)
    # 本位为mod  下一位的计算div递归给自己
    div, mod = divmod(num - 1, len(string.ascii_lowercase))
    # 本位计算出的数值储存在outline中
    outline += string.ascii_lowercase[mod]
    # 计算下一位
    while div > 26:
        lower_row(div, outline)
    else:
        if div != 0:
            outline += string.ascii_lowercase[div - 1]
    return outline[::-1]
