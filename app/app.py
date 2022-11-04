from chatwoot import Chatwoot
from flask import Flask, request
from incoming_message import IncomingMessage
import json
import logging
from rasa import Rasa
import settings as settings

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route("/", methods=['POST'])
def index():
    payload = json.loads(request.data)

    try:
        payload = IncomingMessage(payload)
    except ValueError:
        return 'Payload partially consumed'

    if payload.get_content_type() != 'text':
        return 'Payload partially consumed'

    chatwoot = Chatwoot(
        settings.CHATWOOT_API,
        settings.CHATWOOT_ACCOUNT_ID,
        settings.CHATWOOT_AGENT_TOKEN,
        settings.CHATWOOT_BOT_TOKEN,
    )

    if payload.has_assignee():
        return 'Payload partially consumed'

    rasa = Rasa(settings.RASA_API)
    sender = payload.get_sender_name()
    message = payload.get_message_content()
    res_msg = rasa.get_response(sender, message)
    for msg in res_msg:
        chatwoot.send_bot_message(msg, payload.get_conversation_id())

    app.logger.info({
        'incoming': {
            'sender': sender,
            'message': message
        },
        'outgoing': {
            'sender': 'Bot',
            'messages': res_msg
        },
    })

    return 'Payload consumed'
