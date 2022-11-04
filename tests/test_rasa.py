from app.rasa import Rasa


class TestRasa:
    def test_instantiate(self):
        rasa_1 = Rasa('my.rasa1.com')
        rasa_2 = Rasa('my.rasa2.com')

        assert rasa_1.api_url == 'my.rasa1.com'
        assert rasa_2.api_url == 'my.rasa2.com'
