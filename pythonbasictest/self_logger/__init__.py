#coding = utf-8

import logging

'''
配置二
'''

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(user)s[%(ip)s] - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT)
logging.warning("Some one delete the log file.", exc_info=False, stack_info=False, extra={'user': 'Tom', 'ip':'47.98.53.222'})


# '''
# 日志配置
# '''
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
# logging.basicConfig(
#     level=logging.DEBUG,
# #     filename = "my.log",
#     format = LOG_FORMAT,
#     datefmt = DATE_FORMAT
# )
# 
# '''
# 方式一
# '''
# ###########################输出信息###########################
# logging.debug("debug")
# logging.info("info")
# logging.warning("warnging")
# logging.error("error")
# logging.critical("critical")
# logging.warning('%s is %d years old.', 'Tom', 10)
# ############################################################
# 
# '''
# 方式二
# '''
# logging.log(logging.DEBUG, "This is a debug log.")
# logging.log(logging.INFO, "This is a info log.")
# logging.log(logging.WARNING, "This is a warning log.")
# logging.log(logging.ERROR, "This is a error log.")
# logging.log(logging.CRITICAL, "This is a critical log.")


