import requests 
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
class MessagesResource(Resource): 
    @jwt_required
    def get(self, other_id):
        current_user_id = get_jwt_identity()
        return requests.get('http://localhost:5002/message/'+other_id+'/'+current_user_id)