import requests
import json
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from generate_header import get_header

class UserListResource(Resource):
    @jwt_required()
    def get(self):
        header = get_header()
        data = requests.get('http://server.securechat.tn:5001/user', headers=header)
        return json.loads((data.text)), data.status_code 