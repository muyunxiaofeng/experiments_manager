# -*- encoding: utf-8 -*-
"""
PyCharm formatTime
2022年10月28日
by Orochi
该文件目的
第一层

第二层

执行层

"""
import time


class FormatTimeTool:
    @staticmethod
    def get_format_time():
        return time.strftime("%Y年%m月%d日 %H.%M.%S", time.localtime())

    @staticmethod
    def getFormatDate():
        return time.strftime("%Y年%m月%d日", time.localtime())

    @staticmethod
    def getFormatDateNum():
        return time.strftime("%Y%m%d%H", time.localtime())

    @staticmethod
    def getFormatTimeNum():
        return time.strftime("%Y-%m-%d.%H-%M-%S", time.localtime())

    @staticmethod
    def getFormatTimeDatabase():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
