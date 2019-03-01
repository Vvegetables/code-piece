'''
该concurrent.futures模块提供了一个用于异步执行callables的高级接口
线程：
    ThreadPoolExecutor
进程：
    ProcessPoolExecutor
'''
import concurrent.futures

#ThreadPoolExecutor实例
def threadpoolexecutor_test():
    import requests
    URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

    # 检索单个页面并报告URL和内容
    def load_url(url, timeout):
        with requests.request("GET", url, timeout=timeout) as conn:
            return conn.content
    
    # 我们可以使用with语句来确保及时清理线程
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # 启动加载操作并使用其URL标记每个future
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        print("next1")
        print("next2")
        print("next3")
        #校验异步调用结果，在校验之前代码执行不会堵塞！
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))

import math
def is_prime(n):
        if n % 2 == 0:
            return False
    
        sqrt_n = int(math.floor(math.sqrt(n)))
        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
        return True
    
#ProccessPoolExecutor实例
def proccesspoolexecutor_test():
    PRIMES = [
        112272535095293,
        112582705942171,
        112272535095293,
        115280095190773,
        115797848077099,
        1099726899285419]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
            

if __name__ == "__main__":
#     threadpoolexecutor_test()
    proccesspoolexecutor_test()
