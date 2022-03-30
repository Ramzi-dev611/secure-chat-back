import requests
from flask import request
from flask_restful import Resource

class LoginResource(Resource):
    def post(self):
        request_body = request.get_data()
        response = requests.post('http://localhost:5001/login', data=request_body)
        return response