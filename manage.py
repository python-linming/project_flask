from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db, models

#manage.py是程序启动的入口，只关心启动的相关参数以及内容，不关心具体

app = create_app('development')
manager = Manager(app)
#将app与db关联
Migrate(app,db)
#将迁移命令添加到manager中
manager.add_command('db',MigrateCommand)



if __name__ == '__main__':

   manager.run()
