FROM python:3.8.10-slim
WORKDIR /home/smsp/chatwoot_bot_connector
COPY . .
RUN apt-get update
RUN apt-get -y install gcc
RUN pip install -r requirements.txt
WORKDIR /home/smsp/chatwoot_bot_connector/app
CMD uwsgi --http 0.0.0.0:5000 --master -w wsgi:app
