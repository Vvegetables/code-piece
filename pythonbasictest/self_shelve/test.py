#coding=utf-8
import shelve

'''
shelve是一个简单的数据存储方案，类似key-value数据库，可以很方便的保存python对象，其内部是通过pickle协议来实现数据序列化。
shelve只有一个open()函数，这个函数用于打开指定的文件（一个持久的字典），然后返回一个shelf对象。
shelf是一种持久的、类似字典的对象。它与“dbm”的不同之处在于，其values值可以是任意基本Python对象--pickle模块可以处理的任何数据。
这包括大多数类实例、递归数据类型和包含很多共享子对象的对象。keys还是普通的字符串。

shelve.open(filename, flag='c', protocol=None, writeback=False)
    param：flag：
        'r'    以只读模式打开一个已经存在的数据存储文件
        'w'    以读写模式打开一个已经存在的数据存储文件
        'c'    以读写模式打开一个数据存储文件，如果不存在则创建
        'n'    总是创建一个新的、空数据存储文件，并以读写模式打开
    param：protocol：
        default == pickle v3 参数表示序列化数据所使用的协议版本
    param：writeback：
        default == False 参数表示是否开启回写功能

'''

class Test1:
    #保存数据
    def save_method1(self):
        with shelve.open("student") as db:
            db['name'] = 'Tom'
            db['age'] = 19
            db['hobby'] = ['篮球', '看电影', '弹吉他']
            db['other_info'] = {'daughter' : 1, 'address' : 'xxxx'}
    
    #读取数据
    def load_method1(self):
        with shelve.open("student") as db:
            for key, value in db.items():
                print(key, ": ", value)


# 自定义class
class Student(object):
    def __init__(self, name, age, sno):
        self.name = name
        self.age = age
        self.sno = sno
    
    def __repr__(self):
        return 'Student [name: %s, age: %d, sno: %d]' % (self.name, self.age, self.sno)

class Test2:
    tom = Student('Tom', 19, 1)
    jerry = Student('Jerry', 17, 2)
    #保存数据
    def save_method2(self):
        with shelve.open("stu.db") as db:
            db['Tom'] = self.tom
            db['Jerry'] = self.jerry

    # 读取数据
    def load_method2(self):
        with shelve.open("stu.db") as db:
            print(db['Tom'])
            print(db['Jerry'])
            
if __name__ == "__main__":
    obj1 = Test1()
    obj1.save_method1()
    obj1.load_method1()
