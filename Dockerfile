FROM python:3.10-alpine

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app

COPY main.py /app

RUN pip3 install -r requirements.txt

CMD "gunicorn -w 4 -b 0.0.0.0:8000 --access-logfile log/access.log --error-logfile log/error.log main:app"