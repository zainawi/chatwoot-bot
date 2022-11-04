"""Describe IncomingMessage class"""


class IncomingMessage:
    """Store and process incoming message event payload"""
    def __init__(self, payload):
        if (payload['event'] != 'message_created'
            or payload['message_type'] != 'incoming'):
            raise ValueError('Invalid event')

        self.payload = payload

    def get_content_type(self):
        """Get message content type (text or whatever)"""
        return self.payload['content_type']

    def get_message_type(self):
        """Get message type (incoming or outgoing)"""
        return self.payload['message_type']

    def get_message_content(self):
        """Get message content"""
        return self.payload['content']

    def has_assignee(self):
        """Determine whether the conversation has assignee or not"""
        return self.payload['conversation']['meta']['assignee'] is not None

    def get_sender_name(self):
        """Get incoming message sender name"""
        return self.payload['sender']['name']

    def get_conversation_id(self):
        """Get the conversation ID"""
        return self.payload['conversation']['id']
