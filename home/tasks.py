from celery import shared_task
from datetime import datetime


@shared_task
def task1():
    print('my message task1', datetime.now())
    return


@shared_task
def task2():
    print('my message task2', datetime.now())
    return

