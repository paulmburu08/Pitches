import os

class Config:
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://paul:pauldatabase@localhost/pitches'
    SECRET_KEY = os.environ.get('secret_key')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}