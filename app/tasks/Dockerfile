FROM python:3.10.13-alpine
ENV C_FORCE_ROOT true

COPY . /worker
WORKDIR /worker

RUN pip install --upgrade pip==23.3.2
RUN pip install -r requirements.txt