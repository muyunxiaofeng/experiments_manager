# -*- encoding: utf-8 -*-
"""
PyCharm runIpSpider
2022年10月30日
by Orochi
该文件目的
第一层

第二层

执行层

"""

import time
from .reqFactory import ipSpider as ips
# import factory.reqFactory.ipSpider as ips
# import factory.reqFactory.ipDetect as ipd

if __name__ == '__main__':
    # d = os.path.dirname(__file__)  # 获取当前路径
    # parent_path = os.path.dirname(d)  # 获取上一级路径
    # sys.path.append(parent_path)  # 如果要导入到包在上一级
    # ip = ips.IpSpider()
    # ip = ipSpider.IpSpider()
    # ip.get_98ip()
    # next(ip.get_98ip())
    # ip_de = ipd.IpDetect()
    # ip_de.ipDetector()

    while 1:
        ip = ips.IpSpider()
        ip.get_98ip()
        time.sleep(60 * 60 * 4)
