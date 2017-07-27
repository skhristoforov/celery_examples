from kombu import Queue

broker_url = 'pyamqp://myuser:mypassword@localhost/myvhost'
result_backend = 'redis://localhost'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Moscow'
enable_utc = True

include = ['MID_tasks', 'TSM_tasks']
task_queues = [
    Queue('Queue.MID', routing_key='priority.#'),
    Queue('Queue.TSM', routing_key='priority.#'),
]

task_default_routing_key = 'priority.medium'
task_routes = {
    'MID_tasks.*': {'queue': 'Queue.MID'},
    'TSM_tasks.*': {'queue': 'Queue.TSM'}
}
