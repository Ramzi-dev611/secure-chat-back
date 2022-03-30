import requests
from flask import request
from flask_restful import Resource

class RegisterResource(Resource):
    def post(self):
        request_body = request.get_data()
        response = requests.post('http://localhost:5001/register', data=request_body)
        return response