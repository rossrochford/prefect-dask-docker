import os

from prefect.executors import DaskExecutor


SCHEDULER_ADDRESS = os.environ['PREFECT__ENGINE__EXECUTOR__DASK__ADDRESS']

ex = DaskExecutor(address=SCHEDULER_ADDRESS)
ctx = ex.start()

with ctx:
    future = ex.submit(lambda: 1)
    if future.result() == 1:
        print('success')
    else:
        print('failed')
