from flask import Blueprint
from src.injection.dependency_injection import container
from src.controllers.google_auth_controller import Google_auth_controller


google_auth_controller:Google_auth_controller = container.Google_auth_controller()

google_auth_route = Blueprint('google',__name__)

@google_auth_route.route('/', methods=['GET'])
def authorization_uri():
    return google_auth_controller.authorization_uri()

@google_auth_route.route('/auth', methods=['POST'])
def auth():
    return google_auth_controller.auth()
@google_auth_route.route('/revoke', methods=['POST'])
def revoke():
    return google_auth_controller.revoke()
