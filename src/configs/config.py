import os
from dotenv import load_dotenv

load_dotenv()

#* google client config
client_id = os.getenv("GOOGLE_SECRET_FILE_CLIENT_ID")
project_id = os.getenv("GOOGLE_SECRET_FILE_PROJECT_ID")
auth_uri = os.getenv("GOOGLE_SECRET_FILE_AUTH_URI")
token_uri = os.getenv("GOOGLE_SECRET_FILE_TOKEN_URI")
cert_url = os.getenv("GOOGLE_SECRET_FILE_AUTH_PROVIDER_X509_CERT_URL")
client_secret = os.getenv("GOOGLE_SECRET_FILE_CLIENT_SECRET")
redirect_uris = os.getenv("GOOGLE_SECRET_FILE_REDIRECT_URIS")
javascript_origins = os.getenv("GOOGLE_SECRET_FILE_JAVASCRIPT_ORIGINS")


#* google scopes
scope_oauth_openid = os.getenv("GOOGLE_SCOPE_OAUTH_OPENID")

#*  google services
service_oauth_openid = os.getenv("GOOGLE_SERVICE_OPENID")
service_oauth_revoke_token = os.getenv("GOOGLE_SERVICE_REVOKE_TOKEN")

#* urls
host = os.getenv("HOST_URL")
auth = os.getenv("AUTH_PATH")
callback = os.getenv("CALLBACK_PATH")

google_client_config = {
  "client_id":client_id, 
  "project_id":project_id, 
  "auth_uri":auth_uri,
  "token_uri":token_uri,
  "cert_url":cert_url,
  "client_secret":client_secret,
  "redirect_uris":redirect_uris, 
  "javascript_origins":javascript_origins,
}

google_services = {
  "openid": service_oauth_openid,
  "revoke": service_oauth_revoke_token
}

google_scopes = {
  "openid": scope_oauth_openid
}

urls = {"host": host, "auth": auth, "callback": callback}


def url(param):
  uri = urls['host']
  if param != "host":
    uri = f"{urls['host']}/{urls['param']}"
  return uri