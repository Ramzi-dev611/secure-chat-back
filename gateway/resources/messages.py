import json
import requests 
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from generate_header import get_header
from flask_restful import Resource
class MessagesResource(Resource): 
    @jwt_required()
    def get(self, other_id):
        header = get_header()
        current_user_id = get_jwt_identity()
        data = requests.get('http://server.securechat.tn:5001/message/'+str(other_id)+'/'+str(current_user_id), headers=header)
        return json.loads((data.text)), data.status_code 

    @jwt_required()
    def post(self, other_id):
        header = get_header()
        current_user_id = get_jwt_identity()
        request_body = request.get_json()
        data = requests.post('http://server.securechat.tn:5001/message/'+str(current_user_id)+'/'+str(other_id), json=request_body, headers=header)
        return json.loads((data.text)), data.status_code 