#coding=utf-8

import time

from django.http import JsonResponse

from celery_task.task import CourseTask, EmailSendTask
from django_email import send_single_email


def do(request):
    #执行异步任务
    print('start do request')
    
    #CourseTask.delay()
    CourseTask.apply_async(args=('hello',),queue='work_queue')
    print('end do request')
    
    return JsonResponse({'result':'ok'})

def celery_send_email(request):
    start = time.time()
    print("starttime: ", start)
    EmailSendTask.apply_async(queue='work_queue')
    end = time.time()
    print("endtime: ", end)
    print("span: ", end - start)
    
    return JsonResponse({'time-takes': end - start})

def sync_send_email(request):
    start = time.time()
    print("starttime: ", start)
    send_single_email()
    end = time.time()
    print("endtime: ", end)
    print("span: ", end - start)
    
    return JsonResponse({'time-takes': end - start})