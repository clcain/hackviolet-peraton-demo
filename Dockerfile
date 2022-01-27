FROM python:3.9.10-slim-buster

WORKDIR /app

COPY main.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD python3 main.py
