# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
de_output	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/2/24	当前系统的年月日
14:10	当前系统的时分秒
2024	当前年份
02	当前月份（形式：07）
2月	当前月份（形式：7月）
二月	当前月份（形式：七月）
24	当天
14	当前小时
10	当前分钟
31	当前秒钟
"""
import pandas

from i_experments.config.bin_config import de_info


def de_out():
    with open("./file/deinfo.csv", mode="w", encoding="utf-8") as wr:
        for info in de_info.de_all:
            wr.write(info)
            wr.write("\n")
def de_oto():
    csv = pandas.read_csv("./deinfo.csv")
    df = pd.DataFrame([de_info.de_all, ['B', 'B'], ['C', 5], ['D', 4]],
                      columns=['col_1', 'col_2'],
                      index=list('abcd'))
    print(csv.T)


if __name__ == '__main__':
    # de_out()
    de_oto()