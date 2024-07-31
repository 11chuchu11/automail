from flask import request 
from src.services.google_auth_service import Google_auth_service


class Google_auth_controller:

  
  def __init__(self, Google_auth_service: Google_auth_service) -> None:
    self._google_auth_service = Google_auth_service
    
  def authorization_uri(self):
    response = self._google_auth_service.authorization_uri()
    return response
    
  def auth(self):
    data = request.json
    response = self._google_auth_service.auth(data)
    return response
  
  def revoke(self):
    data = request.json
    return self._google_auth_service.revoke(data)