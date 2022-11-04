from app.incoming_message import IncomingMessage
from pytest import fixture, raises

@fixture
def incoming_no_assignee():
    return IncomingMessage({
        "content_type": "text",
        "content": "Hai",
        "conversation": {
            "id": 9,
            "meta": {
                "assignee": None,
            },
        },
        "created_at": "2022-11-04T07:53:51.946Z",
        "id": 254,
        "inbox": {
            "id": 1,
            "name": "Vue"
        },
        "message_type": "incoming",
        "sender": {
            "name": "Siapa Saya",
        },
        "event": "message_created"
    })

@fixture
def incoming_with_assignee():
    return IncomingMessage({
        "content_type": "text",
        "content": "Hai",
        "conversation": {
            "id": 10,
            "meta": {
                "assignee": {
                    "name": "Zain"
                },
            },
        },
        "created_at": "2022-11-04T07:53:51.946Z",
        "id": 254,
        "inbox": {
            "id": 1,
            "name": "Vue"
        },
        "message_type": "incoming",
        "sender": {
            "name": "Siapa Hayo",
        },
        "event": "message_created"
    })


class TestIncomingMessage:
    def test_invalid_event(self):
        with raises(ValueError):
            IncomingMessage({
                "conversation": {
                    "id": 12,
                    "meta": {
                        "assignee": None,
                    },
                },
                "created_at": "2022-11-04T07:53:51.946Z",
                "id": 254,
                "inbox": {
                    "id": 1,
                    "name": "Vue"
                },
                "event": "conversation_created"
            })
        with raises(ValueError):
            IncomingMessage({
                "content_type": "text",
                "content": "Hai",
                "conversation": {
                    "id": 11,
                    "meta": {
                        "assignee": None,
                    },
                },
                "created_at": "2022-11-04T07:53:51.946Z",
                "id": 254,
                "inbox": {
                    "id": 1,
                    "name": "Vue"
                },
                "message_type": "outgoing",
                "sender": {
                    "name": "Siapa Saya",
                },
                "event": "message_created"
            })

    def test_get_content_type(self, incoming_no_assignee):
        assert incoming_no_assignee.get_content_type() == "text"

    def test_get_message_type(self, incoming_no_assignee):
        assert incoming_no_assignee.get_message_type() == "incoming"

    def test_get_message_content(self, incoming_no_assignee):
        assert incoming_no_assignee.get_message_content() == "Hai"

    def test_has_assignee(self, incoming_no_assignee, incoming_with_assignee):
        assert incoming_no_assignee.has_assignee() == False
        assert incoming_with_assignee.has_assignee() == True

    def test_get_sender_name(self, incoming_no_assignee, incoming_with_assignee):
        assert incoming_no_assignee.get_sender_name() == 'Siapa Saya'
        assert incoming_with_assignee.get_sender_name() == 'Siapa Hayo'

    def test_get_conversation_id(self, incoming_no_assignee, incoming_with_assignee):
        assert incoming_no_assignee.get_conversation_id() == 9
        assert incoming_with_assignee.get_conversation_id() == 10
