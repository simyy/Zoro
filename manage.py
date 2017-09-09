#!/usr/bin/env python
# encoding: utf-8

import os
import werkzeug
import werkzeug.debug
import werkzeug.serving

from app import create_app
from app import db
from app import models
from flask_script  import Manager
from flask_script  import Shell
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from gevent.wsgi import WSGIServer


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, models=models, logger=app.config.logger)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


@manager.command
def runserver(host="127.0.0.1", port=4000):
    """
    run a gevent-based WSGI server
    """
    port = int(port)

    wrapped_app = app 
    if app.config.get("DEBUG", False):
        wrapped_app = werkzeug.debug.DebuggedApplication(app)

    server = WSGIServer(listener=(host, port), application=wrapped_app)


    def serve():
        print(" * Running on http://%s:%d" % (host, port))
        server.serve_forever()

    if app.config.get("DEBUG", False):
        from gevent import monkey
        monkey.patch_all()
        werkzeug.serving.run_with_reloader(serve, reloader_type="auto") 

    else:
        serve()


if __name__ == '__main__':
    manager.run()
