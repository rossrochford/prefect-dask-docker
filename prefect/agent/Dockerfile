FROM python:3.8.11-buster

RUN apt-get update -y
RUN apt-get install -y vim

RUN pip install prefect
RUN pip install bokeh  # temporary

COPY ./run.sh /run.sh


CMD ["/run.sh"]
