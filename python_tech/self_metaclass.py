#coding=utf-8
'''
元类
type的两种用途
1。 type(1) == int
2. type('Hello', (object, ), dict(name='World')) == 
    class Hello(object):
        def __init__(self, name):
            self.name = name
'''

'''
示例一
'''
class SayMetaClass(type):
    def __new__(cls, name:str, bases:tuple, attrs:dict):
        '''
        @param cls: 元类实例
        @param name: 子类类名
        @param bases: 父类元组
        @param attrs: 子类的属性字典   
        '''
        #进行改造
        attrs['say_' + name] = \
            lambda self, value, saying=name : \
                print(saying + ',' + value + '!')
        #调用父类进行类的创建
        return type.__new__(cls, name, bases, attrs)

class Hello(metaclass=SayMetaClass):
    pass

def test_method1(value):
    hello = Hello()
    hello.say_Hello(value)


if __name__ == "__main__":
    test_method1('World')
