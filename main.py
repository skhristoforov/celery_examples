# from remote import remote
#
# MID_result = remote.send_task('MID_tasks.hello_MID',  args=[1, 2], kwargs={})
# TSM_result = remote.send_task('TSM_tasks.hello_TSM',  args=[3, 4], kwargs={})

from MID_tasks import hello_MID
from TSM_tasks import hello_TSM

MID_result = hello_MID.delay(1, 2)
TSM_result = hello_TSM.delay(3, 4)

print(MID_result.get(timeout=1 * 60))
print(TSM_result.get(timeout=1 * 60))

