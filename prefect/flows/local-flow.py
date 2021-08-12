import prefect
from prefect import Flow, Parameter, task
from prefect.executors import LocalExecutor

from prefect.run_configs import LocalRun
from prefect.storage import Local

# note: using Local will cause subsequent runs to be scheduled on a single node, unless you do additional steps to ensure the code is replicated to other nodes


@task(log_stdout=True)
def add_ten(i):
    return i + 10


@task(name="sum", log_stdout=True)
def list_sum(arr):
    logger = prefect.context.get("logger")
    logger.info(f"list_sum({arr})")
    return sum(arr)


# a Flows has: storage, run_config, executor
with Flow("local-flow", storage=Local(), executor=LocalExecutor()) as flow:
    flow.run_config = LocalRun(  # for dask use UniversalRun I think?
        working_dir="/",
        env={"SOME_VAR": "value"}
    )

    start_int = Parameter("start_int", default=1)
    numbers = add_ten.map(i=range(20))
    total = list_sum(numbers)



# registering a flow
# --------------------
# registering a flow, does some preliminary validation, serializes and stores the flow in your infrastructure (e.g. a local file, docker image, s3, gitlab), and sends metadata to the prefect backend/server
# how to register:
# - within the python script:  flow.register(project_name="tutorial")
# - with the command line:     $ prefect register --project "tutorial" --path local-flow.py


# running a flow
# -----------------------------
# within python:                flow.run()
# with the command line:        $ prefect run --name flow-example

# note: if we run within python, we can set the executor per run:  flow.run(executor=ex)
