from flask import Blueprint

api = Blueprint('api', __name__)

from . import auth_controller, guest_controller, episode_controller, appearance_controller