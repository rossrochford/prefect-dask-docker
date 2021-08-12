import os

import dask.distributed
import prefect
from prefect import Flow, Parameter, task
from prefect.executors import DaskExecutor

from prefect.run_configs import UniversalRun
from prefect.storage import Local

SCHEDULER_ADDRESS = os.environ['PREFECT__ENGINE__EXECUTOR__DASK__ADDRESS']


@task(log_stdout=True)
def add_ten(i):
    dask.distributed.get_worker().log_event('add-ten', {'i': i})
    return i + 10


@task(name="sum", log_stdout=True)
def list_sum(arr):
    logger = prefect.context.get("logger")
    logger.info(f"list_sum({arr})")
    return sum(arr)


# a Flows has: storage, run_config, executor
with Flow("dask-flow", storage=Local()) as flow:
    flow.run_config = UniversalRun(  # for dask use UniversalRun I think?
        env={"SOME_VAR": "value"}
    )

    start_int = Parameter("start_int", default=1)
    numbers = add_ten.map(i=range(20))
    total = list_sum(numbers)


# connect to an existing dask cluster
flow.executor = DaskExecutor(address=SCHEDULER_ADDRESS)
