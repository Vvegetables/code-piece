#coding = utf-8

'''
在当前的目录下执行：
    celery -A task worker --loglevel=info -P eventlet
    'task' == 这个目录中的task.py的文件名字
'''

import sys
import time

from celery import Celery
from celery.task.base import Task


app = Celery('task',backend='redis://localhost:6379/1',broker='redis://localhost:6379/2')

app.config_from_object('celery_config')


class MyTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('task done:{0}'.format(retval))
        return Task.on_success(self, retval, task_id, args, kwargs)
    
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print("task fail , reason:{0}".format(exc))
        Task.on_failure(self, exc, task_id, args, kwargs, einfo)

def multiple(x,y):
    return x * y
    
@app.task(base=MyTask)
def add2(x,y):
    return x+y


@app.task(bind=True)
def period_task(self,x,y):
#     print('period task done: {0}'.format(self.request.id))
    print(multiple(x, y))

@app.task
def add(x,y):
    return x +y 


@app.task(bind=True)
def test_mes(self):
    for i in range(1,11):
        time.sleep(0.1)
        self.update_state(state="PROGRESS",meta={'p':i*10})
    
    return 'finish'

def pm(body):
    res = body.get('result')
    if body.get('status') == 'PROGRESS':
        sys.stdout.write('\r任务进度: {0}%'.format(res.get('p')))
        sys.stdout.flush()
    else:
        print('\r')
        print(res)

'''
自定义执行过程
'''
def test_procedure():            
    result = add2.delay(4,4) 
    
    while not result.ready():
        time.sleep(1)
    
    print(result.get())

'''
异步执行
'''  
def test_ascny_call():
    #不要直接add(4,4),这里需要用celery提供的接口delay进行调用
    result = add.delay(4,4) 
    print(add(4,4))
    while not result.ready():
        time.sleep(1)

    print(result.get()) 
    
'''
周期任务、定时任务
''' 
def test_period_task():
    period_task()
    
'''
任务回调
'''
def test_callback():
    r = test_mes.delay()
    print(r.get(on_message=pm, propagate=False))
    
if __name__ == "__main__":
    pass
    
    
    
    
    
    
    