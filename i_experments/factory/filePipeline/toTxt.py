# -*- encoding: utf-8 -*-
"""
PyCharm toTxt
2022年10月28日
by Orochi
该文件目的
第一层

第二层

执行层

"""
import os.path
from ..timeFactory.formatTime import FormatTimeTool
from . import settings


class ToTXT:
    def __init__(self):
        self.base_settings = settings.BaseSettings()
        if not os.path.exists(self.base_settings.QUICK_PATH):
            os.mkdir(self.base_settings.QUICK_PATH)

    def quickSave(self, li: list, file_header=""):
        path = self.base_settings.QUICK_PATH
        timeNum = FormatTimeTool.getFormatDateNum()
        tPath = path + "/" + file_header + timeNum + ".txt"
        with open(tPath, mode="a", encoding="utf-8") as w:
            for line in li:
                w.write(f"{line}")

    def quickSave_followedByScoreList(self, li: list, followList: list, separator=":"):
        path = self.base_settings.QUICK_PATH
        timeNum = FormatTimeTool.getFormatDateNum()
        tPath = path + "/" + timeNum + ".txt"
        with open(tPath, mode="a", encoding="utf-8") as w:
            for lin in li:
                line = ""
                for no, i in enumerate(followList):
                    # if no != 0 and no != len(followList):
                    if no != 0 and no + 1 != len(followList):
                        line += separator
                    if no + 1 == len(followList):
                        line += "\t"
                    line += lin.get(i)
                line += "\n"
                w.write(line)

    def quickSave_followedByList(self, li: list, followList: list, separator=":", fileHeader=""):
        path = self.base_settings.QUICK_PATH
        timeNum = FormatTimeTool.getFormatDateNum()
        tPath = path + "/" + fileHeader + timeNum + "Only" + ".txt"
        with open(tPath, mode="a", encoding="utf-8") as w:
            for lin in li:
                line = ""
                for no, i in enumerate(followList):
                    # if no != 0 and no != len(followList):
                    if no != 0:
                        line += separator
                    line += lin.get(i)
                line += "\n"
                w.write(line)

    def dfSave_followedByList(self, li: list, followList: list, separator=":", fileHeader=""):
        path = self.base_settings.QUICK_PATH
        timeNum = FormatTimeTool.getFormatDateNum()
        tPath = path + "/" + fileHeader + timeNum + "Only" + ".txt"
        with open(tPath, mode="a", encoding="utf-8") as w:
            for lin in li:
                line = ""
                for no, i in enumerate(followList):
                    # if no != 0 and no != len(followList):
                    if no != 0:
                        line += separator
                    line += lin.get(i)
                line += "\n"
                w.write(line)