import requests
import json
from flask_jwt_extended import jwt_required
from flask_restful import Resource

class UserListResource(Resource):
    @jwt_required()
    def get(self):
        data = requests.get('http://server.securechat.tn:5001/user')
        return json.loads((data.text)), data.status_code 