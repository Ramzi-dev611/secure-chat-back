from extensions import db
from sqlalchemy import text
from flask import jsonify

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(), nullable=False,
                           server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False,
                           server_default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all_users(cls):
        query = text("select * from public.user")
        result = db.session.execute(query)
        return [{'id': row['id'], 'username': row['username']} for row in result]

    def save(self):
        db.session.add(self)
        db.session.commit()
