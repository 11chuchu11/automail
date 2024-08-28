
from dependency_injector import containers, providers

from src.services.google_auth_service import Google_auth_service
from src.services.user_type_service import User_Type_Service

from src.controllers.test_controller import Test_controller
from src.controllers.google_auth_controller import Google_auth_controller
from src.controllers.user_type_controller import User_Type_Controller


class Container (containers.DeclarativeContainer):
  config = providers.Configuration()
  
  Google_auth_service = providers.Factory(Google_auth_service)
  User_Type_Service = providers.Factory(User_Type_Service)
  
  Test_controller = providers.Factory(Test_controller)
  Google_auth_controller = providers.Factory(Google_auth_controller, Google_auth_service= Google_auth_service)
  User_Type_Controller = providers.Factory(User_Type_Controller, User_Type_Service=User_Type_Service)

container = Container()