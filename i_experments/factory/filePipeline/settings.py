# -*- encoding: utf-8 -*-
"""
PyCharm settings
2022年10月28日
by Orochi
该文件目的
第一层

第二层

执行层

"""

import logging


class BaseSettings:
    # QUICK_PATH = "../SAVE"
    QUICK_PATH = "./SAVE"


class RadisSettings:
    HOST = '127.0.0.1'
    PORT = 6379
    PASSWORD = '123456'
    DB = 0
    SCORE = 100  # 默认最高权重100
    MIN_SCORE = 50  # 最低权重
    ZSET_NAME = "proxy_radis"  # 有序集合名词

    # VERIFY IP
    VERIFY_IP_ZSET = "verifyIp"
    VERIFY_IP_DB = 1


class MysqlSettings:
    HOST = '127.0.0.1'
    PORT = '3306'
    PASSWORD = '19921227'
    USER = 'orochi'

    ROOT = 'root'
    ROOT_PASSWORD = '123456'
    ROOT_DATABASE = 'NcbiDatabase'

    NCBI_DATABASE = 'NcbiDatabase'
    TABLE_PAPER = 'papers'
    TABLE_PAPER_INFO_1 = 'paperInfo_01'


class Log_Settings:
    # logger
    LOGGER_NAME = "appLogger"
    LOGGER_LEVEL = logging.DEBUG

    # config
    FILE_CONFIG = 'logging.conf'

    # consoleHandler
    CONSOLE_HANDLER_LEVEL = logging.DEBUG

    # fileHandler
    FILE_PATH = "./LogSave"
    FILE_NAME = f"{FILE_PATH}/{LOGGER_NAME}.log"
    FILE_HANDLER_LEVEL = logging.DEBUG

    # summaryHandler
    SUMMARY_HANDLER_LEVEL = logging.DEBUG
    SUMMARY_HANDLER_FILE_NAME = f"{FILE_PATH}/Summary.log"
    SUMMARY_HANDLER_FILTER = "汇总"

    # exceptionHandler
    EXCEPTION_HANDLER_LEVEL = logging.DEBUG
    EXCEPTION_HANDLER_FILE_NAME = f"{FILE_PATH}/EXCEPTION.log"
    EXCEPTION_HANDLER_FILTER = "ex"

    # sqlHandler
    SQL_HANDLER_LEVEL = logging.DEBUG
    SQL_HANDLER_FILE_NAME = f"{FILE_PATH}/SQL.log"
    SQL_HANDLER_FILTER = "sql"

    # urlHandler
    URL_HANDLER_LEVEL = logging.DEBUG
    URL_HANDLER_FILE_NAME = f"{FILE_PATH}/URL.log"
    URL_HANDLER_FILTER = "url"

    # dataHandler
    DATA_HANDLER_LEVEL = logging.DEBUG
    DATA_HANDLER_FILE_NAME = f"{FILE_PATH}/DATA.log"
    DATA_HANDLER_FILTER = "data"

    # formatter设置
    COLORS = [
        'black',
        'red',
        'green',
        'yellow',
        'blue',
        'purple',
        'cyan',
        'white'
    ]
    LOG_COLOR = {'DEBUG': 'cyan',
                 'INFO': 'green',
                 'WARNING': 'yellow',
                 'ERROR': 'red',
                 'CRITICAL': 'bold_purple'}  # 加粗效果
    # ,bg_yellow 设置背景色
    FORMATTER = "%(asctime)s \t %(name)s \t %(levelname)9s \t %(message)50s \t %(filename)20s \t %(lineno)5s"
