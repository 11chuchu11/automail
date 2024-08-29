from flask import Blueprint
from src.server.routes.google_auth_route import google_auth_route
from src.server.routes.user_type_route import user_type_route


route= Blueprint('api',__name__)

route.register_blueprint(google_auth_route, url_prefix='/google')

route.register_blueprint(user_type_route, url_prefix='/user-type')
