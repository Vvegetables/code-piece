#coding=utf-8

'''
启动脚本：
python manage.py celery worker -l INFO

python manage.py celery beat -l INFO

python manage.py celery flower
    --address=0.0.0.0 --port=5555 --broker=xxxx --basic_auth=username:password
    
supervisor 进程管理工具
'''

import time
from celery.task import Task
from django_email import send_single_email

class CourseTask(Task):
    name = "course-task"
    
    def run(self,*args,**kwargs):
        print('start course task')
        
        time.sleep(2)
        
        print(f"args={args},kwargs={kwargs}")
        print('end course task')
        
class EmailSendTask(Task):
    name = "email-task"
    
    def run(self, *args, **kwargs):
        send_single_email()
