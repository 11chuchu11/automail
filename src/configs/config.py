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

google_client_config = {"web": {
  "client_id":client_id, 
  "project_id":project_id, 
  "auth_uri":auth_uri,
  "token_uri":token_uri,
  "cert_url":cert_url,
  "client_secret":client_secret,
  "redirect_uris":redirect_uris, 
  "javascript_origins":javascript_origins
}}

#*  google services
scope_gmail_read_messages = os.get_env("GOOGLE_SCOPE_OAUTH_GMAIL_READ_MESSAGES")
gmail_service = os.getenv("GOOGLE_SERVICE_GMAIL")
gmail_service_version = os.getenv("GOOGLE_GMAIL_VERSION")