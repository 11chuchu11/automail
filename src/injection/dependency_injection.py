from src.injection.container import Dependency_Container
from src.controllers.google_auth_controller import Google_auth_controller
from src.services.google_auth_service import Google_auth_service

Container = Dependency_Container.create_container()

Container.register({
  'Google_auth_controller':Google_auth_controller,
  'Google_auth_service':Google_auth_service,
})
