from celery import Celery

remote = Celery()
remote.config_from_object('celeryconfig')


if __name__ == '__main__':
   remote.start()
