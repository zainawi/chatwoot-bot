from os import getenv

CHATWOOT_API = getenv('CHATWOOT_API') or 'http://localhost:3000/api/v1/'
CHATWOOT_ACCOUNT_ID = getenv('CHATWOOT_ACCOUNT_ID') or 1
CHATWOOT_AGENT_TOKEN = getenv('CHATWOOT_AGENT_TOKEN') or 'm8vdrEdmMpTJq78BmMD2HV7H'
CHATWOOT_BOT_TOKEN = getenv('CHATWOOT_BOT_TOKEN') or 'zhNcRmJZKY1KseVVXpXWemsH'
RASA_API = getenv('RASA_API') or 'http://localhost:5005'
