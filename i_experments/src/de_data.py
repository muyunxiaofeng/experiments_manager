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
"""
import os
import shutil


class De_data:
    def __init__(self):
        path = "/Volumes/找幻影/2023-12-20 183554 实验1w5455/W54-7/result-20231220-1843"
        pass


if __name__ == '__main__':
    path = "/Volumes/找幻影/2023-12-20 183554 实验1w5455/W54-7/result-20231220-1843"
    path = "/"
    print(os.listdir(path))