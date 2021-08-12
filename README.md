## Prefect-Dask cluster with docker-compose


### Launch cluster with 2 dask-workers
```console
$ docker-compose up --build --scale dask-worker=2
```

### Test Dask without Prefect
```console
$ docker exec -it prefect-dask-docker_prefect-agent_1 bash

#  inside agent container
$ python /dask_tests/test_dask.py
$ python /dask_tests/test_dask2.py
```

### Test Prefect
```console
$ docker exec -it prefect-dask-docker_prefect-agent_1 bash

#  inside agent container
$ prefect run --name list-sum-local --watch --log-level DEBUG
$ prefect run --name list-sum-dask --watch --log-level DEBUG
$ prefect run --name dask-flow --watch --log-level DEBUG
```

### Dashboard URLs
* Prefect: http://localhost:8080
* Dask:    http://localhost:8891
