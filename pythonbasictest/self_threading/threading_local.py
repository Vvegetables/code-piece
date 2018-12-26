#coding=utf-8
import threading

#线程本地数据测试threading.local
global_num = 0
global_data = threading.local()

def show():
    print(threading.current_thread().getName(),global_data.num)

def thread_cal():
    global global_num
    for _ in range(1000):
        with threading.Lock(): #保证原子操作
            global_num += 1 #不是原子操作
            
def thread_cal2():
    global_data.num = 0
    for _ in range(1000):
        global_data.num += 1
    show()

def synchr_test(): 
    # Get 10 threads, run them and wait them all finished.
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=thread_cal))
        threads[i].start()
    for i in range(10):
        threads[i].join()
     
    # Value of global variable can be confused.
    print(global_num)
    
def threading_local_test():
    # Get 10 threads, run them and wait them all finished.
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=thread_cal2))
        threads[i].start()
    for i in range(10):
        threads[i].join()
     
    # Value of global variable can be confused.
    
    print("Main thread: ", global_data.__dict__) # {}
    
if __name__ == "__main__":
#     synchr_test()
    threading_local_test()
    