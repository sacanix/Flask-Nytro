#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask.ext.script import Manager
from sample_app import create_app, db, models

app = create_app()
manager = Manager(app)

@manager.command
def syncdb():
    db.create_all(app=app)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, models=models)

if __name__ == '__main__':
    manager.run()