#coding=utf-8
import asyncio

#1。启动事件循环机制
#2。运行协程
def test1():
    async def hello_world():
        print("hello world!")
        with open("asyncio.txt", "w+") as f:
            f.write("async")
        
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello_world())
    print("end")
    loop.close()

#循环5秒钟    
def test2():
    import datetime

    async def display_date(loop):
        end_time = loop.time() + 5.0
        while True:
            print(datetime.datetime.now())
            if (loop.time() + 1.0) >= end_time:
                break
            await asyncio.sleep(1)
    
    loop = asyncio.get_event_loop()
    # 阻止在display_date（）协程完成时返回的调用
    loop.run_until_complete(display_date(loop))
    loop.close()
    
#协程链
def test3():
    async def compute(x, y):
        print("Compute %s + %s ..." % (x, y))
        await asyncio.sleep(1.0)
        return x + y

    async def print_sum(x, y):
        result = await compute(x, y)
        print("%s + %s = %s" % (x, y, result))
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()
    
#future with run_unitl_complete
def test4():
    async def slow_operation(future):
        await asyncio.sleep(1)
        future.set_result('Future is done!')

    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(slow_operation(future))
    loop.run_until_complete(future)
    print(future.result())
    loop.close()
    
#run_forever
def test5():
    async def slow_operation(future):
        await asyncio.sleep(1)
        future.set_result('Future is done!')

    def got_result(future):
        print(future.result())
        loop.stop()
    
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(slow_operation(future))
    future.add_done_callback(got_result)
    try:
        loop.run_forever()
    finally:
        loop.close()

#并行执行多个任务
def test6():
    async def factorial(name, number):
        f = 1
        for i in range(2, number+1):
            print("Task %s: Compute factorial(%s)..." % (name, i))
            await asyncio.sleep(1)
            f *= i
        print("Task %s: factorial(%s) = %s" % (name, number, f))
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    ))
    loop.close()
    
#
def test7():
    async def nested():
        print(42)
        return 42
    
    async def main():
        print("main,", nested()) #会抛异常！不会有返回值
        print("main2", await nested())
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

if __name__ == "__main__":
    test7()