#coding = utf-8

import logging

'''
配置二
'''

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(user)s[%(ip)s] - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT)
logging.warning("Some one delete the log file.", exc_info=False, stack_info=False, extra={'user': 'Tom', 'ip':'47.98.53.222'})


