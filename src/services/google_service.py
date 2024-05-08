import os
import flask 
import requests

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

from src.utils.helpers import google_credentrials_to_dict


from src.configs.config import google_client_config, scope_gmail_read_messages

class Google_auth_service:  
  
  def __init__(self):
    self.scopes=[scope_gmail_read_messages]
  
  def auth(self, redirect_uri:str):
    flow = google_auth_oauthlib.flow.Flow.from_client_config(client_config=google_client_config, scopes=self.scopes)
    flow.redirect_uri = redirect_uri
    
    authorization_url, state = flow.authorization_url(acces_type='offline', include_granted_scopes='true')
    return authorization_url, state
  
  def oauth2callback(self, redirect_uri:str,state, authorization_response:str):
    flow = google_auth_oauthlib.flow.Flow.from_client_config(client_config=google_client_config, scopes=self.scopes, state=state)
    flow.redirect_uri = redirect_uri
        
    authorization_response=authorization_response
    flow.fetch_token(authorization_response=authorization_response)
    
    credentials=flow.credentials
    return google_credentrials_to_dict(credentials)