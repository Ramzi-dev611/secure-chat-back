from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from http import HTTPStatus
from utils import check_password
from models.user import User

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = User.get_by_email(email)
        if not user or not check_password(password, user.password):
            return {'Message': 'email or password wrongly presented'}, HTTPStatus.UNAUTHORIZED
        access_token = create_access_token(identity=user.id)
        return { 'token': access_token }, HTTPStatus.OK