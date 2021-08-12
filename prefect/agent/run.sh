#!/bin/bash

sleep 20

PROJECT="project1"

prefect server create-tenant --name default --slug default > /dev/null 2>&1 || true

prefect create project $PROJECT

for FILE in /flows/*.py
do
  prefect register --project $PROJECT --path $FILE
done


prefect agent local start --agent-address tcp://prefect-agent:8892 --show-flow-logs --log-level WARNING

# note: you can set default env variables for flow runs here with: --env
