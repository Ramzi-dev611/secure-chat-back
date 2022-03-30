class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://securechat:securechatpass123@localhost/securechatdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Lorem-Ipsum-super-secret'
    JWT_ERROR_MESSAGE_KEY = 'messagkey'
