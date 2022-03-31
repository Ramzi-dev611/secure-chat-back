from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from config import Config
from extensions import jwt, db

from resources.login import LoginResource
from resources.user import RegisterUserResource, UserResource
from resources.message import MessageListResource, MessageResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_resources(app)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app=app, db=db)
    jwt.init_app(app)

def register_resources(app):
    api = Api(app)
    api.add_resource(LoginResource, '/login')
    api.add_resource(RegisterUserResource, '/register')
    api.add_resource(UserResource, '/user')
    api.add_resource(MessageListResource, '/message/<int:user1>/<int:user2>')
    api.add_resource(MessageResource, '/message')

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5001)
