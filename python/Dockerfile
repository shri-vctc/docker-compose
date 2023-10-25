FROM python:slim
WORKDIR /usr/app/src

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY main.py ./