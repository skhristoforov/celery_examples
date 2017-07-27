from remote import remote


@remote.task
def add(x, y):
    return x + y
