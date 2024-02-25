FROM python:3.10-alpine


COPY . /api
WORKDIR /api
RUN ls .
RUN pip install -U setuptools pip
RUN pip install -r requirements.txt

EXPOSE 8081


CMD ["gunicorn", "--bind", "0.0.0.0:8081", "--workers", "3", "server:app"]