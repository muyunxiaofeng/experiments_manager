# -*- encoding: utf-8 -*-
"""
PyCharm toEasySave
2022年10月29日
by Orochi
该文件目的
第一层

第二层

执行层

"""

from . import toCSV, toTxt, toPy


class ToEasySave:
    def __init__(self):
        self.csv = toCSV.ToCSV()
        self.txt = toTxt.ToTXT()
        self.py = toPy.ToPy()

    def ctSave(self, listDic, followList, separator=":", fileHeader=""):
        self.csv.pandasSave(listDic=listDic, fileHeader=fileHeader)
        self.txt.quickSave_followedByList(li=listDic, followList=followList, separator=separator, fileHeader=fileHeader)
        self.py.saveListDicToPy(liDic=listDic, file_header=fileHeader)
        # return
