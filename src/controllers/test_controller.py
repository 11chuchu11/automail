from flask import request 
from src.repositories.orm.user_type_repository import User_Type_Respository
from src.entities.user_type_entitie import User_Type_Entitie


class Test_controller:
  
  def find_all(self):
    return User_Type_Respository().find_all()
  
  def find_by_id(self, id):
    id = int(id)
    return User_Type_Respository().find_by_id(id)

  def add(self):
    data = request.json
    user_type = User_Type_Entitie()
    user_type.set_from_dict(data)
    return User_Type_Respository().add(user_type)
  
  def update(self,id):
    if(id):
      id = int(id)
    data = request.json
    user_type = User_Type_Entitie()
    user_type.set_from_dict(data)

    return User_Type_Respository().update(id, user_type)
    
  def delete(self,id):
    if(id):
      id = int(id)
      return User_Type_Respository().delete(id)