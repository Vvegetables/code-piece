#coding=utf-8
'''
定时/周期任务
'''
from datetime import timedelta
from celery.schedules import crontab

CELERY_IMPORTS = (
    'task',
)
 
CELERYBEAT_SCHEDULE = {
    'ptask1': {
        'task': 'task.period_task',
        'schedule': timedelta(seconds=5),
        'args' : (4,5),
    },
    'ptask2': {
        'task' : 'task.period_task',
        'schedule' : crontab(hour=13,minute=0),
        'args' : (4,5)
    }
}
 
CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'