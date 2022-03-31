import json
import requests 
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
class MessagesResource(Resource): 
    @jwt_required()
    def get(self, other_id):
        current_user_id = get_jwt_identity()
        data = requests.get('http://localhost:5001/message/'+str(other_id)+'/'+str(current_user_id))
        return json.loads((data.text)), data.status_code 