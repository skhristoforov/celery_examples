from MID_tasks import add
from TSM_tasks import prod

print(add.delay(4, 4).get(timeout=1 * 60))
print(prod.delay(4, 4).get(timeout=1 * 60))
