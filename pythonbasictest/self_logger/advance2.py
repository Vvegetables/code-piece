#coding=utf-8
'''
向日志输出中添加上下文信息
'''

'''
方式一(通过向日志记录函数传递一个extra参数引入上下文信息)
'''
import logging
from random import choice
import sys


def method1():
    fmt = logging.Formatter("%(asctime)s - %(name)s - %(ip)s - %(username)s - %(message)s")
    h_console = logging.StreamHandler(sys.stdout)
    h_console.setFormatter(fmt)
    logger = logging.getLogger("myPro")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(h_console)
    
    extra_dict = {"ip": "113.208.78.29", "username": "Petter"}
    logger.debug("User Login!", extra=extra_dict)
    
    extra_dict = {"ip": "223.190.65.139", "username": "Jerry"}
    logger.info("User Access!", extra=extra_dict)

'''
方式二(使用LoggerAdapters引入上下文信息)
'''
class MyLoggerAdapter(logging.LoggerAdapter):

    def process(self, msg, kwargs):
        if 'extra' not in kwargs:
            kwargs["extra"] = self.extra
        return msg, kwargs

def method2():
    # 初始化一个要传递给LoggerAdapter构造方法的logger实例
    fmt = logging.Formatter(
        "%(asctime)s - %(name)s - %(ip)s - %(username)s - %(message)s"
    )
    h_console = logging.StreamHandler(sys.stdout)
    h_console.setFormatter(fmt)
    init_logger = logging.getLogger("myPro")
    init_logger.setLevel(logging.DEBUG)
    init_logger.addHandler(h_console)
    
    # 初始化一个要传递给LoggerAdapter构造方法的上下文字典对象
    extra_dict = {"ip": "IP", "username": "USERNAME"}
    # 获取一个自定义LoggerAdapter类的实例
    logger = MyLoggerAdapter(init_logger, extra_dict)
    
    # 应用中的日志记录方法调用
    logger.info("User Login!")
    logger.info("User Login!", extra={"ip": "113.208.78.29", "username": "Petter"})
    logger.info("User Login!")
    logger.info("User Login!")

'''
方式三(使用Filters引入上下文信息)
'''
class ContextFilter(logging.Filter):
    ip = 'IP'
    username = 'USER'

    def filter(self, record):
        record.ip = self.ip
        record.username = self.username
        return True

def method3():
    levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
    users = ['Tom', 'Jerry', 'Peter']
    ips = ['113.108.98.34', '219.238.78.91', '43.123.99.68']

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)-15s %(name)-5s %(levelname)-8s %(ip)-15s %(username)-8s %(message)s')
    logger = logging.getLogger('myLogger')
    filter = ContextFilter()
    logger.addFilter(filter)
    logger.debug('A debug message')
    logger.info('An info message with %s', 'some parameters')

    for x in range(5):
        lvl = choice(levels)
        lvlname = logging.getLevelName(lvl)
        filter.ip = choice(ips)
        filter.username = choice(users)
        logger.log(lvl, 'A message at %s level with %d %s' , lvlname, 2, 'parameters')


if __name__ == "__main__":
    method3()
    
    
