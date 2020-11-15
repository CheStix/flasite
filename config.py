import os
import secret_conf


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or secret_conf.SECRET_KEY
    # mail conf
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.yandex.ru')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', secret_conf.MAIL_USERNAME)
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', secret_conf.MAIL_PASSWORD)
    FLASITE_MAIL_SUBJECT_PREFIX = '[Flasite]'
    FLASITE_MAIL_SENDER = secret_conf.MAIL_USERNAME
    FLASITE_ADMIN = secret_conf.FLASITE_ADMIN
    FLASITE_POSTS_PER_PAGE = 10
    FLASITE_FOLLOWERS_PER_PAGE = 50
    # SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'db-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
