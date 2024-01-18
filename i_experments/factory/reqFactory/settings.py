# -*- encoding: utf-8 -*-
"""
PyCharm settings
2022年09月18日
by Orochi
该文件目的
第一层

第二层

执行层

"""


class RequestToolSettings:
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 + "Chrome/105.0.0.0 Safari/537.36"
    PROXY = '223.96.90.216:8085'
    TEST_URL = "http://httpbin.org/ip"
    TIME_OUT = 30
    SLEEP_TIME = 10  # 最多睡多久 = SLEEP_TIME + LIMIT_SLEEP_TIME
    LIMIT_SLEEP_TIME = 1  # 最少睡多久


class IpSpiderSettings:
    MAX_EXCEPTION = 10

    # SAVE
    # SAVE_DATA = False
    # SAVE_TXT = False
    # SAVE_CSV = False
    # SAVE_RADIS = False

    SAVE_DATA = True
    SAVE_TXT = True
    SAVE_CSV = True
    SAVE_RADIS = True

    # debugger
    DEBUGGER = False
    # DEBUGGER = True

    # RADIS INFO
    VERIFY_IP_ZSET = "verifyIp"
    VERIFY_IP_DB = 1

    PROXY_RADIS_ZSET = "proxy_radis"
    PROXY_RADIS_DB = 0


class Paper:
    SCISummaryUrl = "https://tool.yovisun.com/scihub/"
    YI_SOU_JI_DA = "https://www.ablesci.com/so"
    LIB_URL = "http://libgen.ggfwzs.net/"
    LIB_URI = "https://www.booksc.ggfwzs.net/"
    GUO_FEN_XUE_SHU = "https://gfsoso.99lb.net/sci-hub.html"
    GUO_FEN_XUE_SHU_URI = "http://bbs.99lb.net/"
    GUO_FEN_XUE_SHU_URL = "https://gfsoso.99lb.net/bookzz.html"
    ZHONG_WEN_LIB_URL = "http://www.sci-hub.ac.cn/zw.html"
    SCIHUB_LIST = [
        "https://sci-hub.st/",
        "http://sci-hub.ren/",
        "https://sci-hub.shop/",
        "https://sci-hub.wf/",
        "https://sci-hub.se/",
        "https://sci-hub.et-fine.com/",
        "https://sci-hub.ee/"

    ]
    SHEN_DU_XUE_SHU = "https://xs.zidianzhan.net/"

    rq20221114 = ['https://sci-hub.au/',
                  'https://sci-hub.bz/',
                  'https://sci-hub.cm/',
                  'https://sci-hub.de/',
                  'https://sci-hub.ee/',
                  'https://sci-hub.is/',
                  'https://sci-hub.la/',
                  'https://sci-hub.nz/',
                  'https://sci-hub.pm/',
                  'https://sci-hub.re/',
                  'https://sci-hub.sc/',
                  'https://sci-hub.se/',
                  'https://sci-hub.st/',
                  'https://sci-hub.tf/',
                  'https://sci-hub.wf/']
