"""Chatwoot class definition"""

import requests


class Chatwoot:
    """Store Chatwoot information and perform some API call"""
    def __init__(self, api_url, account_id, agent_access_token, bot_access_token):
        self.api_url = api_url
        self.account_id = account_id
        self.agent_access_token = agent_access_token
        self.bot_access_token = bot_access_token

    def get_conversation_detail(self, id):
        response = requests.get(
            f'{self.api_url}/accounts/{self.account_id}/conversations/{id}',
            headers={'api_access_token': self.agent_access_token},
        )
        return response.json()

    def send_bot_message(self, message, conversation_id):
        response = requests.post(
            f'{self.api_url}/accounts/{self.account_id}/conversations/{conversation_id}/messages',
            headers={'api_access_token': self.bot_access_token},
            json={'content': message, 'message_type': 'outgoing'}
        )
        return True if response.status_code == 200 else False
