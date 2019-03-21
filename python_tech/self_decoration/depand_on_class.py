__version__ = "1.0.0"
__author__ = "Zcxu"
'''
基于类的装饰器
'''
from functools import wraps

class ClassDecorator:
    def __init__(self, *args, **kwargs):
        print("ClassDecorator.__init__")
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("ClassDecorator.__call__")
            return func(*args, **kwargs)
        return wrapper

'''
装饰器测试
'''
@ClassDecorator()
def echo(info):
    print(info)

if __name__ == "__main__":
    echo("hello")
    