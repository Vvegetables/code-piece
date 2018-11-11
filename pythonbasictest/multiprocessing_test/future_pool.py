#coding=utf-8

import concurrent.futures
import math
import os
import random
import time
import datetime


# PRIMES = [
#     112272535095293,
#     112582705942171,
#     112272535095293,
#     115280095190773,
#     115797848077099,
#     1099726899285419]
# 
# def is_prime(n):
#     if n % 2 == 0:
#         return False
# 
#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3, sqrt_n + 1, 2):
#         if n % i == 0:
#             return False
#     return True
# 
# def main():
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
#             print('%d is prime: %s' % (number, prime))
# 
# if __name__ == '__main__':
#     main()



def handle(res):
    res=res.result()
    print("handle res %s"%res)


def read(q):
    print('Get %s from %s queue at time %s' % (q,os.getpid(),datetime.datetime.now()))
    time.sleep(random.random())
    return os.getpid()

def main():
    futures = set()
    #开启进程池
    with concurrent.futures.ProcessPoolExecutor() as executor:
        
        #left==各个进程的返回值
        left = executor.map(read,(chr(ord('A')+i) for i in range(26))) #map取代了for+submit
        
#         for q in (chr(ord('A')+i) for i in range(26)):
#             future = executor.submit(read, q) #开启一个进程任务，异步操作。
# #             executor.submit(read,q).result() #开启一个进程任务，同步操作。
#             
#             #使用回调函数
#             future.add_done_callback(handle)
#             
#             #将任务加入set
#             futures.add(future)
    
    #这里是等待所有进程完成，才继续执行下边代码，wait=false则不完成也继续执行
    executor.shutdown(wait=True) #关门等待所有进程完成
    
#     try:
#         for future in concurrent.futures.as_completed(futures): #等待所有子进程都执行完毕。
#             err = future.exception() #收集子进程出现的异常
#             print(future.result()) #收集子进程返回的结果
#             if err is not None:
#                 raise err
#     except KeyboardInterrupt:
#         print("stopped by hand")

if __name__ == '__main__':
    main() 
    
    
    
    