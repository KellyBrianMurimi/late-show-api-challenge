# server/models/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

from .user import User
from .guest import Guest
from .episode import Episode
from .appearance import Appearance

def init_app(app):
    db.init_app(app)
    jwt.init_app(app)
