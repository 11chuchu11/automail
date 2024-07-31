import os
from typing import Union
import flask
from flask_cors import CORS
from src.routes.route import route


app = flask.Flask(__name__)
#!Cambiar esto y generar una secret key extraida de .env


app.secret_key=b'_5#y2L"F4Q8z\n\xec]/'
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(route, url_prefix='/api')

if __name__== '__main__':
    #! EN PRODUCCION ELIMINAR ESTO
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.run('localhost', 8000, debug=True)
