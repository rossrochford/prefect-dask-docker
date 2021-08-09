FROM python:3.8.11-buster

RUN apt-get update -y
RUN apt-get install -y vim
RUN pip install prefect
RUN pip install bokeh  # temporary

RUN mkdir -p /root/.prefect/
COPY ./prefect_backend_config.toml /root/.prefect/backend.toml

COPY ./run.sh /run.sh

RUN mkdir -p /flows
COPY ./flows /flows/


CMD ["/run.sh"]
