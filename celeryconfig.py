broker_url = 'pyamqp://myuser:mypassword@localhost/myvhost'
result_backend = 'redis://localhost'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Moscow'
enable_utc = True
include = ['MID_tasks', 'TSM_tasks']
task_queues = ['priority.hi', 'priority.medium', 'priority.low']
task_routes = {
    'MID_tasks.hello_MID': {'queue': 'priority.hi'},
    'MID_tasks.hello_TSM': {'queue': 'priority.medium'}
}
