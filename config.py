import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:kiilumwikali@localhost/pitches'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}