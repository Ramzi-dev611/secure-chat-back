from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, create_access_token
from http import HTTPStatus
from utils import hash_password
from models.user import User


class RegisterUserResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        if User.get_by_email(email):
            return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST
        if User.get_by_username(username):
            return {'message': 'username already used'}, HTTPStatus.BAD_REQUEST
        hashed = hash_password(password)
        user = User(username=username, email=email, password=hashed)
        user.save()
        access_token = create_access_token(identity=user.id)
        return {'token': access_token}, HTTPStatus.OK


class UserResource(Resource):
    def get(self):
        return User.get_all_users()

