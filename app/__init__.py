#!/usr/bin/env python
# encoding: utf-8

import yaml
import logging.config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config


db = SQLAlchemy()


def init_logging():
    with open('app/logging.yaml') as f:
        D = yaml.load(f)
        D.setdefault('version', 1)
        logging.config.dictConfig(D)
        return logging.getLogger()

logger = init_logging()


def create_app(config_name):
    print(config_name)
    app = Flask(__name__, template_folder="templates")

    @app.route('/static/<path:path>')
    def static_files():
        return app.send_static_file(path)

    app.config.from_object(config[config_name])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)

    app.config.logger = logger
   
    # attack routes and cunstom err pages here
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
