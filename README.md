## Prefect-Dask cluster with docker-compose


### Launch containers
```console
$ docker-compose --build
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

$ prefect run --name list-sum-local  # this works
$ prefect run --name list-sum-dask  # fails to complete
```
