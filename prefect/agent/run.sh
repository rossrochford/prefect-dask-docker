#!/bin/bash

sleep 20

prefect server create-tenant --name default --slug default > /dev/null 2>&1 || true

prefect create project project1


prefect register --project "project1" --path /flows/list-sum-dask.py
prefect register --project "project1" --path /flows/list-sum-local.py
prefect register --project "project1" --path /flows/local-flow.py


prefect agent local start --agent-address tcp://agent:8892 --show-flow-logs --log-level WARNING

# note: you can set default env variables for flow runs here with: --env
