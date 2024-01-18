# -*- encoding: utf-8 -*-
"""
PyCharm toPy
2022年11月19日
by Orochi
该文件目的
第一层

第二层

执行层

"""
import json
import os
from ..timeFactory.formatTime import FormatTimeTool
from . import settings


class ToPy:
    def __init__(self):
        self.base_settings = settings.BaseSettings()
        if not os.path.exists(self.base_settings.QUICK_PATH):
            os.mkdir(self.base_settings.QUICK_PATH)

    def saveListDicToPy(self, liDic: list, file_header=""):
        path = self.base_settings.QUICK_PATH
        timeNum = FormatTimeTool.getFormatDateNum()
        tPath = path + "/" + file_header + timeNum + ".py"
        with open(tPath, mode="a", encoding="utf-8") as w:
            w.write(json.dumps(liDic))
