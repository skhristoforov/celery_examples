from remote import remote
import time


@remote.task
def hello_TSM(x, y):
    print('TSM task start...')
    time.sleep(1)
    print('TSM task done. result: {}'.format(x * y))
    return x * y
