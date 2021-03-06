import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    MODEL_HB = 'HBrain vb0.3.3'

    ROS_SOURCE_PATH = '/opt/ros/indigo/setup.bash'

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    BOOTSTRAP_SERVE_LOCAL = True
    CATKIN_FOLDER = os.environ.get('CATKIN_FOLDER') or '/Users/ludus/develop/dotbot_ws/ros/'
    DOTBOT_PACKAGE_NAME = os.environ.get('DOTBOT_PACKAGE_NAME') or 'dotbot_app'
    ROS_ENVS = os.environ.get('ROS_ENVS') or '/opt/ros/indigo/setup.bash'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'

    REDIS_URL='redis://localhost:6379'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
