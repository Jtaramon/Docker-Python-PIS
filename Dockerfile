FROM python:3.7.4-slim-buster
COPY . usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requierements.txt

ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload