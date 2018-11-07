#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/7/007 20:50
# @Author  : jiaojinglong


import logging

# DEBUG：调试信息，通常在诊断问题的时候用得着；
# INFO：普通信息，确认程序安装预期运行；
# WARNING：警告信息，表示发生了意想不到的事情，或者指示接下来可能会出现一些问题，但是程序还是继续运行；
# ERROR：错误信息，程序运行中出现了一些问题，一些功能没有执行；
# CRITICAL：危险信息，一个严重的错误，导致程序无法继续运行。


#日志格式
# %(asctime)s：日志创建时的普通时间；
# %(created)f：日志创建时的时间（由time.time()返回）；
# %(filename)s：文件名；
# %(funcName)s：调用日志记录的函数；
# %(levelname)s：日志消息的文本级别；
# %(levelno)s：日志消息的数字级别；
# %(lineno)d：调用日志消息的行号；
# %(msecs)d：创建时间的毫秒部分；
# %(message)s：日志消息；
# %(name)s：日志器的名称；
# %(pathname)s：记录日志的源文件的路径名；
# %(process)d：进程ID；
# %(processName)s：进程名；
# %(thread)d：线程ID；
# %(threadName)s：线程名；
# %(relativeCreated)d：创建日志记录的时间（以毫秒为单位）




import logging

class Mylog():
    def __init__(self):
        self.log = logging.getLogger("test_logger")
        self.log.setLevel(logging.DEBUG)
        #创建一个日志处理器，记录所有日志
        log_handler = logging.FileHandler(filename='log.log', encoding="utf8")
        log_handler.setLevel(logging.INFO)

        # 创建一个日志处理器，记录错误日志
        error_handler = logging.FileHandler(filename='error.log', encoding="utf8")
        error_handler.setLevel(logging.ERROR)

        #屏幕输出日志
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)

        # 创建一个日志格式器
        formats = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s: %(message)s',
                                    datefmt='%Y/%m/%d %I:%M:%S %p')

        # 将日志格式器添加到日志处理器中
        log_handler.setFormatter(formats)
        error_handler.setFormatter(formats)
        stream_handler.setFormatter(formats)

        # 将日志处理器添加到日志记录器中
        self.log.addHandler(log_handler)
        self.log.addHandler(error_handler)
        self.log.addHandler(stream_handler)

    def error(self,message):
        """
        记录到错误日志，普通日志并输出
        :param message:
        :return:
        """
        self.log.error(message)

    def debug(self,message):
        """
        调试信息只输出到屏幕
        :param message:
        :return:
        """
        self.log.debug(message)

    def info(self,message):
        """
        记录文件并输出
        :param message:
        :return:
        """
        self.log.info(message)

    def warning(self,message):
        """
        记录文件并输出
        :param message:
        :return:
        """
        self.log.warning(message)

    def critical(self,message):
        """
        记录到错误日志，普通日志并输出
        :param message:
        :return:
        """
        self.log.critical(message)


mylog = Mylog()
mylog.error("出现了错误",)
mylog.info("打印信息")
mylog.warning("警告信息")
mylog.debug("asdasdfsdf")