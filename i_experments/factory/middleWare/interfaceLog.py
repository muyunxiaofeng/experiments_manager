# -*- encoding: utf-8 -*-
"""
PyCharm interfaceLog
2022年11月12日
by Orochi
该文件目的
第一层

第二层

执行层

"""

from ..filePipeline import toLog



logger = toLog.ToLog().logger
# time.sleep(3)
summary = toLog.ToLog("汇总").logger
# time.sleep(3)
ex = toLog.ToLog("ex").logger
# time.sleep(3)
sql = toLog.ToLog("sql").logger
# time.sleep(3)
urlLog = toLog.ToLog("url").logger

dataLog = toLog.ToLog("data").logger


