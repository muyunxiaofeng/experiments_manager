# -*- encoding: utf-8 -*-
"""
PyCharm toLog
2022年11月10日
by Orochi
该文件目的
第一层

第二层

执行层

"""
import logging
import traceback

from . import settings
from logging.handlers import TimedRotatingFileHandler
import colorlog
import re

# 使用配置文件的方式来处理日志
import os.path


# logging.config.fileConfig('./logging.conf')
#
# rootLogger = logging.getLogger()
# rootLogger.debug("This is root Logger, debug")
#
# # 记录器
# logger = logging.getLogger("appLog")  # 修改的显示名称
# # 打印日志的代码
# logger.debug('This is debug log，bug')  # 调试级别


class ToLog:
    def __init__(self, loggerName=None):

        # 获取设置
        logSettings = settings.Log_Settings()
        if not os.path.exists(logSettings.FILE_PATH):
            os.mkdir(logSettings.FILE_PATH)
        #
        # logging.config.fileConfig('./logging.conf')
        print("初始化Logger")

        # 记录器
        if loggerName is None:
            appLogger = logging.getLogger(logSettings.LOGGER_NAME)  # 修改的显示名称
        else:
            appLogger = logging.getLogger(loggerName)  # 修改的显示名称

        appLogger.setLevel(logSettings.LOGGER_LEVEL)  # 修改日志级别

        # 处理器
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logSettings.CONSOLE_HANDLER_LEVEL)

        # 写入文件，没有给handler指定日志级别，将使用logger的级别
        # fileHandler = logging.FileHandler(filename=logSettings.FILE_NAME, mode="a", encoding="utf-8")
        # fileHandler.setLevel(logging.INFO)

        fileHandler = logging.handlers.TimedRotatingFileHandler(filename=logSettings.FILE_NAME, when="midnight",
                                                                encoding="utf-8")
        fileHandler.setLevel(logSettings.FILE_HANDLER_LEVEL)
        fileHandler.suffix = "%Y-%m-%d.appLogger.log"
        fileHandler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.appLogger.log$")

        # 给处理器设置formatter格式; 8s：表示s前面的占8位 https://www.cnblogs.com/mghhzAnne/p/14176625.html
        formatter = logging.Formatter(logSettings.FORMATTER)
        # log_colors 为空为默认颜色
        colorFormatter = colorlog.ColoredFormatter("%(log_color)s" + logSettings.FORMATTER,
                                                   log_colors=logSettings.LOG_COLOR)

        # 给处理器设置格式
        consoleHandler.setFormatter(colorFormatter)
        fileHandler.setFormatter(formatter)

        # 记录器要设置处理器
        appLogger.addHandler(consoleHandler)
        appLogger.addHandler(fileHandler)

        # 方法API
        self.logger = appLogger
        self.consoleHandler = consoleHandler

        # 关联过滤器
        # logger.addFilter(fit)
        # fileHandler.addFilter(fit)

        """
        
        other handler
        
        
        """
        try:
            # 汇总的日志方便统筹
            # logging.handlers.WatchedFileHandler
            # logging.handlers.BaseRotatingHandler
            # logging.handlers.QueueHandler
            # logging.handlers.RotatingFileHandler
            # logging.handlers.BufferingHandler
            summaryHandler = logging.handlers.RotatingFileHandler(filename=logSettings.SUMMARY_HANDLER_FILE_NAME,
                                                                  mode="a", maxBytes=1024 * 1024, encoding="utf-8",
                                                                  backupCount=50)
            # summaryHandler = logging.handlers.TimedRotatingFileHandler(filename=logSettings.SUMMARY_HANDLER_FILE_NAME,
            #                                                            when="midnight", encoding="utf-8")
            summaryHandler.setLevel(logSettings.SUMMARY_HANDLER_LEVEL)
            summaryHandler.suffix = "%Y-%m-%d.Summary.log"
            summaryHandler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.Summary.log$")

            summaryHandler.setFormatter(formatter)
            appLogger.addHandler(summaryHandler)
            summaryHandlerFilter = logging.Filter(logSettings.SUMMARY_HANDLER_FILTER)
            summaryHandler.addFilter(summaryHandlerFilter)
            self.summaryHandler = summaryHandler

            # 异常的日志方便统筹
            # exceptionHandler = logging.handlers.TimedRotatingFileHandler(
            #     filename=logSettings.EXCEPTION_HANDLER_FILE_NAME,
            #     when="W1", encoding="utf-8")
            exceptionHandler = logging.handlers.RotatingFileHandler(filename=logSettings.EXCEPTION_HANDLER_FILE_NAME,
                                                                    mode="a", maxBytes=1024 * 1024, encoding="utf-8")
            exceptionHandler.suffix = "%Y-%m-%d.ex.log"
            exceptionHandler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.Summary.log$")
            exceptionHandler.setLevel(logSettings.EXCEPTION_HANDLER_LEVEL)
            exceptionHandler.setFormatter(formatter)
            appLogger.addHandler(exceptionHandler)
            exceptionHandlerFilter = logging.Filter(logSettings.EXCEPTION_HANDLER_FILTER)
            exceptionHandler.addFilter(exceptionHandlerFilter)
            self.exceptionHandler = exceptionHandler

            # SQL的日志方便统筹
            # sqlHandler = logging.handlers.TimedRotatingFileHandler(filename=logSettings.SQL_HANDLER_FILE_NAME,
            #                                                        when="W2", encoding="utf-8")
            sqlHandler = logging.handlers.RotatingFileHandler(filename=logSettings.SQL_HANDLER_FILE_NAME,
                                                              mode="a", maxBytes=1024 * 1024, encoding="utf-8")
            sqlHandler.suffix = "%Y-%m-%d.sql.log"
            sqlHandler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.sql.log$")
            sqlHandler.setLevel(logSettings.SQL_HANDLER_LEVEL)
            sqlHandler.setFormatter(formatter)
            appLogger.addHandler(sqlHandler)
            sqlHandlerFilter = logging.Filter(logSettings.SQL_HANDLER_FILTER)
            sqlHandler.addFilter(sqlHandlerFilter)
            self.sqlHandler = sqlHandler

            # URL的日志方便统筹
            # urlHandler = logging.handlers.TimedRotatingFileHandler(filename=logSettings.URL_HANDLER_FILE_NAME,
            #                                                        when="W3", encoding="utf-8")
            urlHandler = logging.handlers.RotatingFileHandler(filename=logSettings.URL_HANDLER_FILE_NAME,
                                                              mode="a", maxBytes=1024 * 1024, encoding="utf-8")
            urlHandler.suffix = "%Y-%m-%d.url.log"
            urlHandler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.url.log$")
            urlHandler.setLevel(logSettings.URL_HANDLER_LEVEL)
            urlHandler.setFormatter(formatter)
            appLogger.addHandler(urlHandler)
            urlHandlerFilter = logging.Filter(logSettings.URL_HANDLER_FILTER)
            urlHandler.addFilter(urlHandlerFilter)
            self.urlHandler = urlHandler

            # URL的日志方便统筹
            # urlHandler = logging.handlers.TimedRotatingFileHandler(filename=logSettings.URL_HANDLER_FILE_NAME,
            #                                                        when="W3", encoding="utf-8")
            dataHandler = logging.handlers.RotatingFileHandler(filename=logSettings.DATA_HANDLER_FILE_NAME,
                                                              mode="a", maxBytes=1024 * 1024, encoding="utf-8")
            dataHandler.suffix = "%Y-%m-%d.data.log"
            dataHandler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.data.log$")
            dataHandler.setLevel(logSettings.DATA_HANDLER_LEVEL)
            dataHandler.setFormatter(formatter)
            appLogger.addHandler(dataHandler)
            dataHandlerFilter = logging.Filter(logSettings.DATA_HANDLER_FILTER)
            dataHandler.addFilter(dataHandlerFilter)
            self.dataHandler = dataHandler
        except Exception as e:
            print(traceback.format_exc())
        # 打印日志的代码
        if loggerName is None:
            appLogger.debug('This is debug log')  # 调试级别
        elif loggerName == "汇总":
            appLogger.info('This is info log')  # 信息级别
        elif loggerName == "url":
            appLogger.warning('This is warning log')  # 警告级别
        elif loggerName == "sql":
            appLogger.error('This is error log')  # 错误级别
        elif loggerName == "data":
            appLogger.critical('This is critical log')  # 严重错误级别
        elif loggerName == "ex":
            appLogger.critical('This is critical log')  # 严重错误级别

    def logClose(self):
        self.summaryHandler.close()
        self.exceptionHandler.close()
        self.sqlHandler.close()
        self.urlHandler.close()
        self.dataHandler.close()
        self.logger.warning("CLOSING LOG...")
        ToLog()
