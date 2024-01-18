# -*- encoding: utf-8 -*-
"""
PyCharm runDetectIp
2022年10月30日
by Orochi
该文件目的
第一层

第二层

执行层

"""
import time

from .reqFactory import ipDetect

if __name__ == '__main__':
    while 1:
        ipd = ipDetect.IpDetect()
        ipd.independentlyDetectIp()
        time.sleep(60 * 60 * 2)
