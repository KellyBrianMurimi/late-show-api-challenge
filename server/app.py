from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import Config
from server.models import db
from server.controllers import (
    auth_controller,
    episode_controller,
    guest_controller,
    appearance_controller
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)
    
    # Auth routes
    app.route('/register', methods=['POST'])(auth_controller.register)
    app.route('/login', methods=['POST'])(auth_controller.login)
    
    # Episode routes
    app.route('/episodes', methods=['GET'])(episode_controller.get_episodes)
    app.route('/episodes/<int:id>', methods=['GET'])(episode_controller.get_episode)
    app.route('/episodes/<int:id>', methods=['DELETE'])(episode_controller.delete_episode)
    
    # Guest routes
    app.route('/guests', methods=['GET'])(guest_controller.get_guests)
    
    # Appearance routes
    app.route('/appearances', methods=['POST'])(appearance_controller.create_appearance)
    
    return app