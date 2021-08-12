## Prefect-Dask cluster with docker-compose


### Launch cluster with 2 dask-workers
```console
$ docker-compose --build --scale dask-worker=2
```

### Test Dask (without Prefect)
```console
$ docker exec -it dask-prefect_agent_1 bash
$ python /flows/test_dask.py
$ python /flows/test_dask2.py
```

### Test Prefect
```console
$ docker exec -it dask-prefect_agent_1 bash

$ prefect run --name list-sum-local --watch --log-level DEBUG
$ prefect run --name list-sum-dask --watch --log-level DEBUG
```

### Dashboard URLs
* Prefect: http://localhost:8080
* Dask:    http://localhost:8891
