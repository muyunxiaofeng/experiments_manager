# -*- coding:utf-8 -*-
"""
experiments_manager	项目名
PyCharm	集成开发环境
data_washing	文件名
41379	用户名（指登录电脑的那个用户名）
2023/11/4	当前系统的年月日
13:01	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
04	当天
13	当前小时
01	当前分钟
23	当前秒钟

对于多组数据的处理的类：
1. 离散型数值的清理
"""
import numpy as np


class Data_washing:
    def __init__(self):
        pass

    import numpy as np
    from scipy.stats import zscore

    # 生成示例数据
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # 计算四分位数范围（IQR）
    q25, q75 = np.percentile(data, [25, 75])
    iqr = q75 - q25

    # 计算Z-score
    z_scores = zscore(data)

    # 定义格鲁布斯临界值表，可根据需要调整显著性水平
    alpha = 0.05
    critical_values = [1.4826, 1.7576, 2.0565, 2.3801, 2.7345, 3.1174, 3.5300, 3.9746, 4.4528, 5.0000]

    # 根据Z-score判断异常值
    outliers = []
    for i in range(len(z_scores)):
        if abs(z_scores[i]) > critical_values[int(iqr / 0.25 * alpha)]:
            outliers.append(data[i])

    import numpy as np

    def grubbs_test(data):
        """
        Grubbs test for outliers detection.

        Parameters:
            data (list): A list of numerical data.

        Returns:
            list: A list of outliers. If there are no outliers, return an empty list.
        """
        # Sort the data in ascending order.
        sorted_data = sorted(data)
        n = len(sorted_data)

        # Calculate the mean and standard deviation.
        mean = np.mean(sorted_data)
        std = np.std(sorted_data)

        # Initialize the outlier list.
        outliers = []

        # Calculate the Grubbs test statistic for each data point.
        for i in range(1, n - 1):
            x = sorted_data[i]
            mx = sorted_data[0] + (i - 1) * (mean - sorted_data[0]) / (n - 1)
            sx = np.sqrt((n - i) * variance(sorted_data[0:i]) + (i - 1) * variance(sorted_data[i:n]))
            t = abs(x - mx) / sx
            if t >= np.sqrt(2 / n):
                outliers.append(x)

        return outliers


    