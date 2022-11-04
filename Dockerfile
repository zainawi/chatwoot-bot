FROM python:3.8.10-alpine
WORKDIR /home/smsp/chatwoot_bot_connector
COPY . .
RUN pip install -r requirements.txt
CMD flask --app app/app run --host 0.0.0.0
