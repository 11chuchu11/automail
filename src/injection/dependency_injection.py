
from src.controllers.google_auth_controller import Google_auth_controller
from src.services.google_auth_service import Google_auth_service
from dependency_injector import containers, providers

class Container (containers.DeclarativeContainer):
  config = providers.Configuration()
  
  Google_auth_service = providers.Factory(Google_auth_service)
  
  Google_auth_controller = providers.Factory(Google_auth_controller, Google_auth_service= Google_auth_service)

container = Container()