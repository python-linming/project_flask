from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Config(object):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@192.168.25.255:3306/information27'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)

app.config.from_object(Config)

db =SQLAlchemy(app)

@app.route('/')
def index():
    return 'index222'

if __name__ == '__main__':
    app.run(debug=True)
    print('fuck')