import requests

class MessagesService:
    instance = None

    @classmethod
    def get_instance(cls):
        if not cls.instance :
            cls.instance = MessagesService()
        return cls.instance

    def save_message(self, data):
        return requests.post('http://localhost:5002/message')