# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
test	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/1/21	当前系统的年月日
16:32	当前系统的时分秒
2024	当前年份
01	当前月份（形式：07）
1月	当前月份（形式：7月）
一月	当前月份（形式：七月）
21	当天
16	当前小时
32	当前分钟
36	当前秒钟
"""

import pandas as pd

# 创建一个示例DataFrame
data = {'name': ['张三', '李四', '王五', '赵六'],
        'age': [25, 30, 35, 40],
        'city': ['北京', '上海', '深圳', '广州']}
df = pd.DataFrame(data)

# 将第三行name列改为"李四"  
df.loc[2, 'name'] = '李四'

# 打印修改后的DataFrame
print(df)