from kombu import Queue

broker_url = 'pyamqp://myuser:mypassword@localhost/myvhost'
result_backend = 'redis://localhost'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Moscow'
enable_utc = True

#  INCLUDING ALL KINDS OF TASKS
include = ['MID_tasks', 'TSM_tasks']
#  CREATING QUEUES
task_queues = [
    Queue('MID.HI',  routing_key='priority.#'),
    Queue('MID.LOW', routing_key='priority.low'),
    Queue('TSM.HI',  routing_key='priority.#'),
    Queue('TSM.LOW', routing_key='priority.low'),
]
#  DEFINING ROUTES FOR DIFFERENT KINDS OF TASKS
task_routes = {
    'MID_tasks.hello_MID_lowprior': {
        'queue': 'MID.LOW',
        'routing_key': 'priority.low'
    },
    'MID_tasks.hello_MID_hiprior': {
        'queue': 'MID.HI',
        'routing_key': 'priority.hi'
    },

    'TSM_tasks.*': {
        'queue': 'TSM.LOW',
        'routing_key': 'priority.low'
    }
}

task_default_routing_key = 'priority.low'
