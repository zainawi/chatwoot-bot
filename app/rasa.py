import requests
import json

class Rasa:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_response(self, sender, message):
        response = requests.post(
            f'{self.api_url}/webhooks/rest/webhook',
            json={'sender': sender, 'message': message},
        )
        payload = response.json()
        messages = []
        for res in payload:
            if 'text' in res:
                messages.append(res['text'])
            if 'image' in res:
                messages.append(res['image'])
        return messages
