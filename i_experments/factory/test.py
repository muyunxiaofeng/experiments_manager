# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年10月27日
by Orochi
该文件目的
第一层

第二层

执行层

"""
#
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from reqFactory.reqTool import ipSpider
import time

from new_module import factory as ipd

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
        ip_de = ipd.IpDetect()
        ip_de.ipDetector()
        time.sleep(60 * 60 * 2)
