import requests
import json
from flask import request
from flask_restful import Resource

class LoginResource(Resource):
    def post(self):
        request_body = request.get_json()
        response = requests.post('http://localhost:5001/login', json=request_body)
        return json.loads((response.text)), response.status_code 