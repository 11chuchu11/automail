import os
from dotenv import load_dotenv

load_dotenv()

google_client_config = {
  "client_id":os.getenv("GOOGLE_SECRET_FILE_CLIENT_ID"),
  "project_id":os.getenv("GOOGLE_SECRET_FILE_PROJECT_ID"), 
  "auth_uri":os.getenv("GOOGLE_SECRET_FILE_AUTH_URI"),
  "token_uri":os.getenv("GOOGLE_SECRET_FILE_TOKEN_URI"),
  "cert_url":os.getenv("GOOGLE_SECRET_FILE_AUTH_PROVIDER_X509_CERT_URL"),
  "client_secret":os.getenv("GOOGLE_SECRET_FILE_CLIENT_SECRET"),
  "redirect_uris":os.getenv("GOOGLE_SECRET_FILE_REDIRECT_URIS"), 
  "javascript_origins":os.getenv("GOOGLE_SECRET_FILE_JAVASCRIPT_ORIGINS"),
}

google_services = {
  "openid": os.getenv("GOOGLE_SERVICE_OPENID"),
  "revoke": os.getenv("GOOGLE_SERVICE_REVOKE_TOKEN")
}

google_scopes = {
  "openid": os.getenv("GOOGLE_SCOPE_OAUTH_OPENID"),
}

#*BBDD
bbdd = {
  "engine": os.getenv("BBDD_ENGINE"),
  "name_db":os.getenv("BBDD_NAME_DB"),
  "user": os.getenv("BBDD_USER"),
  "pssw": os.getenv("BBDD_PSSW"),
  "host": os.getenv("BBDD_HOST"),
  "port": os.getenv("BBDD_PORT"),
  "max_connections": os.getenv("BBDD_MAX_CONNECTIONS"),
}


urls = {
  "host": os.getenv("HOST_URL"),
  "auth": os.getenv("AUTH_PATH"),
  "callback": os.getenv("CALLBACK_PATH")}


def url(param):
  uri = urls['host']
  if param != "host":
    uri = f"{urls['host']}/{urls['param']}"
  return uri