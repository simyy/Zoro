#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config


db = SQLAlchemy()


def create_app(config_name):
    print(config_name)
    app = Flask(__name__, template_folder="templates")

    @app.route('/static/<path:path>')
    def static_files():
        return app.send_static_file(path)

    app.config.from_object(config[config_name])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
   
    # attack routes and cunstom err pages here
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
