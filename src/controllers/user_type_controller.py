from flask import request

from entities.user_type_entitie import User_Type_Entitie
from src.services.user_type_service import User_Type_Service

class User_Type_Controller:
  
  def __init__(self, User_Type_Service:User_Type_Service):
    self.user_type_service = User_Type_Service
    
  def find_all(self):
    response = self.user_type_service.find_all()
    return response
  
  def find_by_id(self, id): 
    id = int(id)
    response = self.user_type_service.find_by_id(id)
    return response
    
  def add(self):
    data = request.json
    user_type = User_Type_Entitie()
    user_type.set_from_dict(data)
    
    response = self.user_type_service.add(user_type)
    return response
  
  def update(self, id):
    id = int(id)
    data = request.json
    user_type = User_Type_Entitie()
    user_type.set_from_dict(data)
    
    response = self.user_type_service.update(id, data)
    return response
  
  def delete(self, id):
    id = int(id)
    response = self.user_type_service.delete(id)
    return response
    