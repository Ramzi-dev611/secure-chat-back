import requests
import json
from flask import request
from flask_restful import Resource
from generate_header import get_header

class LoginResource(Resource):
    def post(self):
        header = get_header()
        request_body = request.get_json()
        response = requests.post('http://server.securechat.tn:5001/login', json=request_body, headers=header)
        return json.loads((response.text)), response.status_code 