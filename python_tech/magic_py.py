from collections import Counter
import math
import random
'''
https://docs.python.org/3/reference/datamodel.html#special-method-names
'''
from functools import wraps

#数值型魔术方法
#1

def print_boundary(func_name=""):
    def out_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            print("#" * 20 + func_name + "#" * 20)
            return func(*args, **kwargs)
            print("#" * 20 + func_name + "#" * 20)
        return inner_wrapper
    return out_wrapper

class NumberMagicClass:
    value = 5
    def __init__(self):
        print("#" * 20 + "NumberMagicClass.__init__" + "#" * 20)
#         print("__name__: ", self.__name__) #错误
        print("__class__: ", NumberMagicClass.__name__)
        self._value = 8
        print("__class__: 这个不是字符串，这个是当前类", self.__class__)
        print("__dict__: ", self.__dict__)
#         print("__code__: ", self.__code__) #function
        print("__doc__: ", self.__doc__)
        print("#" * 20 + "NumberMagicClass.__init__" + "#" * 20)
        
    def __neg__(self):
        return "-"
    def __ceil__(self):
        return "ceil"
    def __add__(self, other):
        return str(self.value) + str(other.value) 
    
def test_number_magic_class():
    obj = NumberMagicClass()
    other = NumberMagicClass()
    print("__neg__: ", -obj)
    print("__ceil__: ", math.ceil(obj))
    print("__add__: ", obj + other)

#字典型魔术方法
#1
class DictMagicClass():
    _dict = {"value":"v"}
    
    def __getitem__(self, key):
        print(key)
        return key

def test_dict_magic_class():
    obj = DictMagicClass()
    obj['v']

#2    
class DictSubClass(dict):
    def __missing__(self, key, value=None):
        print(key)
        print(value)

def test_dict_subclass():
    obj = DictSubClass()
    obj['v']

#3
class DictCounterClass(object):
    def __init__(self, v):
        self.v = v
        print(v)
    
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
        
    def __hash__(self):
        _hash = hash(str(self.v) + DictCounterClass.__name__)
        return _hash

def test_dict_counter_class():
    counter = Counter([DictCounterClass(random.randint(12, 20)) for i in range(30)])
    for k, v in counter.items():
        print(k, " ", v)
        
#4.定制模块行为
from types import ModuleType

class VerboseModule(ModuleType):
    def __repr__(self):
        return f'Verbose {self.__name__}'

    def __setattr__(self, attr, value):
        print(f'Setting {attr}...')
        super().__setattr__(attr, value)
def test_verbose_moudle():
    print(VerboseModule('test'))

if __name__ == "__main__":
    test_number_magic_class()
#     test_dict_magic_class()
#     test_dict_counter_class()
#     test_verbose_moudle()


        