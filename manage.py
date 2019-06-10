from redis import StrictRedis
from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session #指定session保存位置
from flask_script import Manager

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



app = Flask(__name__)
#加载配置
app.config.from_object(Config)
#初始化数据库
db =SQLAlchemy(app)
#初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
#开启当前项目CSRF保护
CSRFProtect(app)

Session(app)
manager = Manager(app)

@app.route('/')
def index():
    session['name'] = 'itheima'
    return 'index222'

if __name__ == '__main__':
   manager.run()
