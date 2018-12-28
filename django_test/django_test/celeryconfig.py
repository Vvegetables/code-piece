#coding=utf-8
import djcelery
from _datetime import timedelta
djcelery.setup_loader()


CELERY_QUEUES = {
    'beta_tasks' : {
        'exchange' : 'beat_tasks',
        'exchange_type' : 'direct',
        'binding_type' : 'beat_tasks',
    },
    'work_queue' : {
        'exchange' : 'work_queue',
        'exchange_type' : 'direct',
        'binding_key' : 'work_queue'
    }
}


CELERY_IMPORTS = {
    'celery_task.task',
}

CELERY_DEFAULT_QUEUE = 'work_queue'

#有些情况可以防止死锁
CELERY_FORCE_EXECV = True

#设置并发的worker数量
CELERY_CONCURRENCY = 4

#允许重试
CELERY_ACKS_LATE = True

#每个worker最多执行100个任务被销毁，可以防止内存泄漏
CELERYD_MAX_TASKS_PER_CHILD = 100

#设置单个任务的最大运行时间
CELERY_TASK_TIME_LIMIT = 12 * 30



#定时任务
CELERYBEAT_SCHEDULE = {
    'task1' : {
        'task' : 'course-task',
        'schedule' : timedelta(seconds=5),
        'options' : {
            'queue' : 'beat_tasks',
        }
    }
}
