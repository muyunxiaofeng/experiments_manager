# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
Process_theardings	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/1/26	当前系统的年月日
19:48	当前系统的时分秒
2024	当前年份
01	当前月份（形式：07）
1月	当前月份（形式：7月）
一月	当前月份（形式：七月）
26	当天
19	当前小时
48	当前分钟
35	当前秒钟
"""
import multiprocessing
import concurrent.futures


class Process_threading:
    def __init__(self):
        pass

    @staticmethod
    def func(arg1, arg2, arg3, arg4):
        print(f"Thread {arg1} is running, args: {arg1}, {arg2}, {arg3}, {arg4}")
        # Do something...

    @staticmethod
    def main():
        # 创建多进程
        processes = []
        for i in range(multiprocessing.cpu_count()):
            p = multiprocessing.Process(target=worker)
            p.start()
            processes.append(p)
        for p in processes:
            p.join()

    @staticmethod
    def worker():
        # 创建线程池
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # 提交任务到线程池
            futures = [executor.submit(func, i, 'arg2', 'arg3', 'arg4') for i in range(5)]
            for future in concurrent.futures.as_completed(futures):
                print(f"Future {future.result()} has completed")
