broker_url = 'pyamqp://myuser:mypassword@localhost/myvhost'
result_backend = 'redis://localhost'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True

include=['MID_tasks', 'TSM_tasks']
