#coding=utf-8
'''
博客地址：https://www.cnblogs.com/tkqasn/p/5700281.html
'''

import threading
import time

def action(arg):
    time.sleep(1)
    print("the arg is:%s\r" % arg)

def main():
    
    #设置线程阻塞函数的超时参数允许的最大值，大于此值将发生异常
    threading.TIMEOUT_MAX = 60
    
    for i in range(4):
        t = threading.Thread(target=action,args=(i,))
        t.start()
    #获得活跃的线程数量
    print(threading.active_count())
    #获得线程标识符
    print(threading.get_ident())
    #返回当前活动的所有Thread对象的列表。该列表包括守护线程
    print(threading.enumerate())
    #返回主线程
    print(threading.main_thread())

#继承类方法写线程
class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread,self).__init__()
        self.arg = arg
    
    def run(self):
        time.sleep(1)
        print("the arg is:%s\r" % self.arg)
        
def class_thread_test():
    for i in range(4):
        t = MyThread(i)
        t.start()

if __name__ == "__main__":
    #main()
    class_thread_test()

