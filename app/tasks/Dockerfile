FROM python:3.10-alpine
ENV C_FORCE_ROOT true

COPY . /worker
WORKDIR /worker

RUN pip install -U setuptools pip
RUN pip install -r requirements.txt