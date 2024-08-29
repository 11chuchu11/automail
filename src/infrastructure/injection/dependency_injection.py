
from dependency_injector import containers, providers

from src.infrastructure.sdk.validations.user_type_validation import User_Type_Validation_Schema

from src.infrastructure.data.repositories_sqlalchemy.user_type_repository import User_Type_Respository

from src.domain.services.google_auth_service import Google_auth_service
from src.domain.services.user_type_service import User_Type_Service

from src.server.controllers.google_auth_controller import Google_auth_controller
from src.server.controllers.user_type_controller import User_Type_Controller


class Container (containers.DeclarativeContainer):
  config = providers.Configuration()
  
  User_Type_Validation_Schema = providers.Factory(User_Type_Validation_Schema)
  
  User_Type_Repository = providers.Factory(User_Type_Respository)
  
  Google_auth_service = providers.Factory(Google_auth_service)
  User_Type_Service = providers.Factory(User_Type_Service, User_Type_Respository=User_Type_Repository, User_Type_Validation_Schema = User_Type_Validation_Schema)
  
  Google_auth_controller = providers.Factory(Google_auth_controller, Google_auth_service= Google_auth_service)
  User_Type_Controller = providers.Factory(User_Type_Controller, User_Type_Service=User_Type_Service)
  

container = Container()