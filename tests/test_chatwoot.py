from app.chatwoot import Chatwoot


class TestChatwoot:
    def test_instantiate(self):
        chatwoot_1 = Chatwoot(
            'my.chatwoot1.com',
            1,
            'agent_access_token_1',
            'bot_access_token_1',
        )
        chatwoot_2 = Chatwoot(
            'my.chatwoot2.com',
            2,
            'agent_access_token_2',
            'bot_access_token_2',
        )

        assert chatwoot_1.api_url == 'my.chatwoot1.com'
        assert chatwoot_1.account_id == 1
        assert chatwoot_1.agent_access_token == 'agent_access_token_1'
        assert chatwoot_1.bot_access_token == 'bot_access_token_1'

        assert chatwoot_2.api_url == 'my.chatwoot2.com'
        assert chatwoot_2.account_id == 2
        assert chatwoot_2.agent_access_token == 'agent_access_token_2'
        assert chatwoot_2.bot_access_token == 'bot_access_token_2'
