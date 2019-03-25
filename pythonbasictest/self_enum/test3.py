
class TestMeta(type):
    def __prepare__(self, *args, **kwargs):
        print(self, args, kwargs)
        return {} #必须返回一个mapping类型数据
    
    def _hello(self): #可以直接给TestNew(metaclass=TestMeta)类使用
        print("hello")
        
    def __getitem__(self, name): #可以直接给TestNew(metaclass=TestMeta)类使用
        print(name)
        return name
        
    def __new__(self, *args, **kwargs):
        return type.__new__(self, *args, **kwargs)

class TestNew(metaclass=TestMeta):
    def __new__(self):
        print("__new__")
    def __init__(self):
        print("__init__")
        
if __name__ == '__main__':
    TestNew._hello()
    TestNew['t_attribute']
    