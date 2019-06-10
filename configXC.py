import logging

from redis import StrictRedis


class Config(object):
    #项目的配置
    DEBUG = True
    SECRET_KEY = "b'q8TpYy2LUznFeGhmBro/pE9jxAUzVq9Z0dVlAYUq9vStAS64rGWLGDuzEb74LE4I'"
    #为数据库添加配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@192.168.25.255:3306/information27'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #redis配置
    REDIS_HOST = '192.168.25.129'
    REDIS_PORT = 6379
    #Session保存位置
    SESSION_TYPE = 'redis'
    #开启session签名
    SESSION_USE_SIGNER = True
    #制定Session保存的 redis
    SESSION_REDIS = StrictRedis(host = REDIS_HOST,port = REDIS_PORT)
    #设置需要过期
    SESSION_PERMAENT = False
    #设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400*2
    #设置日志等级
    LOG_LEVEL = logging.DEBUG

class DevelopmentConfig(Config):
    """开发环境下的配置"""
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = True
    LOG_LEVEL = logging.WARNING

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

config = {
    "development":DevelopmentConfig,
    "production":ProductionConfig,
    "testing":TestingConfig

}


