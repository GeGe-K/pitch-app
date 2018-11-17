 import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycop2://postgres:kiilumwikali@localhost/pitches'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}