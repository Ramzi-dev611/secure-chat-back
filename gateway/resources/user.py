import requests
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

class UserListResource(Resource):
    @jwt_required
    def get(self):
        return requests.get('http://localhost:5002/user')
        