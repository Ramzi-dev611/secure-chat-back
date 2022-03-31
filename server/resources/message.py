from flask import request 
from flask_restful import Resource
from http import HTTPStatus

from models.message import Message

class MessageListResource(Resource):
    def get(self, user1, user2):
        data = Message.get_list_messages(user1, user2)
        print(data)
        return data, HTTPStatus.OK

    def post(self, user1, user2):
        data = request.get_json()
        message = Message(
            sent_to=user2,
            sent_by=user1,
            message=data.get('message')
        )
        message.save()
        return {'message': 'saved message'}, HTTPStatus.CREATED
