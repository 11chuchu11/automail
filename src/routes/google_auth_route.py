from flask import Blueprint
from src.injection.dependency_injection import Container
from src.controllers.google_auth_controller import Google_auth_controller


google_auth_controller:Google_auth_controller = Container.resolve('Google_auth_controller')

google_auth_route = Blueprint('auth',__name__)

google_auth_route.route('/')(Google_auth_controller.auth)
google_auth_route.route('/oauth2callback')(Google_auth_controller.oauth2callback)
google_auth_route.route('/revoke')(Google_auth_controller.revoke)
google_auth_route.route('/clear')(Google_auth_controller.clear)
