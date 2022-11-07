FROM python:3.8.10-slim
WORKDIR /home/smsp/chatwoot-bot
COPY . .
RUN apt-get update
RUN apt-get -y install gcc
RUN pip install -r requirements.txt
WORKDIR /home/smsp/chatwoot-bot/app
CMD uwsgi --http 0.0.0.0:5000 --master -w wsgi:app
