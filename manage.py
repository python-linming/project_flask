import logging

from flask import session, current_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db

app = create_app('development')
manager = Manager(app)
#将app与db关联
Migrate(app,db)
#将迁移命令添加到manager中
manager.add_command('db',MigrateCommand)

@app.route('/')
def index():
    # session['name'] = 'itheima'
    #测试打印日志
    logging.debug('测试debug')
    logging.warning('测试debug')
    logging.error('测试debug')
    logging.fatal('测试debug')
    # current_app.logger.error('测试error')
    return 'index222'

if __name__ == '__main__':
   manager.run()
