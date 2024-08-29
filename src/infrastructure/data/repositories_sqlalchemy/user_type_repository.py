from flask import Response

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound

from src.server.configs.database_connection import create_connection
from src.domain.repositories.user_type_repository_abs import User_Type_Repository_Abs
from src.infrastructure.data.repositories_sqlalchemy.models.user_type_model import User_Type
from src.infrastructure.data.repositories_sqlalchemy.models.base import Base
from src.domain.entities.user_type_entitie import User_Type_Entitie


class User_Type_Respository(User_Type_Repository_Abs):
  
  def __init__(self):
    engine = create_connection()
    Session = sessionmaker(bind=engine)
    self.session = Session()
    
    #*Chequea si la tabla esta creada sino la crea
    if not engine.dialect.has_table(engine.connect(), User_Type.__tablename__):
      Base.metadata.create_all(engine, tables=[User_Type.__tablename__])
    
  def find_all(self):
    session = self.session
    users_type = session.query(User_Type).all()
    results = [row.get_values() for row in users_type]
    return results

  def find_by_id(self, id):
    session = self.session
    user_type = session.query(User_Type).filter(User_Type.id == id).one()
    result = user_type.get_values()
    return result
  
  def add(self,row:User_Type_Entitie):
    session = self.session
    user_type = User_Type(name=row.name)
    session.add(user_type)
    session.commit()
    result = user_type.get_values()
    return result
  
  def update(self, id, row: User_Type_Entitie):
    session = self.session
    user_type = session.query(User_Type).filter(User_Type.id==id).first()
    user_type.name = row.name
    session.add(user_type)
    session.commit()
    result = user_type.get_values()
    return (result)
  
  def delete(self, id):
    session = self.session
    result = session.query(User_Type).filter(User_Type.id == id).delete()
    session.commit()
    
    if result == 0:
      raise NoResultFound()
    
    return ({"id":id})