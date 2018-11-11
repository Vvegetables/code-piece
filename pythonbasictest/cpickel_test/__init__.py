#coding=utf-8
'''
在python中提供了两个模块：cpickle和pickle来实现序列化，前者是c编写，速度比后者会快1000倍左右。
但是它不支持Pickler（）和Unpickler（）类的子类化，因为在cPickle中这些是函数，而不是类。
大多数应用程序不需要此功能。并且他们的api基本上是一样的，所以我们一般先找cPickle然后再考虑pickle
'''
try:
    import cPickle as pickle
except:
    import pickle
    
'''
用于序列化的两个模块
　　json：用于字符串和Python数据类型间进行转换(可以达到跨语言的目的)
　　pickle: 用于python特有的类型和python的数据类型间进行转换
　　json提供四个功能：dumps,dump,loads,load
　　pickle提供四个功能：dumps,dump,loads,load

pickle可以存储什么类型的数据呢？
所有python支持的原生类型：布尔值，整数，浮点数，复数，字符串，字节，None。
由任何原生类型组成的列表，元组，字典和集合。
函数，类，类的实例
pickle模块中常用的方法有：
    1. pickle.dump(obj, file, protocol=None,)

    必填参数obj表示将要封装的对象

    必填参数file表示obj要写入的文件对象，file必须以二进制可写模式打开，即“wb”

    可选参数protocol表示告知pickler使用的协议，支持的协议有0,1,2,3，
    默认的协议是添加在Python 3中的协议3。　
    2. pickle.load(file,*,fix_imports=True, encoding="ASCII", errors="strict")

    必填参数file必须以二进制可读模式打开，即“rb”，其他都为可选参数

    3. pickle.dumps(obj)：以字节对象形式返回封装的对象，不需要写入文件中

    4. pickle.loads(bytes_object): 从字节对象中读取被封装的对象，并返回

 pickle模块可能出现三种异常：

    1. PickleError：封装和拆封时出现的异常类，继承自Exception

    2. PicklingError: 遇到不可封装的对象时出现的异常，继承自PickleError

    3. UnPicklingError: 拆封对象过程中出现的异常，继承自PickleError　　
'''
# dumps功能
data = ['aa', 'bb', 'cc']  
# dumps 将数据通过特殊的形式转换为只有python语言认识的字符串,写成变量形式
p_str = pickle.dumps(data)
print(p_str)

#loads功能 #将格式化的变量重新变成python的数据结构
mes = pickle.loads(p_str)
print(mes)

#dump功能，直接编码到文件中
with open('test.txt','wb') as f:
    pickle.dump(data,f)

#load功能 从文件中读出数据，转换成python的数据结构
with open('test.txt','rb') as f:
    pr = pickle.load(f)
    print(pr)


    
    
    
    
    
    
    
    
    
    
    
