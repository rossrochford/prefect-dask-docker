import os

import dask
from dask.distributed import Client
import distributed


SCHEDULER_ADDRESS = os.environ['PREFECT__ENGINE__EXECUTOR__DASK__ADDRESS']


def inc(x):
    dask.distributed.get_worker().log_event('inc-log', {'x': x})
    return x + 1

def square(x):
    return x*x


client = Client(SCHEDULER_ADDRESS)
x = client.submit(inc, 10)
print(x.result())

y = client.submit(inc, x)
print(y.result())

#with distributed.get_task_stream(plot='save', filename="/var/log/task-stream.html") as ts:
#    f = client.map(square, [x for x in range(100)])
#    distributed.wait(f)


L = client.map(inc, range(1000))
list_incremented = client.gather(L)
print(list_incremented)


total = client.submit(sum, L)
print(total.result())

events = client.get_events('inc-log')
print(events)

'''
# note: functions that use randomness and not 'pure' becuase they give 
# different outputs for the same input, dask needs to be told this
import numpy as np
client.submit(np.random.random, 1000, pure=False)
'''
