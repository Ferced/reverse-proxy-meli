import os

basedir = os.path.abspath(os.path.dirname(__file__))
os.environ['REVERSEPROXY_ENV']='dev'

class Config:
    
    SECRET_KEY = os.getenv("SECRET_KEY", "DFJ8F2382RJSDFJ238922TJWE3FWEFWJE2")
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_HOST = "mongodb"
    MONGODB_PORT = 27017
    MONGODB_NAME = "reverse-proxy-dev"
    REDIS_HOST = "redis"
    REDIS_PORT = "6379"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MONGODB_HOST = "0.0.0.0"
    MONGODB_PORT = 2717
    MONGODB_NAME = "reverse-proxy-test"
    REDIS_HOST = "localhost"
    REDIS_PORT = "6379"
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    MONGODB_HOST = "mongodb"
    MONGODB_PORT = 27017
    MONGODB_NAME = "reverse-proxy-prod"
    REDIS_HOST = "redis"
    REDIS_PORT = "6379"
    DEBUG = False


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)

key = Config.SECRET_KEY
