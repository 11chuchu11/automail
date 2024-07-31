import requests

from authlib.integrations.requests_client import OAuth2Session

from src.configs.config import google_client_config, google_scopes, google_services, url
from requests.compat import urljoin

class Google_auth_service:  
  _scope = google_scopes['openid']
  
  
  def __init__(self):
    self._client_id = google_client_config['client_id']
    self._client_secret = google_client_config['client_secret']
    self._auth_uri = google_client_config['auth_uri']
    self._token_uri = google_client_config['token_uri']
    self._revoke_uri = google_services['revoke']
    
    self._client = OAuth2Session(self._client_id, self._client_secret, scope=self._scope, token_endpoint=self._token_uri)
    
  def authorization_uri(self):
    AUTH_URI = self._auth_uri
    
    client = self._client
    
    client.redirect_uri = 'http://localhost:3000/auth/2'
    uri, state = client.create_authorization_url(AUTH_URI)
    return {"uri":uri, "state":state}
  
  def auth(self, data):
    TOKEN_URI = self._token_uri
    uriParams = data['url']
    
    client = self._client
    
    client.redirect_uri = 'http://localhost:3000/auth/2'
    url = urljoin('http://localhost:3000/auth/2', '?'+uriParams)
    token = client.fetch_token(TOKEN_URI, authorization_response=url)
    return token
  
  def revoke(self, data):
    REVOKE_URI = self._revoke_uri

    token = data["token"]    
    client = self._client
    respRevoke = client.revoke_token(REVOKE_URI, token=token["access_token"])
    print(respRevoke.json())
    return respRevoke.json()
    


  
