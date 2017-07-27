from MID_tasks import hello_MID_lowprior
from MID_tasks import hello_MID_hiprior
from TSM_tasks import hello_TSM

MID_result_hi, MID_result_low, TSM_result = [], [], []
for t in range(100):
    MID_result_low.append(hello_MID_lowprior.delay(1, 2))
    TSM_result.append(hello_TSM.delay(3, 4))

for t in range(100):
    MID_result_hi.append(hello_MID_hiprior.delay(1, 2))
    MID_result_low.append(hello_MID_lowprior.delay(1, 2))
    TSM_result.append(hello_TSM.delay(3, 4))


for t in range(100):
    print(MID_result_hi[t].get(timeout=1 * 60))
for t in range(200):
    print(MID_result_low[t].get(timeout=1 * 60))
    print(TSM_result[t].get(timeout=1 * 60))

