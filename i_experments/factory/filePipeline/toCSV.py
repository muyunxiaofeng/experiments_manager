# -*- encoding: utf-8 -*-
"""
PyCharm toCSV
2022年10月28日
by Orochi
该文件目的
第一层

第二层

执行层

"""
import os

import pandas

from ..timeFactory.formatTime import FormatTimeTool
from . import settings


class ToCSV:

    def __init__(self):
        self.base_settings = settings.BaseSettings()
        if not os.path.exists(self.base_settings.QUICK_PATH):
            os.mkdir(self.base_settings.QUICK_PATH)

    def quickSave(self, title: list, content: list):

        if title is None:
            title = []

        path = self.base_settings.QUICK_PATH
        timeNum = FormatTimeTool.getFormatDateNum()
        tPath = path + "/" + timeNum + ".csv"

        with open(tPath, mode="a", encoding="utf-8") as wr:
            # title
            ti = ""
            for tit in title:
                ti += f"{tit}"
                ti += "\t"
            print(ti)
            ti += "\n"
            wr.write(ti)

            # content
            con = ""
            for i, info in enumerate(content):
                con += f"{info}"
                con += "\t"

                if ((i + 1) % len(title) == 0 and i != 0) or i == len(content) - 1:
                    con += "\n"
                    print(con)
                    wr.write(con)
                    con = ""

    def pandasSave(self, listDic, fileHeader="", sep="\t"):

        path = self.base_settings.QUICK_PATH
        timeNum = FormatTimeTool.getFormatDateNum()
        tPath_gbk = path + "/" + fileHeader + timeNum + "_gbk" + ".csv"
        tPath_utf8 = path + "/" + fileHeader + timeNum + "_utf8" + ".csv"

        df = pandas.DataFrame(list(listDic))
        df.to_csv(tPath_utf8, encoding="utf-8", mode="a", sep=sep)
        df.to_csv(tPath_gbk, encoding="gbk", mode="a", sep=sep)
