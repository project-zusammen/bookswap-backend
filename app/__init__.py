from flask import Flask

from .extensions import api, db
from .resources import ns
from .config import Config
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)

    # "postgresql://postgres:tatapjang@localhost:5432/bookswap"
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI

    # Configure Flask-JWT-Extended
    # Replace with your secret key
    app.config['JWT_SECRET_KEY'] = Config.SECRET_KEY
    jwt = JWTManager(app)

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(ns)

    return app
