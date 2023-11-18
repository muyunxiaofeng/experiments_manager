# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
loading_info_from_excel	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/17	当前系统的年月日
15:17	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
17	当天
15	当前小时
17	当前分钟
01	当前秒钟
"""
import pandas as pd

from i_experimnet.config.info_config import Info_config as _config


class Excel_info:
    def __init__(self):
        self.root = None

    def root_add(self, items, path):
        self.root = pd.read_excel(_config.root_file)
        if self.root.empty:
            self.root = pd.DataFrame(columns=['items', 'path'])
        # 创建一个新的行数据
        new_data = pd.Series([items, path])

        # 使用append()函数将新数据添加到DataFrame的末尾
        df = self.root.append(new_data)
        print(df)
        print(self.root)


if __name__ == '__main__':
    e = Excel_info()
    e.root_add(1, 2)
