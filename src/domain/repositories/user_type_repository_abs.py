from abc import ABCMeta, abstractmethod

from src.domain.entities.user_type_entitie import User_Type_Entitie


class User_Type_Repository_Abs(metaclass=ABCMeta):
  @abstractmethod
  def find_all(self):
    pass

  @abstractmethod
  def find_by_id(self, id):
    pass
  
  
  @abstractmethod
  def add(self,row:User_Type_Entitie):
    pass
  
  @abstractmethod
  def update(self,id, row:User_Type_Entitie):
    pass
  
  @abstractmethod
  def delete(self,id):
    pass
