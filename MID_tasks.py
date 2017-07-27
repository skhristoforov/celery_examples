from remote import remote
import time


def hello_MID(x, y):
    print('MID task start...')
    result = x + y
    print('MID task done. result: {}'.format(result))
    return result


@remote.task
def hello_MID_lowprior(*args, **kwargs):
    print('Starting hello MID with low priority')
    time.sleep(1)
    return hello_MID(*args, **kwargs)


@remote.task
def hello_MID_hiprior(*args, **kwargs):
    print('Starting hello MID with hi priority')
    time.sleep(3)
    return hello_MID(*args, **kwargs)
