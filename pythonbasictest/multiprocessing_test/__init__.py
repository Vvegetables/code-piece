#coding=utf-8
'''
process.deamon = True：
    这表示主进程不管子进程有没有执行结束，一旦主进程结束，子进程也将一起结束
process.join()
    这表示主进程将在此阻塞，直到子进程执行结束
'''
#https://blog.csdn.net/cityzenoldwang/article/details/78584175
#https://blog.csdn.net/dutsoft/article/details/54694798
#https://www.cnblogs.com/eailoo/p/9174257.html
'''
单进程
'''

from multiprocessing import Process
import multiprocessing
import os
import time


def task(msg):
    print('hello, %s' % msg)
    time.sleep(1)


if __name__ == '__main__':
    p = Process(target=task, args=('world',))

    p.start()
    if p.is_alive():
        print('Process: %s is running' % p.pid)
    p.join()
'''
这段代码的执行过程：在主进程中创建子进程，然后调用start()启动子进程，调用join()等待子进程执行完，再继续执行主进程的整个的执行流程。 
控制子进程进入不同阶段的是 start(), join(), is_alive(), terminate(), exitcode() 方法，这些方法只能在创建子进程的进程中执行。

创建：创建进程需要一个 function 和相关参数，参数可以是dictProcess(target=func, args=(), kwargs = {})，name 可以用来标识进程。

关闭：close停止接收新的任务，如果还有任务来，就会抛出异常。 join 是等待所有任务完成。 join 必须要在 close 之后调用，否则会抛出异常。

等待：在UNIX平台上，当某个进程终结之后，该进程需要被其父进程调用wait，否则进程成为僵尸进程(Zombie)。所以在这里，我们调用了Process对象的join()方法 ，实际上等同于wait的作用。 
对于多线程来说，由于只有一个进程，所以不存在此必要性。

结束：terminate() 结束工作进程，不再处理未完成的任务。
'''
    
'''
多进程（也可以使用多个单进程创建）这里使用进程池pool
'''
'''
Pool 可以提供指定数量的进程供用户使用，默认是 CPU 核数。当有新的请求提交到 Poll 的时候，如果池子没有满，会创建一个进程来执行，否则就会让该请求等待。 
- Pool 对象调用 join 方法会等待所有的子进程执行完毕 
- 调用 join 方法之前，必须调用 close 
- 调用 close 之后就不能继续添加新的 Process 了

pool.apply_async
    apply_async 方法用来同步执行进程，允许多个进程同时进入池子。
    
pool.apply
    apply(func[, args[, kwds]])
    该方法只能允许一个进程进入池子，在一个进程结束之后，另外一个进程才可以进入池子。
'''

def run_task(name):
    print('Task {0} pid {1} is running, parent id is {2}'.format(name, os.getpid(), os.getppid()))
    time.sleep(1)
    print('Task {0} end.'.format(name))

if __name__ == '__main__':
    print('current process {0}'.format(os.getpid()))
    p = multiprocessing.Pool(processes=3)
    for i in range(6):
        p.apply_async(run_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All processes done!')

'''
进程间的通信
pipe通常是两个进程之间
queue是多个进程之间
'''

'''
单个锁控制
'''

#db文件内容  {"count": 0}

'''lock = Lock()　　创建锁对象

　　lock.acquire()　　查询钥匙,如果有就拿走,如果没有就等待

　　lock.release()　　归还钥匙

　　lock可以使用with上下文进行管理(类似于文件读取)

　　with lock:

    print('hello' )
'''

import json
import time
from multiprocessing import Process,Lock
def search(i):
    f =open('db')
    ticket_dic =json.load(f)
    f.close()
    print(f"{i} 正在查票,剩余票数{ticket_dic['count']}")

def buy(i):
    with open('db') as f: ticket_dic = json.load(f)
    time.sleep(0.2)
    if ticket_dic['count'] > 0:
        ticket_dic['count'] -= 1
        print(f'{i} 买到票了')
        time.sleep(0.2)
        with open('db','w') as f :json.dump(ticket_dic,f)
    else:
        print(f"{i} 太火爆被抢购一空了,剩余票数{ticket_dic['count']}")


# def get_ticket(i,lock):
#     search(i)
#     lock.acquire()
#     buy(i)
#     lock.release()

def get_ticket(i,lock):
    search(i)
    with lock:
        buy(i)

if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=get_ticket,args=(i,lock))
        p.start()


'''sem = Semaphore(4)　　创建锁对象,4把钥匙,可以被连续acquire4次

　　sem.acquire()　　查询钥匙,如果有就拿走,如果没有就等待

　　sem.release()　　归还钥匙

　　sem 可以使用with上下文进行管理(类似于文件读取)

　　with sem:

　　　　print('hello' )
'''
#测试
from multiprocessing import Semaphore,Process
import time
import random        
# def ktv(sem,i):
#     sem.acquire()
#     print(f'{i}走进ktv')
#     time.sleep(random.randint(1,3))
#     print(f'{i}走出ktv')
#     sem.release()

def ktv(sem,i):
    with sem:
        print(f'{i}走进ktv')
        time.sleep(random.randint(1,3))
        print(f'{i}走出ktv')


if __name__ == '__main__':
    sem = Semaphore(4)
    for i in range(10):
        p = Process(target=ktv,args=(sem,i))
        p.start()  
    
    
    
    
    
    




    