from src.infrastructure.data.repositories_sqlalchemy.user_type_repository import User_Type_Respository
from src.domain.entities.user_type_entitie import User_Type_Entitie
from src.infrastructure.sdk.validations.user_type_validation import User_Type_Validation_Schema

class User_Type_Service:
  
  def __init__ (self, User_Type_Respository: User_Type_Respository, User_Type_Validation_Schema: User_Type_Validation_Schema):
    self.user_type_repository = User_Type_Respository
    self.validation_schema = User_Type_Validation_Schema
    
  def find_all(self):
    response = self.user_type_repository.find_all()
    return response
  
  def find_by_id(self,id:int):
    response = self.user_type_repository.find_by_id(id)
    return response
  
  def add(self,row:User_Type_Entitie):
    user_type = User_Type_Entitie()
    user_type.set_from_dict(row)
    
    validation = self.validation_schema
    validation.load(user_type.json())
    
    response = self.user_type_repository.add(user_type)
    return response
  
  def update(self,id:int, row:User_Type_Entitie):
    user_type = User_Type_Entitie()
    user_type.set_from_dict(row)
    
    validation = self.validation_schema
    validation.load(user_type.json())
    
    response = self.user_type_repository.update(id, user_type)
    return response
  
  def delete(self,id):
    response = self.user_type_repository.delete(id)
    return response