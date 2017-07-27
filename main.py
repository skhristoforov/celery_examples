from remote import remote

MID_result = remote.send_task('MID_tasks.hello_MID',  args=[1, 2], kwargs={})
TSM_result = remote.send_task('TSM_tasks.hello_TSM', args=[3, 4], kwargs={})

MID_result.get(timeout=1 * 60)
TSM_result.get(timeout=1 * 60)

