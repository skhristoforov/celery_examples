from remote import remote
import time


@remote.task
def hello_MID(x, y):
    print('MID task start...')
    time.sleep(3)
    print('MID task done. result: {}'.format(x + y))
    return x + y
