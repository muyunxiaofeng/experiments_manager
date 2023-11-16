# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
ttt	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/6	当前系统的年月日
13:49	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
06	当天
13	当前小时
49	当前分钟
24	当前秒钟
"""
import math

import string


def col(num, outline=""):
    if num == 0:
        return
    # print(len(string.ascii_lowercase)) # 26
    div, mod = divmod(num - 1, len(string.ascii_lowercase))

    outline += string.ascii_lowercase[mod]
    while div > 26:
        col(div, outline)
    else:
        if div != 0:
            outline += string.ascii_lowercase[div - 1]
    print(outline[::-1])
    return outline[::-1]



import pandas as pd

# 创建一个示例DataFrame
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

# 使用.iloc方法取出第1行和第3行的数据
selected_rows = df.iloc[[0, 2]]
print(selected_rows)