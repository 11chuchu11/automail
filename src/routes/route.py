from flask import Blueprint
from src.routes.google_auth_route import google_auth_route
from src.routes.test_route import test_route
from src.routes.user_type_route import user_type_route


route= Blueprint('api',__name__)

route.register_blueprint(google_auth_route, url_prefix='/google')
route.register_blueprint(test_route, url_prefix='/test')
route.register_blueprint(user_type_route, url_prefix='/user-type')
