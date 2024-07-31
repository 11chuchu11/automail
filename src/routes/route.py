from flask import Blueprint
from src.routes.google_auth_route import google_auth_route

route= Blueprint('api',__name__)

route.register_blueprint(google_auth_route, url_prefix='/google')
