import requests
import json
from flask import request
from flask_restful import Resource

class RegisterResource(Resource):
    def post(self):
        request_body = request.get_json()
        response = requests.post('http://localhost:5001/register', json=request_body)
        return json.loads((response.text)), response.status_code 