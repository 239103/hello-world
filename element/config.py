'''Application configuration'''
import os
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('o\xedU|k5TF%\x848\xfbR[j\x98')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    
    FLASKY_MAIL_SUBJECT_PREFIX = '[Element]'
    FLASKY_MAIL_SENDER = 'David Chan <chenwei2@sf-express.com>'
    FLASKY_ADMIN = os.environ.get('Element_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = '127.0.0.1'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
'development': DevelopmentConfig,
'testing': TestingConfig,
'Production': ProductionConfig,
'default': DevelopmentConfig
}
