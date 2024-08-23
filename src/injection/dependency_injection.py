
from dependency_injector import containers, providers

from src.services.google_auth_service import Google_auth_service

from src.controllers.test_controller import Test_controller
from src.controllers.google_auth_controller import Google_auth_controller

class Container (containers.DeclarativeContainer):
  config = providers.Configuration()
  
  Google_auth_service = providers.Factory(Google_auth_service)
  
  Test_controller = providers.Factory(Test_controller)
  Google_auth_controller = providers.Factory(Google_auth_controller, Google_auth_service= Google_auth_service)
  

container = Container()