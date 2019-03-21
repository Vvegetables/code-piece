__version__ = "1.0.1"
__author__ = "Zcxu"

'''
基于函数的装饰器
'''

from functools import wraps


def print_boundary(func_name=""):
    def out_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            print("#" * 20 + func_name + "#" * 20)
            return func(*args, **kwargs)
            print("#" * 20 + func_name + "#" * 20)
        return inner_wrapper
    return out_wrapper