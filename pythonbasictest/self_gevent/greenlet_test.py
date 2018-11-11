#coding=utf-8

from greenlet import greenlet, \
    getcurrent  #返回当前的greenlet实例

'''
https://www.cnblogs.com/xybaby/p/6337944.html

dead：如果greenlet执行结束，那么该属性为true
run：当greenlet启动的时候会调用到这个callable，如果我们需要继承greenlet.greenlet时，需要重写该方法
'''


#demo1
#switch切换使用

# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#     
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#     
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# 
# gr1.switch()

#demo2
#有参数，有返回值

# def test3(x, y):
#     z = gr2.switch(x+y)
#     print('test1 ', z)
# 
# def test4(u):
#     print('test2 ', u)
#     gr1.switch(10)
# 
# gr1 = greenlet(test3)
# gr2 = greenlet(test4)
# print(gr1.switch("hello", " world"))

#demo3
#parent的使用
# def test1(x, y):
#     print(id(getcurrent()), id(getcurrent().parent)) # 40240272 40239952
#     z = gr2.switch(x+y)
#     print('back z', z)
# 
# def test2(u):
#     print(id(getcurrent()), id(getcurrent().parent)) # 40240352 40239952
#     return('hehe')  #直接返回生成它的地方。不在返回switch到它的地方
# 
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# print(id(getcurrent()), id(gr1), id(gr2))     # 40239952, 40240272, 40240352
# print(gr1.switch("hello", " world"), 'back to main')    # hehe back to main

'''
上述例子可以看到，尽量是从test1所在的协程gr1 切换到了gr2，但gr2的parent还是’main’ greenlet，因为默认的parent取决于greenlet的创生环境。
另外 在test2中return之后整个返回值返回到了其parent，而不是switch到该协程的地方（即不是test1），
这个跟我们平时的函数调用不一样，记住“switch not call”。对于异常 也是展开至parent
'''

#demo4
#异常的抛出，会直接抛给parent

# def test1(x, y):
#     try:
#         z = gr2.switch(x+y)
#     except Exception:
#         print('catch Exception in test1')
# 
# def test2(u):
#     assert False
# 
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# try:
#     gr1.switch("hello", " world")
# except:
#     print('catch Exception in main')
    
    
#demo5
def test1():
    gr2.switch(1)
    print('test1 finished')

def test2(x):
    print('test2 first', x)
    z = gr1.switch()
    print('test2 back', z)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
print('gr1 is dead?: %s, gr2 is dead?: %s' % (gr1.dead, gr2.dead))
gr2.switch()
print('gr1 is dead?: %s, gr2 is dead?: %s' % (gr1.dead, gr2.dead))
print(gr2.switch(10))

'''
只有当协程对应的函数执行完毕，协程才会die，所以第一次Check的时候gr2并没有die，因为第9行切换出去了就没切回来。在main中再switch到gr2的时候， 执行后面的逻辑，gr2 die
如果试图再次switch到一个已经是dead状态的greenlet会怎么样呢，事实上会切换到其parent greenlet。
'''



