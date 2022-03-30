from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from models.message import Message

class MessageListResource(Resource):
    def get(self, user1, user2):
        data = Message.get_list_messages(user1, user2)
        return data, HTTPStatus.OK

class MessageResource(Resource):
    def post(self):
        data = request.get_json()
        message = Message(
            sent_to = data.get('sentTo'),
            sent_by = data.get('sentBy'),
            message = data.get('message')
        )
        message.save()
        return {'message': 'saved message'}, HTTPStatus.CREATED
