import requests
import json
class MessagesService:
    instance = None

    @classmethod
    def get_instance(cls):
        if not cls.instance :
            cls.instance = MessagesService()
        return cls.instance

    @classmethod
    def get_messages(cls):
        data = requests.get('http://localhost:5001/message/')
        return json.loads((data.text)), data.status_code 

    def save_message(self, content):
        data = requests.post('http://localhost:5001/message', json=content)
        return json.loads((data.text)), data.status_code 