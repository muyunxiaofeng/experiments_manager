# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
ewfads	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/18	当前系统的年月日
10:09	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
18	当天
10	当前小时
09	当前分钟
35	当前秒钟
"""
import pandas as pd

# 创建一个 DataFrame
df = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']},
    index=[0, 1, 2, 3])

# 创建新的行
new_row = pd.Series(['A4', 'B4', 'C4', 'D4'], index=['A', 'B', 'C', 'D'])

# 使用 append 方法添加新的行
df = df.append(new_row, ignore_index=True)

# 打印 DataFrame
print(df.to_string())