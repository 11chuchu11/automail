from flask import Blueprint
from src.controllers.google_auth_controller import Google_auth_controller
google_auth_route = Blueprint('auth',__name__)

google_auth_route.route('/')(Google_auth_controller.auth)