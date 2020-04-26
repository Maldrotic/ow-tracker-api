from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import config

from resources.user import User


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    db.init_app(app)

    api = Api(app)
    api.add_resource(User)

    return app