#coding=utf-8
import threading

#线程本地数据测试threading.local
global_num = 0

def thread_cal():
    global global_num
    for i in range(1000):
        with threading.Lock(): #保证原子操作
            global_num += 1 #不是原子操作
 
# Get 10 threads, run them and wait them all finished.
threads = []
for i in range(10):
    threads.append(threading.Thread(target=thread_cal))
    threads[i].start()
for i in range(10):
    threads[i].join()
 
# Value of global variable can be confused.
print(global_num)