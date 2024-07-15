import os
import flask 
import requests

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from authlib.integrations.flask_client import OAuth

from src.utils.helpers import google_credentrials_to_dict


from src.configs.config import google_client_config, scope_gmail_read_messages

class Google_auth_service:  
  _scopes=[scope_gmail_read_messages]
  
  
  def __init__(self, app):
    _oauth = OAuth(app)
    _oauth.register(
      name='google',
      client_id=google_client_config['client_id'],
      client_secret=google_client_config['client_secret'],
      authorize_url=google_client_config['auth_uri'],
      server_metadata_url=google_client_config['openid_url'],
      client_kwargs={
        'scope': 'openid email profile'
    }
      )
    
  def login(self, redirect_uri):
    return self._oauth.google.authorize_redirect(redirect_uri)
  
  def auth(self, redirect_uri:str):
    token = self._oauth.google.authorize_access_token()
    return token
  
  def refresh(self, token):
    creds = Credentials(token['access_token'], refresh_token=token.get('refresh_token'),token_uri=google_client_config['token_uri'], client_id=google_client_config['client_id'], client_secret=google_client_config['client_secret'])
    if creds.expired and creds.refresh_token:
      creds.refresh(Request())
      token['access_token'] = creds.token
    return creds
  
  def revoke(self, credentials):
    credentials = google.oauth2.credentials.Credentials(**credentials)
    revoke = requests.post('https://oauth2.googleapis.com/revoke',params={'token': credentials.token},headers = {'content-type': 'application/x-www-form-urlencoded'})
    status_code = getattr(revoke, 'status_code')
    return status_code
  
  #TODO logica para eliminar credenciales de la base de datos
  def clear_credentials(): pass