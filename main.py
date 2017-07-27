from remote import remote

MID_result = remote.send_task('MID_tasks.add', args=[1, 2], kwargs={})
print(MID_result.get(timeout=1 * 60))

MID_result = remote.send_task('TSM_tasks.prod', args=[3, 4], kwargs={})
print(MID_result.get(timeout=1 * 60))

