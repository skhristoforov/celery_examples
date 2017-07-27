from remote import remote
import time


def hello_MID(x, y):
    print('MID task start...')
    time.sleep(1)
    print('MID task done. result: {}'.format(x + y))
    return x + y


@remote.task
def hello_MID_lowprior(**kwargs):
    print('Starting hello MID with low priority')
    return hello_MID(**kwargs)


@remote.task
def hello_MID_hiprior(**kwargs):
    print('Starting hello MID with hi priority')
    return hello_MID(**kwargs)
