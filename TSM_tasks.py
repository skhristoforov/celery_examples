from remote import remote


@remote.task
def prod(x, y):
    return x * y
