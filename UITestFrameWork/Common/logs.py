#!/usr/bin/python3
# -*- coding=utf-8 -*-


"""
logging模块支持我们自定义封装一个新日志类
"""

import logging
import time
import os.path


class Logger(object):

    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.cases = './'

        # 创建一个handler，用于写入日志文件
        for filename in os.listdir(os.getcwd()):
            if filename == "Logs":
                break
        else:
            os.mkdir(os.getcwd() + '/Logs')

        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.getcwd() + '/Logs/'
        log_name = log_path + rq + '.log'  # 文件名
        print('log_name={}'.format(log_name))

        # 将日志写入磁盘
        fh = logging.FileHandler(log_name)
        # 设置日志器将会处理的日志消息的最低严重级别，
        fh.setLevel(logging.INFO)

        # 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)


        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger


if __name__=="__main__":
    log = Logger('logger').get_log()
    log.warning("warning")
    log.info("info")
    log.error("error")
