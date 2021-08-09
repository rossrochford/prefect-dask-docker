import datetime
import os
import random
import sys
from time import sleep

import prefect
from prefect import task, Flow
from prefect.executors import LocalExecutor


@task(log_stdout=True)
def inc(x):
    logger = prefect.context.get("logger")
    logger.info(f"inc({x})")
    sleep(random.random() / 10)
    return x + 1


@task(log_stdout=True)
def dec(x):
    logger = prefect.context.get("logger")
    logger.info(f"dec({x})")
    sleep(random.random() / 10)
    return x - 1


@task(log_stdout=True)
def add(x, y):
    logger = prefect.context.get("logger")
    logger.info(f"add({x}, {y})")
    sleep(random.random() / 10)
    return x + y


@task(name="sum", log_stdout=True)
def list_sum(arr):
    logger = prefect.context.get("logger")
    logger.info(f"list_sum({arr})")
    return sum(arr)


with Flow("list-sum-local") as flow:
    flow.executor = LocalExecutor()
    incs = inc.map(x=range(50))
    decs = dec.map(x=range(50))
    adds = add.map(x=incs, y=decs)
    total = list_sum(adds)


'''
# note: we can avoid explicitly setting the executor and dask-scheduler address by setting these environment variables:

$ export PREFECT__ENGINE__EXECUTOR__DEFAULT_CLASS="prefect.executors.DaskExecutor"
$ export PREFECT__ENGINE__EXECUTOR__DASK__ADDRESS="tcp://10.0.0.41:8786"
'''


#executor = DaskExecutor(address="tcp://10.0.0.41:8786")
#flow.run(executor=executor)
