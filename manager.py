#coding:utf8
from flask import  Flask
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from ihome import db,create_app



app=create_app('develop')

#创建管理工具对象
manager=Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__=="__main__":
    # print (app.url_map)
    manager.run()