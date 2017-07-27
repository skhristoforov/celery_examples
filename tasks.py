from celery import Celery

remote = Celery()
remote.config_from_object('celeryconfig')

@remote.task
def add(x, y):
    return x + y
