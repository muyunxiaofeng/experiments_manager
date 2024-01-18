# -*- encoding: utf-8 -*-
"""
PyCharm requestTool
2022年09月18日
by Orochi
该文件目的
第一层

第二层

执行层

"""
import random
import traceback

import requests
from lxml import etree

from .settings import RequestToolSettings
from ..filePipeline import fromRadisGetIp


class RequestTool:
    # 对请求方法进行一个封装
    def __init__(self, url, proxy=False, html=True):
        self.tree = None
        self.html = None
        self.file = None
        self.res = None
        self.session = None
        self.Dic = None
        if html:
            if proxy:
                self.requestWebWithProxy(url)
            elif url is not None:
                self.requestWeb(url)
        else:
            if proxy:
                self.requestWebWithProxy(url, html)
            elif url is not None:
                self.requestWeb(url, html)

    def requestWeb(self, url, html=True):
        """
        访问网页的方法 封装了session等元素
        :param url:
        :param html:    True 则为正常爬虫模式  访问网页等
                        False 则为下载等模式  仅对文件进行简单的获取如content
        :return:
        """
        # 不管咋地先睡会
        _time = random.random() * RequestToolSettings.SLEEP_TIME + RequestToolSettings.LIMIT_SLEEP_TIME
        print("Zzz" * 50, "睡了", _time, "s")
        logger.debug(f"睡了 {_time} s")
        time.sleep(_time)
        # 常规参数设置
        header = {
            "user-agent": RequestToolSettings.USER_AGENT
        }
        proxy = {"http": RequestToolSettings.PROXY}
        testUrl = RequestToolSettings.TEST_URL
        timeout = RequestToolSettings.TIME_OUT
        res1 = requests.get(testUrl, headers=header, proxies=proxy, timeout=timeout)
        print("测试代理 \t ", res1.status_code)
        logger.warning(f"测试代理:{res1.status_code}")
        # 代理验证
        if res1.status_code <= 200:

            self.session = requests.Session()
            self.res = self.session.get(url, headers=header, proxies=proxy)
            if html:
                self.html = self.res.content.decode(self.res.apparent_encoding)
                self.tree = etree.HTML(self.html)
                self.Dic = {"session": self.session, "res": self.res, "html": self.html, "tree": self.tree}
            else:
                self.file = self.res.content
                self.Dic = {"session": self.session, "res": self.res, "file": self.file}

            # log
            urlLog.info(f"{url}:{self.res.status_code}")
            urlLog.debug(f"requestCookies:{self.session.cookies.get_dict()}")
            urlLog.debug(f"responseCookies:{self.res.cookies.get_dict()}")
            urlLog.debug(f"responseCookies:{self.res.headers.get('cookie')}")
            urlLog.debug(f"responseHeader:{self.res.headers}")
        else:
            print("代理超时")

    @staticmethod
    def testIp(ip: str):
        # 不管咋地先睡会
        # _time = random.random() * RequestToolSettings.SLEEP_TIME + RequestToolSettings.LIMIT_SLEEP_TIME
        _time = 1
        # print("Zzz" * 50, "睡了", _time, "s")
        time.sleep(_time)
        # 常规参数设置
        header = {
            "user-agent": RequestToolSettings.USER_AGENT
        }
        proxy = {"http": ip}
        testUrl = RequestToolSettings.TEST_URL
        timeout = 3
        res1 = requests.get(testUrl, headers=header, proxies=proxy, timeout=timeout)
        print("requestTool.py  \t 测试代理 \t ", res1.status_code)
        logger.warning(f"测试代理:{res1.status_code}")
        urlLog.warning(f"测试代理:{res1.status_code}")
        return res1.status_code

    def requestWebWithProxy(self, url, html=True):
        """
        访问网页的方法 封装了session等元素
        :param url:
        :param html:    True 则为正常爬虫模式  访问网页等
                        False 则为下载等模式  仅对文件进行简单的获取如content
        :return:
        """
        # 不管咋地先睡会
        _time = random.random() * RequestToolSettings.SLEEP_TIME + RequestToolSettings.LIMIT_SLEEP_TIME
        print("Zzz" * 50, "睡了", _time, "s")
        logger.debug(f"睡了 {_time} s")
        time.sleep(_time)
        # 常规参数设置
        header = {
            "user-agent": self.getUserAgent()
        }
        proxy = {"http": self.getProxyIp()}
        testUrl = RequestToolSettings.TEST_URL
        timeout = RequestToolSettings.TIME_OUT

        res1 = requests.get(testUrl, headers=header, proxies=proxy, timeout=timeout)

        print("测试代理 \t ", res1.status_code)
        logger.warning(f"测试代理:{res1.status_code}")
        urlLog.warning(f"测试代理:{res1.status_code}")
        # 代理验证
        if res1.status_code <= 200:

            # request
            self.session = requests.Session()
            self.res = self.session.get(url, headers=header, proxies=proxy)
            if html:
                self.html = self.res.content.decode(self.res.apparent_encoding)
                self.tree = etree.HTML(self.html)
                self.Dic = {"session": self.session, "res": self.res, "html": self.html, "tree": self.tree}
            else:
                self.file = self.res.content
                self.Dic = {"session": self.session, "res": self.res, "file": self.file}

            # log
            urlLog.info(f"{url}:{self.res.status_code}")
            urlLog.debug(f"requestCookies:{self.session.cookies.get_dict()}")
            urlLog.debug(f"responseCookies:{self.res.cookies.get_dict()}")
            urlLog.debug(f"responseCookies:{self.res.headers.get('cookie')}")
            urlLog.debug(f"responseHeader:{self.res.headers}")
        else:
            # print("代理超时")
            urlLog.exception("代理超时")

    def getProxyIp(self):
        getIP = fromRadisGetIp.FromRadisGetIp(db=1)
        topIpList = getIP.getTopIp_fromRadis()
        print("topIpList:", topIpList)
        if topIpList:
            for ip in topIpList:
                try:
                    statusCode = self.testIp(ip)
                    if statusCode <= 200:
                        return ip
                except Exception as e:
                    ex.warning(traceback.format_exc())
                    continue

        else:
            topIpList = getIP.getMidIp_fromRadis()
            for ip in topIpList:
                try:
                    statusCode = self.testIp(ip)
                    if statusCode <= 200:
                        return ip
                    else:
                        continue
                except Exception as e:
                    ex.warning(traceback.format_exc())
                    continue
            ex.warning("无可用ip")
            exit()

    @staticmethod
    def getUserAgent():
        """
        生成一个headers


        :return: 生成一个headers
        """

        chrome_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome"
            "/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome"
            "/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome"
            "/19.0.1055.1 Safari/535.24"

            # ————————————————
            # 版权声明：本文为CSDN博主「Se_cure」的原创文章，遵循CC
            # 4.0
            # BY - SA版权协议，转载请附上原文出处链接及本声明。
            # 原文链接：https: // blog.csdn.net / dxyna / article / details / 81096150
        ]
        firefox_list = [
            "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar"
            "/alxf-2.0 Firefox/3.6.14",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
            # ————————————————
            # 版权声明：本文为CSDN博主「Se_cure」的原创文章，遵循CC
            # 4.0
            # BY - SA版权协议，转载请附上原文出处链接及本声明。
            # 原文链接：https: // blog.csdn.net / dxyna / article / details / 81096150
        ]
        opera_list = [
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Android 2.3.4; Linux; Opera mobi/adr-1107051709; U; zh-cn) Presto/2.8.149 Version/1"
            # ————————————————
            # 版权声明：本文为CSDN博主「Se_cure」的原创文章，遵循CC
            # 4.0
            # BY - SA版权协议，转载请附上原文出处链接及本声明。
            # 原文链接：https: // blog.csdn.net / dxyna / article / details / 81096150
        ]
        safari_list = [
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit"
            "/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit"
            "/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit"
            "/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5"

            # ————————————————
            # 版权声明：本文为CSDN博主「Se_cure」的原创文章，遵循CC
            # 4.0
            # BY - SA版权协议，转载请附上原文出处链接及本声明。
            # 原文链接：https: // blog.csdn.net / dxyna / article / details / 81096150
        ]
        ie_list = [
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
            # ————————————————
            # 版权声明：本文为CSDN博主「Se_cure」的原创文章，遵循CC
            # 4.0
            # BY - SA版权协议，转载请附上原文出处链接及本声明。
            # 原文链接：https: // blog.csdn.net / dxyna / article / details / 81096150
        ]
        native_list = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
            "/104.0.0.0 Safari/537.36"
        ]
        # faker = UserAgent()
        # fake_list = [{'UserAgent': faker.random}.get('UserAgent')]
        # headers_list = chrome_list + firefox_list + opera_list + safari_list + ie_list + fake_list + native_list
        headers_list = chrome_list + firefox_list + opera_list + safari_list + ie_list + native_list
        # print(len(headers_list))
        # print(random.choice(headers_list))
        return random.choice(headers_list)
