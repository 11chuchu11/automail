import flask 
from src.services.google_service import Google_auth_service


class Google_auth_controller:
  __google_auth_service: Google_auth_service
  __callback_uri='oauth2callback'
  
  def __init__(self, google_auth_service: Google_auth_service) -> None:
    self.__google_auth_service = google_auth_service
    
    
  def auth(self):
    try:
      
      redirect_uri = flask.url_for(redirect_uri=self.__callback_uri, _external=True)
      authorization_url, state = self.__google_auth_service.auth(redirect_uri=redirect_uri)
      flask.session['state'] = state
      return flask.redirect(authorization_url)
    except:
      print('ERROR')
      
  def oauth2callback(self):
    try:
      state = flask.session['state']
      credentials = self.__google_auth_service.oauth2callback(redirect_uri=self.__callback_uri,state=state)
      flask.session['credentials'] = credentials
      return flask.redirect(flask.url_for('main_page'))
      
    except:
      print('ERROR')
  
  def revoke():
    return