#!/usr/bin/env python
# encoding: utf-8

import logging.config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__, template_folder="templates")

    @app.route('/static/<path:path>')
    def static_files():
        return app.send_static_file(path)

    app.config.from_object(config)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
   
    # attack routes and cunstom err pages here
    from app.demo import demo as demo_blueprint
    app.register_blueprint(demo_blueprint)

    return app
