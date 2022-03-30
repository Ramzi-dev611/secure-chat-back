from flask import Flask
from flask_restful import Api
from flask_sock import Sock

from services.message_service import MessagesService

from resources.login import LoginResource
from resources.messages import MessagesResource
from resources.register import RegisterResource
from resources.user import UserListResource

from config import Config
from extensions import jwt 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_resources(app)
    register_sockets(app)
    return app


def register_extensions(app):
    jwt.init_app(app)

def register_resources(app):
    api = Api(app)
    api.add_resource(LoginResource, '/login')
    api.add_resource(MessagesResource, '/message/<int:other_id>')
    api.add_resource(RegisterResource, '/register')
    api.add_resource(UserListResource, '/user')

def register_sockets(app):
    sock = Sock(app)
    @sock.route('/messages')
    def echo(ws):
        while True:
            text = ws.receive()
            service = MessagesService.get_instance()
            service.save_message(text)
            ws.send(text)


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)