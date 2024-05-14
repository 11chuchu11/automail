import flask 
from src.services.google_auth_service import Google_auth_service


class Google_auth_controller:
  __callback_uri='oauth2callback'
  
  def __init__(self, Google_auth_service: Google_auth_service) -> None:
    self._google_auth_service = Google_auth_service
    
    
  def auth(self):
    try:
      
      redirect_uri = flask.url_for(redirect_uri=self.__callback_uri, _external=True)
      authorization_url, state = self._google_auth_service.auth(redirect_uri=redirect_uri)
      flask.session['state'] = state
      return flask.redirect(authorization_url)
    except:
      print('ERROR')
      
      
  def oauth2callback(self):
    try:
      state = flask.session['state']
      credentials = self._google_auth_service.oauth2callback(redirect_uri=self.__callback_uri,state=state)
      flask.session['credentials'] = credentials
      return flask.redirect(flask.url_for('main_page'))
      
    except:
      print('ERROR')
  
  
  def revoke(self):
    home_uri = flask.url_for('landing')
    error_uri = flask.url_for('error_page')
    
    try:
      #TODO redireccionar a una pantalla home
      if 'credentials' not in flask.session: 
        return flask.redirect(home_uri)

      status_code = self._google_auth_service.revoke()

      if status_code == 200: return flask.redirect(home_uri)
      else: return flask.redirect(error_uri)
    except:
      print('ERROR')
    
  def clear(self):
    
    try:
      if 'credentials' in flask.session:
        del flask.session['credentials']
        return {'status':201}
    except:
      print('Error')